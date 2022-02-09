#                EFEL for ABF Formatted Files TEST FILE
#                   *Created by AY on 12/28/2020*
#                   *Last Updated on 1/21/2022*
#     *For any issues or bugs, please contact alex.yonk2@gmail.com*

#The following libraries must be installed before being imported!

import efel
import numpy as np
import pyabf
from tkinter import filedialog
from matplotlib import pyplot as plt

#Opens a dialog box allowing the user to select the file and removes the extension from the file name
file_path = filedialog.askopenfilename()
file = file_path[:-4]

#Sets settings for derivative threshold, interpolation step, and calculation of RMP
efel.setDoubleSetting('interp_step',0.05) #Must be set to the sampling rate (20,000 Hz = 0.05)
efel.setDoubleSetting('voltage_base_start_perc',0.1) #Used for RMP calculation
efel.setDoubleSetting('voltage_base_end_perc',0.8) #Used for RMP calculation
efel.setDerivativeThreshold(15) #Normally set to 15

#Import ABF file and assign the corresponding data to Time and RawData variables
File = pyabf.ABF(file_path)
Time = (File.sweepX)*1000
RawData = File.data

#Identify the number of traces in the abf file (*Note: this is designed for a 20kHz recording lasting ~10s)
#Other differences in recording will need to change these values
RawData = np.transpose(RawData)
TraceNum = int((len(RawData) / 200000))

#Using the number of calulcated traces, split the first RawData column into equal arrays of 200000
#Then, concatenate the arrays together and segment out the first 35000 sampling points 
# (the last 165000 points are irrelevant)
SortedData = np.split(RawData[:,0],TraceNum,0)
SortedData = np.column_stack(SortedData)
SortedData = SortedData[0:35000,:]
Time = Time[:35000]

#Determine where the first spike occurs to calculate Threshold_AP information and starting point for trace analysis
SpikeRows,SpikeColumns = np.where(SortedData > 10)
StartingColumn = min(SpikeColumns)
IterVar = StartingColumn

#Global variables are created outside the loop to store each trace as a dictionary in a list and store ancillary values
AllAverages = []
trace_results = {}

#Loop that cycles through each trace, extracts the pertinent information, computes other parameters, 
#and stores it into its own dictionary
for i in SortedData[IterVar:TraceNum:1]:
    trace1 = {}
    trace1['T'] = Time[:]
    trace1['V'] = SortedData[:,IterVar]
    trace1['stim_start'] = [256.3] #Value set to 257 to exclude depolarization step (normally is 256.3)
    trace1['stim_end'] = [1256.3]
    traces = [trace1]
    
    #NOTE: EFEL FEATURE EXTRACTION WILL NOT RUN IF ONLY ONE SPIKE IS DETECTED!!!!
    #Thus, this piece of code assesses if only one spike is present in a trace
    #If only one spike is detected, it will extract the pertinent features, compute other parameters, and save it within a 
    #list of dictionaries that will be outputted as a CSV
    #Additionally, further parameters (Max Frequency/Mean Instantaneous Frequency/etc.) will not be calculated for this trace
    #Once these calculations are done, the iterable variable will move onto the next trace 
    traces_results = efel.getFeatureValues(traces,['Spikecount'])
    if traces_results[0]['Spikecount'] == 1:
        traces_results = efel.getFeatureValues(traces,['Spikecount','AP_rise_time','min_AHP_values','AP_begin_voltage','AP_amplitude',
                                                       'AP_begin_indices','spike_half_width'])
        
        AP_Latency = Time[traces_results[0]['AP_begin_indices'][0]] - 256.3
        trace_results['AHP'] = traces_results[0]['min_AHP_values'] - traces_results[0]['AP_begin_voltage']
        Threshold_AP = {'AP_Latency': AP_Latency, 'AP_Threshold': traces_results[0]['AP_begin_voltage'][0],
                        'AP_Amplitude': traces_results[0]['AP_amplitude'][0],'AP_Rise': 
                        traces_results[0]['AP_rise_time'][0],'AP_Half-Height_Width': float(traces_results[0]['spike_half_width']),
                        'AHP_Amplitude': trace_results['AHP'][0]}
        IterVar += 1
        continue
    
    #If the one spike error DOES NOT occur, the code continues
    traces_results = efel.getFeatureValues(traces,[
                                            'AP_begin_voltage','voltage_base','AP_amplitude','AP_rise_time',
                                            'Spikecount','min_AHP_values','AP_begin_indices','peak_time',
                                            'ISI_values','spike_width2','time_to_first_spike','peak_indices','peak_voltage'])
    
    #New Error: Detection of multiple peak_indices that don't have corresponding AP_begin_indices due to derivative threshold
    if traces_results[0]['Spikecount'] != len(traces_results[0]['AP_begin_indices']):
        Limit = len(traces_results[0]['AP_begin_indices'])
        trace_results['Spikecount'] = Limit
        trace_results['min_AHP_values'] = traces_results[0]['min_AHP_values'][0:Limit]
        trace_results['spike_width2'] = traces_results[0]['spike_width2'][0:Limit]
        trace_results['peak_voltage'] = traces_results[0]['peak_voltage'][0:Limit]
        trace_results['AP_amplitude'] = trace_results['peak_voltage'][0:Limit] - traces_results[0]['AP_begin_voltage'][0:Limit]
        trace_results['ISI_values'] = traces_results[0]['ISI_values'][0:Limit]
        
        #Calculate AHP
        trace_results['AHP'] = trace_results['min_AHP_values'] - traces_results[0]['AP_begin_voltage']
    
        #Calculate Duration of Spiking
        trace_results['SpikeDur'] = Time[traces_results[0]['AP_begin_indices'][-1]] - Time[traces_results[0]['AP_begin_indices'][0]]
                
        #Calculate Frequency Parameters (Mean Instantaneous, Max, and Frequency Adaptation)
        Frequency = 1/trace_results['ISI_values']
        trace_results['MeanInstFreq'] = np.mean(Frequency)
        trace_results['MaxFreq'] = max(Frequency)
        trace_results['FreqAdapt'] = Frequency[-1] / Frequency[0]
        
        #Calculate AP Parameters (mean AP Amplitude and Peak Adaptation)
        trace_results['MeanAPAmp'] = np.mean(trace_results['AP_amplitude'])
        trace_results['PeakAdapt'] = trace_results['AP_amplitude'][-1] / trace_results['AP_amplitude'][0]
    
        #Calculate AHP Parameters (mean AHP Amplitude and AHP Peak Adaptation)
        trace_results['MeanAHPAmp'] = np.mean(trace_results['AHP'])
        trace_results['AHPAdapt'] = trace_results['AHP'][-1] / trace_results['AHP'][0]
    
        averages = {'AP #': int(trace_results['Spikecount']), 'Duration_of_Spiking': trace_results['SpikeDur'],
            'Mean_Instantaneous_Frequency':trace_results['MeanInstFreq'],'Max_Frequency': trace_results['MaxFreq'],
            'Frequency_Adaptation': trace_results['FreqAdapt'], 'Mean_AP_Amplitude': trace_results['MeanAPAmp'],
            'Peak_Adaptation': trace_results['PeakAdapt'], 'Mean_AHP_Amplitude': trace_results['MeanAHPAmp'],
            'AHP_Adaptation': trace_results['AHPAdapt']}
    
        AllAverages.append(averages)
        
    #Normal analysis of traces
    if traces_results[0]['Spikecount'] == len(traces_results[0]['AP_begin_indices']):

        #Calculate initial ISI value and insert this value into the 0 position of ISI values
        FirstISI = traces_results[0]['peak_time'][1] - traces_results[0]['peak_time'][0]
        trace_results['ISI_values'] = np.insert(traces_results[0]['ISI_values'],0,FirstISI)

        #Calculate AHP amplitude values
        #trace_results['AHP'] = traces_results[0]['min_AHP_values'] - traces_results[0]['AP_begin_voltage']
    
        #Calculate Duration of Spiking
        trace_results['SpikeDur'] = Time[traces_results[0]['AP_begin_indices'][-1]] - Time[traces_results[0]['AP_begin_indices'][0]]
                
        #Calculate Frequency Parameters (Mean Instantaneous, Max, and Frequency Adaptation)
        Frequency = 1/trace_results['ISI_values']
        trace_results['MeanInstFreq'] = np.mean(Frequency)
        trace_results['MaxFreq'] = max(Frequency)
        trace_results['FreqAdapt'] = Frequency[-1] / Frequency[0]
    
        #Calculate AP Parameters (mean AP Amplitude and Peak Adaptation)
        trace_results['MeanAPAmp'] = np.mean(traces_results[0]['AP_amplitude'])
        trace_results['PeakAdapt'] = traces_results[0]['AP_amplitude'][-1] / traces_results[0]['AP_amplitude'][0]
    
        #Calculate AHP Parameters (mean AHP Amplitude and AHP Peak Adaptation)
        #trace_results['MeanAHPAmp'] = np.mean(trace_results['AHP'])
        #trace_results['AHPAdapt'] = trace_results['AHP'][-1] / trace_results['AHP'][0]
        
        '''
        averages = {'AP #': int(traces_results[0]['Spikecount']), 'Duration_of_Spiking': trace_results['SpikeDur'],
            'Mean_Instantaneous_Frequency':trace_results['MeanInstFreq'],'Max_Frequency': trace_results['MaxFreq'],
            'Frequency_Adaptation': trace_results['FreqAdapt'], 'Mean_AP_Amplitude': trace_results['MeanAPAmp'],
            'Peak_Adaptation': trace_results['PeakAdapt'], 'Mean_AHP_Amplitude': trace_results['MeanAHPAmp'],
            'AHP_Adaptation': trace_results['AHPAdapt']}
        
        AllAverages.append(averages)
    '''
    plt.plot(Time,SortedData[:,IterVar])
    plt.show()
    
    IterVar += 1