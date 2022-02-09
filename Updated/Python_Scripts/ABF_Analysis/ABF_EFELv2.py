#                    EFEL for ABF Formatted Files
#                   *Created by AY on 12/28/2020*
#                   *Last Updated on 02/09/2022*
#     *For any issues or bugs, please contact alex.yonk2@gmail.com*


#The following libraries must be installed before being imported!
import efel
import numpy as np
import pyabf
from matplotlib import pyplot as plt
from csv import DictWriter
from tkinter import filedialog
from os import chdir, getcwd

#Allows user to set working directory
WorkDir = int(input('Would you like to change the working directory? (Input 0): '))
if WorkDir == 0:
    wd = filedialog.askdirectory()
    chdir(wd)

#Opens a dialog box allowing the user to select the file and removes the extension from the file name
file_path = filedialog.askopenfilename()
file = file_path[:-4]

#Sets settings for derivative threshold, interpolation step, and calculation of RMP
efel.setDoubleSetting('interp_step',0.05) #Must be set to the sampling rate (20,000 Hz = 0.05)
efel.setDoubleSetting('voltage_base_start_perc',0.1) #Used for RMP calculation
efel.setDoubleSetting('voltage_base_end_perc',0.8) #Used for RMP calculation
efel.setDerivativeThreshold(15) #Normally set to 15
#efel.setIntSetting('strict_stiminterval',True)
efel.setDoubleSetting('rise_start_perc',0.1)
efel.setDoubleSetting('rise_end_perc',0.9)
#efel.setThreshold(0)

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
    
    #If Spikecount is one, calculate Threshold_AP parameters, append info into First_AP dictionary, and continue
    if traces_results[0]['Spikecount'] == 1:
        traces_results = efel.getFeatureValues(traces,['Spikecount','AP_rise_time','min_AHP_values','AP_begin_voltage','AP_amplitude',
                                                       'AP_begin_indices','spike_half_width','AP_rise_time'])
        
        AP_Latency = Time[traces_results[0]['AP_begin_indices'][0]] - 256.3
        traces_results['AHP'] = traces_results[0]['min_AHP_values'][0] - traces_results[0]['AP_begin_voltage'][0]
        First_AP = {'AP_Latency': AP_Latency, 'AP_Threshold': traces_results[0]['AP_begin_voltage'][0],
                        'AP_Amplitude': traces_results[0]['AP_amplitude'][0],'AP_Rise': traces_results[0]['AP_rise_time'][0],
                        'AP_Half-Height_Width': float(traces_results[0]['spike_half_width']),'AHP_Amplitude': trace_results['AHP'][0]}
        First_Threshold_AP.append(First_AP)
        IterVar += 1
        continue
    
    #If the one spike error WILL NOT occur, the code continues as normal
    traces_results = efel.getFeatureValues(traces,[
                                            'AP_begin_voltage','voltage_base','Spikecount','min_AHP_values',
                                            'AP_begin_indices','spike_half_width','peak_voltage','min_AHP_indices',
                                            'peak_indices'])

    #An error occurs when the number of peak_indices does not equal the number of AP begin indices
    #To correct for erroneous values, a while loop circles through and removes inappropriate values
    #until the number of peak_indices and AP_begin indices are equal
    #Inappropriate values are selected by calculating the difference between AP_begin_indices and peak_indices
    #Only one peak corresponds to one AP threshold (Thus, if the difference is very negative, a second peak was
    #calculated in between AP threshold 1 and AP threshold 2)
    while len(traces_results[0]['AP_begin_indices']) != len(traces_results[0]['peak_indices']):
        oper_ind_list = [traces_results[0]['AP_begin_indices'],traces_results[0]['peak_indices']]
        operdifflist = np.empty((max(y.shape[0] for y in oper_ind_list), len(oper_ind_list)))
        operdifflist[:] = np.nan
        for i,y in enumerate(oper_ind_list):
            operdifflist[0:len(y), i] = y.T
        oper_diff = np.diff(operdifflist)
        oper_del = np.where(oper_diff < 0)
            
        #Conditional if statement to catch when the difference is 0, but the parameters are not equal
        #Usually means that there is an extra value (NaN) at the end
        if len(oper_del[0]) == 0:
            oper_del = np.argwhere(np.isnan(oper_diff))
            
        #Deletes the value corresponding to inappropriate values from specified parameters
        traces_results[0]['peak_indices'] = np.delete(traces_results[0]['peak_indices'], oper_del[0][0])
        traces_results[0]['peak_voltage'] = np.delete(traces_results[0]['peak_voltage'], oper_del[0][0])    
        traces_results[0]['Spikecount'] = traces_results[0]['Spikecount'] - 1

        #When the size of AP_begin_indices equals the size of peak_indices, the while loop breaks
        if len(traces_results[0]['AP_begin_indices']) == len(traces_results[0]['peak_indices']):
            break

    #A potential error occurs when a spike occurs at the end of the stimulation window without a clear min_AHP_index.
    #To correct for this, if the size of AP_begin_indices is larger than min_AHP_indices (by 1), it will remove the 
    #last AP_begin_voltage, AP_begin_indices,  Spikecount, peak_voltage, and peak_indices
    if len(traces_results[0]['min_AHP_indices']) < len(traces_results[0]['AP_begin_indices']):
        traces_results[0]['AP_begin_indices'] = np.delete(traces_results[0]['AP_begin_indices'], -1)
        traces_results[0]['AP_begin_voltage'] = np.delete(traces_results[0]['AP_begin_voltage'], -1)
        traces_results[0]['Spikecount'] = traces_results[0]['Spikecount'] - 1
        traces_results[0]['peak_voltage'] = np.delete(traces_results[0]['peak_voltage'], -1)
        traces_results[0]['peak_indices'] = np.delete(traces_results[0]['peak_indices'], -1)

    #An error occurs when the number of AHP indices does not equal the number of AP begin indices
    #To correct for erroneous values, a while loop circles through and removes inappropriate values
    #until the number of AHP and AP_begin indices are equal
    while len(traces_results[0]['AP_begin_indices']) != len(traces_results[0]['min_AHP_indices']):
        oper_ind_list2 = [traces_results[0]['AP_begin_indices'],traces_results[0]['min_AHP_indices']]
        operdifflist2 = np.empty((max(z.shape[0] for z in oper_ind_list2), len(oper_ind_list2)))
        operdifflist2[:] = np.nan
        for i,z in enumerate(oper_ind_list2):
            operdifflist2[0:len(z), i] = z.T
        oper_diff2 = np.diff(operdifflist2)
        oper_del2 = np.where(oper_diff2 < 0)
          
        #Conditional If statement to catch when the difference is 0, but the parameter length is not equal
        #Usually means that there is an extra value (read NaN) at the end
        if len(oper_del2[0]) == 0:
            oper_del2 = np.argwhere(np.isnan(oper_diff2))
            
        #Deletes the value corresponding to inappropriate values from specified parameters
        traces_results[0]['min_AHP_indices'] = np.delete(traces_results[0]['min_AHP_indices'], oper_del2[0][0])
        traces_results[0]['min_AHP_values'] = np.delete(traces_results[0]['min_AHP_values'], oper_del2[0][0])
            
        #When the number of AHP and AP_begin indices are equal, the while loop terminates
        if len(traces_results[0]['AP_begin_indices']) == len(traces_results[0]['min_AHP_indices']):
            break

    #If a trace contains multiple spikes and only a few spikes are picked up, more spike_half_width values are calculated
    #A while loop runs when the size of spike_half_width is not equal to AP_begin_indices
    #This loop removes the last value of spike_half_width until the sizes are equal to each other
    while len(traces_results[0]['spike_half_width']) != len(traces_results[0]['AP_begin_indices']):
        traces_results[0]['spike_half_width'] = np.delete(traces_results[0]['spike_half_width'], -1)
        if len(traces_results[0]['spike_half_width']) == len(traces_results[0]['AP_begin_indices']):
            break
        
    #Calculate ISI values based on AP_begin_indices and multiply each value by the sampling point value (0.05ms)
    #Note= This size of this parameter should be one less than the spikecount
    traces_results[0]['ISI_values'] = np.diff(traces_results[0]['AP_begin_indices']) * 0.05
        
    #Calculate AP amplitude by subtracting peak voltage from AP threshold values
    traces_results[0]['AP_Amp'] = traces_results[0]['peak_voltage'] - traces_results[0]['AP_begin_voltage']
    
    #Calculate AHP values by subtracting the minimum AHP values from the AP threshold values
    #Also, calculates the AHP adaptation by dividing the last value by the first value
    traces_results[0]['AHP'] = traces_results[0]['min_AHP_values'] - traces_results[0]['AP_begin_voltage']
    traces_results[0]['AHPAdapt'] = traces_results[0]['AHP'][-1] / traces_results[0]['AHP'][0]

    #Calculate Duration of Spiking
    if traces_results[0]['AP_begin_indices'][-1] > 25126:
        Begin_indices_clip = traces_results[0]['AP_begin_indices'][0:int(traces_results[0]['Spikecount'])-1]
    else:
        Begin_indices_clip = traces_results[0]['AP_begin_indices'][0:int(traces_results[0]['Spikecount'])]
        traces_results[0]['SpikeDur'] = Time[Begin_indices_clip[-1]] - Time[Begin_indices_clip[0]]
        
    #Calculate frequency and adaptation parameters
    Frequency = 1 / traces_results[0]['ISI_values']
    traces_results[0]['MeanInstFreq'] = np.mean(Frequency) * 1000
    traces_results[0]['MaxFreq'] = np.max(Frequency) * 1000
    traces_results[0]['FreqAdapt'] = (Frequency[-1] / Frequency[0])
    traces_results[0]['PeakAdapt'] = traces_results[0]['AP_Amp'][-1] / traces_results[0]['AP_Amp'][0]            
    traces_results[0]['Thresh_Adapt_Freq'] = traces_results[0]['AP_begin_voltage'][-1] / traces_results[0]['AP_begin_voltage'][0]

    #Save First Threshold AP parameters
    AP_Latency = Time[traces_results[0]['AP_begin_indices'][0]] - 256.3
    AP_Rise = (traces_results[0]['peak_indices'][0] - traces_results[0]['AP_begin_indices'][0]) * 0.05
    First_AP = {'AP_Latency': AP_Latency, 'AP_Threshold': traces_results[0]['AP_begin_voltage'][0],
                          'AP_Amplitude': traces_results[0]['AP_Amp'][0],'AP_Rise': AP_Rise,
                          'AP_Half-Height_Width': float(traces_results[0]['spike_half_width'][0]),
                          'AHP_Amplitude': traces_results[0]['AHP'][0]}
    
    #Insert all pertinent average data for each trace into a dictionary
    averages = {'AP #': int(traces_results[0]['Spikecount']), 'Duration_of_Spiking': traces_results[0]['SpikeDur'],
            'Mean_Instantaneous_Frequency':traces_results[0]['MeanInstFreq'],'Max_Frequency': traces_results[0]['MaxFreq'],
            'Frequency_Adaptation': traces_results[0]['FreqAdapt'], 'Mean_AP_Amplitude': np.mean(traces_results[0]['AP_Amp']),
            'Peak_Adaptation': traces_results[0]['PeakAdapt'], 'Mean_AHP_Amplitude': np.mean(traces_results[0]['AHP']),
            'AHP_Adaptation': traces_results[0]['AHPAdapt'], 'Thresh_Adapt_Freq': traces_results[0]['Thresh_Adapt_Freq'],
            'Mean_Spike_half_width': np.mean(traces_results[0]['spike_half_width'])}
    
    #Graph to plot related information
    #Added section that plots red plus signs above denoted APs
    peak_indices = traces_results[0]['peak_indices'][0:len(traces_results[0]['peak_voltage'])] * 0.05
    plt.plot(Time,SortedData[:,IterVar])
    plt.scatter(peak_indices,traces_results[0]['peak_voltage'] + 20,c='r',marker = '+')
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
                                 'AHP_Adaptation','Thresh_Adapt_Freq','Mean_Spike_half_width'))
    writer2.writeheader()
    writer2.writerows(AllAverages)
tAP.close()
Avg.close()

print('Success! Outputs saved as CSVs' + '\n')