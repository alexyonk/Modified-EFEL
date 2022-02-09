#                    EFEL for ABF Formatted Files
#                   *Created by AY on 12/28/2020*
#                   *Last Updated on 2/5/2021*
#     *For any issues or bugs, please contact alex.yonk2@gmail.com*


#The following libraries must be installed before being imported!
import efel
import numpy as np
import pyabf
from csv import DictWriter
from tkinter import filedialog

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

#Global variables are created outside the loop to store each trace as a dictionary in a list
AllAverages = []
trace_results = {}
SpikeCount = 0

#Loop that cycles through each trace, extracts the pertinent information, computes other parameters, 
#and stores it into its own dictionary
for i in SortedData[IterVar:TraceNum:1]:
    trace1 = {}
    trace1['T'] = Time[:]
    trace1['V'] = SortedData[:,IterVar]
    trace1['stim_start'] = [257] #Value set to 257 to exclude depolarization step (normally is 256.3)
    trace1['stim_end'] = [1256.3]
    traces = [trace1]
    traces_results = efel.getFeatureValues(traces,['Spikecount'])
    
    #If Spikecount is equal to 0, append a 0 to AllAverages variable, and move onto next trace
    if traces_results[0]['Spikecount'] == 0:
        print('No spikes in trace ' + str(IterVar))
        AllAverages.append(0)
        IterVar += 1
        continue
    
    #If Spikecount equals one, calculate Threshold_AP parameters, append "1" to AllAverages, and continue
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
    
    #If the one spike error WILL NOT occur, the code continues as normal
    traces_results = efel.getFeatureValues(traces,[
                                            'AP_begin_voltage','voltage_base','AP_amplitude','AP_rise_time',
                                            'Spikecount','min_AHP_values','AP_begin_indices','peak_time',
                                            'ISI_values','spike_width2','peak_voltage'])
    
    #Calculate initial ISI value and insert this value into the 0 position of ISI values
    FirstISI = traces_results[0]['peak_time'][1] - traces_results[0]['peak_time'][0]
    trace_results['ISI_values'] = np.insert(traces_results[0]['ISI_values'],0,FirstISI)
    
    #Another error comes about if more AHP or threshold AP values are detected
    #This code automatically removes the problematic errors and makes the number of values equal for further calculations
    if len(traces_results[0]['min_AHP_values']) != len(traces_results[0]['AP_begin_voltage']):
        if len(traces_results[0]['min_AHP_values']) > len(traces_results[0]['AP_begin_voltage']):
            Diff = len(traces_results[0]['min_AHP_values']) - len(traces_results[0]['AP_begin_voltage'])
            traces_results[0]['min_AHP_values'] = traces_results[0]['min_AHP_values'][0:traces_results[0]['min_AHP_values'].size-Diff]
            traces_results[0]['peak_voltage'] = traces_results[0]['peak_voltage'][0:traces_results[0]['peak_voltage'].size-Diff]
            traces_results[0]['Spikecount'] = traces_results[0]['Spikecount']-Diff
            SpikeCount = 1
            
        elif len(traces_results[0]['AP_begin_voltage']) > len(traces_results[0]['min_AHP_values']):
            traces_results[0]['AP_begin_voltage'] = np.delete(traces_results[0]['AP_begin_voltage'],-1)
            traces_results[0]['AP_begin_indices'] = np.delete(traces_results[0]['AP_begin_indices'],-1)
            
            
    #Calculate AHP amplitude values
    trace_results['AHP'] = traces_results[0]['min_AHP_values'] - traces_results[0]['AP_begin_voltage']
    
    #Calculate Duration of Spiking
    trace_results['SpikeDur'] = Time[traces_results[0]['AP_begin_indices'][-1]] - Time[traces_results[0]['AP_begin_indices'][0]]
                
    #Calculate Frequency Parameters (Mean Instantaneous, Max, and Frequency Adaptation)
    Frequency = 1/trace_results['ISI_values']
    trace_results['MeanInstFreq'] = np.mean(Frequency)
    trace_results['MaxFreq'] = max(Frequency)
    trace_results['FreqAdapt'] = Frequency[-1] / Frequency[0]
    
    #Calculate AP parameters when Spikecount differs from AP_begin_voltage
    if SpikeCount == 1:
        traces_results[0]['AP_Amplitude'] = traces_results[0]['peak_voltage'] - traces_results[0]['AP_begin_voltage']
        trace_results['MeanAPAmp'] = np.mean(traces_results[0]['AP_Amplitude'])
        trace_results['PeakAdapt'] = traces_results[0]['AP_Amplitude'][-1] / traces_results[0]['AP_Amplitude'][0]
        
    #Calculate AP parameters when Spikecount is similar to AP_begin_voltage
    if SpikeCount == 0:
        trace_results['MeanAPAmp'] = np.mean(traces_results[0]['AP_amplitude'])
        trace_results['PeakAdapt'] = traces_results[0]['AP_amplitude'][-1] / traces_results[0]['AP_amplitude'][0]
    
    #Calculate AHP Parameters (mean AHP Amplitude and AHP Peak Adaptation)
    trace_results['MeanAHPAmp'] = np.mean(trace_results['AHP'])
    trace_results['AHPAdapt'] = trace_results['AHP'][-1] / trace_results['AHP'][0]
    
    #Calculate Threshold AP Parameters if the trace contains more than one spike
    if IterVar == StartingColumn and SpikeCount == 1:
        AP_Latency = Time[traces_results[0]['AP_begin_indices'][0]] - 256.3
        Threshold_AP = {'AP_Latency': AP_Latency, 'AP_Threshold': traces_results[0]['AP_begin_voltage'][0],
                        'AP_Amplitude': traces_results[0]['AP_Amplitude'][0],'AP_Rise': 
                        traces_results[0]['AP_rise_time'][0],'AP_Half-Height_Width':traces_results[0]['spike_width2'][0],
                        'AHP_Amplitude': trace_results['AHP'][0]}
            
    if IterVar == StartingColumn and SpikeCount == 0:
        AP_Latency = Time[traces_results[0]['AP_begin_indices'][0]] - 256.3
        Threshold_AP = {'AP_Latency': AP_Latency, 'AP_Threshold': traces_results[0]['AP_begin_voltage'][0],
                        'AP_Amplitude': traces_results[0]['AP_amplitude'][0],'AP_Rise': 
                        traces_results[0]['AP_rise_time'][0],'AP_Half-Height_Width':traces_results[0]['spike_width2'][0],
                        'AHP_Amplitude': trace_results['AHP'][0]}
            
    #Insert all pertinent average data for each trace into a dictionary
    averages = {'AP #': int(traces_results[0]['Spikecount']), 'Duration_of_Spiking': trace_results['SpikeDur'],
            'Mean_Instantaneous_Frequency':trace_results['MeanInstFreq'],'Max_Frequency': trace_results['MaxFreq'],
            'Frequency_Adaptation': trace_results['FreqAdapt'], 'Mean_AP_Amplitude': trace_results['MeanAPAmp'],
            'Peak_Adaptation': trace_results['PeakAdapt'], 'Mean_AHP_Amplitude': trace_results['MeanAHPAmp'],
            'AHP_Adaptation': trace_results['AHPAdapt']}
    
    AllAverages.append(averages)
    
    IterVar += 1
    
#Two CSV output files for averaged trace data and Threshold_AP data
with open(str(file) + '_ThresholdAP' + '.csv','w') as tAP, open(str(file) + '_Averages' + '.csv','w') as Avg:
    writer1 = DictWriter(tAP,('AP_Latency','AP_Threshold','AP_Amplitude','AP_Rise','AP_Half-Height_Width','AHP_Amplitude'))
    writer1.writeheader()
    writer1.writerow(Threshold_AP)
    writer2 = DictWriter(Avg,('AP #','Duration_of_Spiking','Mean_Instantaneous_Frequency','Max_Frequency',
                                 'Frequency_Adaptation','Mean_AP_Amplitude','Peak_Adaptation','Mean_AHP_Amplitude',
                                 'AHP_Adaptation'))
    writer2.writeheader()
    writer2.writerows(AllAverages)
tAP.close()
Avg.close()

print('Success! Outputs saved as CSVs' + '\n')
    