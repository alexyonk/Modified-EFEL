#                    EFEL for ABF Formatted Files
#                   *Created by AY on 12/28/2020*
#                   *Last Updated on 7/28/2021*
#     *For any issues or bugs, please contact alex.yonk2@gmail.com*


#The following libraries must be installed before being imported!
import efel
import numpy as np
import pyabf
from matplotlib import pyplot as plt
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
efel.setIntSetting('strict_stiminterval',True)
efel.setDoubleSetting('rise_start_perc',0.1)
efel.setDoubleSetting('rise_end_perc',0.9)

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
First_Threshold_AP = list()
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
        print('No spikes in trace ' + str(IterVar) + '.')
        IterVar += 1
        continue
    
    #If Spikecount equals one, calculate Threshold_AP parameters, append "1" to AllAverages, and continue
    if traces_results[0]['Spikecount'] == 1:
        traces_results = efel.getFeatureValues(traces,['Spikecount','AP_rise_time','min_AHP_values','AP_begin_voltage','AP_amplitude',
                                                       'AP_begin_indices','spike_half_width'])
        AP_Latency = Time[traces_results[0]['AP_begin_indices'][0]] - 256.3
        trace_results['AHP'] = traces_results[0]['min_AHP_values'] - traces_results[0]['AP_begin_voltage']
        First_AP = {'AP_Latency': AP_Latency, 'AP_Threshold': traces_results[0]['AP_begin_voltage'][0],
                        'AP_Amplitude': traces_results[0]['AP_amplitude'][0],'AP_Rise': 
                        traces_results[0]['AP_rise_time'][0],'AP_Half-Height_Width': float(traces_results[0]['spike_half_width']),
                        'AHP_Amplitude': trace_results['AHP'][0]}
        First_Threshold_AP.append(First_AP)
        IterVar += 1
        continue
    
    #If the one spike error WILL NOT occur, the code continues as normal
    traces_results = efel.getFeatureValues(traces,[
                                            'AP_begin_voltage','voltage_base','AP_amplitude','AP_rise_time',
                                            'Spikecount','min_AHP_values','AP_begin_indices','peak_time',
                                            'spike_width2','peak_voltage','peak_indices','AP_rise_time'])
        
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
    
    #Further error occurs if the spikecount doesn't mean the AP_begin_voltages
    if len(traces_results[0]['Spikecount']) != len(traces_results[0]['AP_begin_voltage']):
        Diff2 = int(traces_results[0]['Spikecount']) - len(traces_results[0]['AP_begin_voltage'])
        traces_results[0]['peak_voltage'] = traces_results[0]['peak_voltage'][0:traces_results[0]['peak_voltage'].size-Diff2]
        traces_results[0]['peak_time'] = traces_results[0]['peak_time'][0:traces_results[0]['peak_time'].size-Diff2]
            
    #Save First Threshold AP parameters
    AP_Latency = Time[traces_results[0]['AP_begin_indices'][0]] - 256.3
    trace_results['AHP'] = traces_results[0]['min_AHP_values'] - traces_results[0]['AP_begin_voltage']
    AP_Rise = (traces_results[0]['peak_indices'][0] - traces_results[0]['AP_begin_indices'][0]) * Time[1]
    AP_Amp = traces_results[0]['peak_voltage'] - traces_results[0]['AP_begin_voltage']
    First_AP = {'AP_Latency': AP_Latency, 'AP_Threshold': traces_results[0]['AP_begin_voltage'][0],
                          'AP_Amplitude': AP_Amp[0],'AP_Rise': AP_Rise,
                            'AP_Half-Height_Width': float(traces_results[0]['spike_width2'][0]),
                            'AHP_Amplitude': trace_results['AHP'][0]}

    #Calculate ISI values based on AP_begin_indices and multiply each value by the sampling point (0.05ms)
    if traces_results[0]['Spikecount'] == 2:
        traces_results[0]['ISI_values'] = float(traces_results[0]['AP_begin_indices'][-1] - traces_results[0]['AP_begin_indices'][0]) * 0.05
    elif traces_results[0]['Spikecount'] > 2:    
        traces_results[0]['ISI_values'] = np.diff(traces_results[0]['AP_begin_indices']) * 0.05
            
    #Calculate AHP amplitude values
    trace_results['AHP'] = traces_results[0]['min_AHP_values'] - traces_results[0]['AP_begin_voltage']
    
    #Calculate Duration of Spiking
    if traces_results[0]['AP_begin_indices'][-1] > 25126:
        Begin_indices_clip = traces_results[0]['AP_begin_indices'][0:int(traces_results[0]['Spikecount'])-1]
    else:
        Begin_indices_clip = traces_results[0]['AP_begin_indices'][0:int(traces_results[0]['Spikecount'])]
    trace_results['SpikeDur'] = Time[Begin_indices_clip[-1]] - Time[Begin_indices_clip[0]]
            
    #Calculate Frequency Parameters (Mean Instantaneous, Max, and Frequency Adaptation)
    #If there is only one frequency value, calculate MaxFreq and FreqAdapt is not applicable
    #If there is more than one frequency value, calculate both parameters appropriately
    #ISI values are calculated from AP_begin_indices(i+1) - AP_begin_indices(i) as opposed to the peaks
    Frequency = 1/traces_results[0]['ISI_values']
    trace_results['MeanInstFreq'] = np.mean(Frequency)*1000
    if np.size(traces_results[0]['ISI_values']) == 1:   
        trace_results['MaxFreq'] = Frequency * 1000
        trace_results['FreqAdapt'] = 'N/A'
    elif np.size(traces_results[0]['ISI_values']) > 1:
        trace_results['MaxFreq'] = max(Frequency) * 1000
        trace_results['FreqAdapt'] = (Frequency[-1] / Frequency[0])
    #Calculate Threshold Adaptation Frequency
    trace_results['Thresh_Adapt_Freq'] = traces_results[0]['AP_begin_voltage'][-1] / traces_results[0]['AP_begin_voltage'][0]
    
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
                        'AP_Amplitude': traces_results[0]['AP_Amplitude'][0],'AP_Rise': traces_results[0]['AP_rise_time'][0],
                        'AP_Half-Height_Width':traces_results[0]['spike_width2'][0],
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
            'AHP_Adaptation': trace_results['AHPAdapt'], 'Thresh_Adapt_Freq': trace_results['Thresh_Adapt_Freq']}
    
    #Graph to plot related information
    #Added section that plots red plus signs above denoted APs
    peak_time = traces_results[0]['peak_time'][0:len(traces_results[0]['peak_voltage'])]
    plt.plot(Time,SortedData[:,IterVar])
    plt.scatter(peak_time,traces_results[0]['peak_voltage'] + 20,c='r',marker = '+')
    plt.show()

    #Append all pertinent information into a list to be written into a CSV
    First_Threshold_AP.append(First_AP)
    AllAverages.append(averages)
    
    IterVar += 1
    
#Two CSV output files for averaged trace data and First_Threshold_AP data
with open(str(file) + '_FirstAP' + '.csv','w') as tAP, open(str(file) + '_Averages' + '.csv','w') as Avg:
    writer1 = DictWriter(tAP,('AP_Latency','AP_Threshold','AP_Amplitude','AP_Rise','AP_Half-Height_Width','AHP_Amplitude'))
    writer1.writeheader()
    writer1.writerows(First_Threshold_AP)
    writer2 = DictWriter(Avg,('AP #','Duration_of_Spiking','Mean_Instantaneous_Frequency','Max_Frequency',
                                 'Frequency_Adaptation','Mean_AP_Amplitude','Peak_Adaptation','Mean_AHP_Amplitude',
                                 'AHP_Adaptation','Thresh_Adapt_Freq'))
    writer2.writeheader()
    writer2.writerows(AllAverages)
tAP.close()
Avg.close()

print('Success! Outputs saved as CSVs' + '\n')