#                   EFEL for HEKA DAT Files v2.0
#                   *Created by AY on 1/31/2021*
#                   *Last Updated on 4/13/2021*
#     *For any issues or bugs, please contact alex.yonk2@gmail.com*
#*This script was designed to analyze electrophysiological parameters from HEKA .dat files converted into mat files
#*Files can be analyzed as single traces w/ graphs or an experiment as a whole
#*It should be used in conjunction with the HEKAv2 MATLAB script

#Install and Import these scripts
import scipy.io
import efel
import numpy as np
from tkinter import filedialog
from matplotlib import pyplot as plt

#Enable EFEL Settings
efel.setDoubleSetting('interp_step',0.05) #Must be set to the sampling rate (20,000 Hz = 0.05)
efel.setDoubleSetting('voltage_base_start_perc',0.1)
efel.setDoubleSetting('voltage_base_end_perc',0.8)
efel.setDerivativeThreshold(10) #Value can be changed, but normally set to 10
efel.setThreshold(0)

#Create global variable
trace_results = dict()

#Opens a dialog box allowing the user to select the file and removes the extension from the file name & load in the file
file_path = filedialog.askopenfilename()
file = file_path[:-4]
mat = scipy.io.loadmat(file_path)

#Depending upon the number of cells present, split the data into a list of numpy arrays based on the number of experiments
print('There are ' + str(int(mat['CellNum'])) + ' cells in this file.')

if mat['CellNum'] == 1:
    Cell1 = list(np.hsplit(mat['C1data'],int(mat['C1Expts'])))
    print('Cell #1 has ' + str(int(mat['C1Expts'])) + ' experiments.')
if mat['CellNum'] == 2:
    Cell1 = list(np.hsplit(mat['C1data'],int(mat['C1Expts'])))
    Cell2 = list(np.hsplit(mat['C2data'],int(mat['C2Expts'])))
    print('Cell #1 has ' + str(int(mat['C1Expts'])) + ' experiments.')
    print('Cell #2 has ' + str(int(mat['C2Expts'])) + ' experiments.')
if mat['CellNum'] == 3:
    Cell1 = list(np.hsplit(mat['C1data'],int(mat['C1Expts'])))
    Cell2 = list(np.hsplit(mat['C2data'],int(mat['C2Expts'])))
    Cell3 = list(np.hsplit(mat['C3data'],int(mat['C3Expts'])))
    print('Cell #1 has ' + str(int(mat['C1Expts'])) + ' experiments.')
    print('Cell #2 has ' + str(int(mat['C2Expts'])) + ' experiments.')
    print('Cell #3 has ' + str(int(mat['C3Expts'])) + ' experiments.')    
if mat['CellNum'] == 4:
    Cell1 = list(np.hsplit(mat['C1data'],int(mat['C1Expts'])))
    Cell2 = list(np.hsplit(mat['C2data'],int(mat['C2Expts'])))
    Cell3 = list(np.hsplit(mat['C3data'],int(mat['C3Expts'])))
    Cell4 = list(np.hsplit(mat['C4data'],int(mat['C4Expts'])))
    print('Cell #1 has ' + str(int(mat['C1Expts'])) + ' experiments.')
    print('Cell #2 has ' + str(int(mat['C2Expts'])) + ' experiments.')
    print('Cell #3 has ' + str(int(mat['C3Expts'])) + ' experiments.')
    print('Cell #4 has ' + str(int(mat['C4Expts'])) + ' experiments.')
    
#Allows user input for what cell to analyze, what experiment to analyze, and what trace(s) to analyze
CellVal = int(input(' Which cell would youl like to analyze? :'))
ExptVal = int(input('Which experiment would you like to analyze? (Input starts at 0) :'))
TraceVal = int(input('Which trace would you like to analyze? (Input the number of the trace "0-10" or input "12" for all traces) :')) 

#Analysis for Cell 1
if CellVal == 1:
    #Analyze a single trace in Cell 1
    if TraceVal <= 11:    
        SingleC1Trace = list()
        for i in Cell1[ExptVal][TraceVal]:
            trace1 = {}
            trace1['T'] = mat['Time'][:]
            trace1['V'] = Cell1[ExptVal][:,TraceVal]
            trace1['stim_start'] = [201]
            trace1['stim_end'] = [700]
            traces = [trace1]
            traces_results = efel.getFeatureValues(traces,['Spikecount'])
            
            #If a Spikecount of 0 is detected, print message and end loop
            if traces_results[0]['Spikecount'] == 0:
                print('There are no spikes in this trace')
                break
            
            #If a Spikecount of 1 is detected, record threshold AP parameters and end loop
            if traces_results[0]['Spikecount'] == 1:
                traces_results = efel.getFeatureValues(traces,['Spikecount','AP_rise_time','min_AHP_values','AP_begin_voltage',
                                                       'AP_amplitude','AP_begin_indices','spike_half_width'])
                AP_Latency = mat['Time'][[traces_results[0]['AP_begin_indices'][0]]] - 201
                trace_results['AHP'] = traces_results[0]['min_AHP_values'] - traces_results[0]['AP_begin_voltage']
                Threshold_AP = {'AP_Latency': AP_Latency, 'AP_Threshold': traces_results[0]['AP_begin_voltage'][0],
                            'AP_Amplitude': traces_results[0]['AP_amplitude'][0], 'AP_Rise': traces_results[0]['AP_rise_time'][0],
                            'AP_Half-Height_Width': float(traces_results[0]['spike_half_width']),
                            'AHP_Amplitude': trace_results['AHP'][0]}
                
                SingleC1Trace.append(Threshold_AP)
                
                plt.plot(mat['Time'],Cell1[ExptVal][:,TraceVal])
                plt.xlabel('Time (in ms)')
                plt.ylabel('Voltage (in mV)')
                plt.show()
            
                print('Trace ' + str(TraceVal) + ' of Cell ' + str(CellVal) + ' analyzed successfully!')
                break
            
            #If Spikecount is greater than 1, the code continues as normal
            traces_results = efel.getFeatureValues(traces,[
                                            'AP_begin_voltage','voltage_base','AP_amplitude','AP_rise_time',
                                            'Spikecount','min_AHP_values','AP_begin_indices','peak_time',
                                            'ISI_values','spike_width2'])
            
            #Calculate initial ISI value and insert this value into the 0 position of ISI values
            FirstISI = traces_results[0]['peak_time'][1] - traces_results[0]['peak_time'][0]
            trace_results['ISI_values'] = np.insert(traces_results[0]['ISI_values'],0,FirstISI)
    
            #Another error comes about if more AHP or threshold AP values are detected
            #This code automatically removes the problematic errors and makes the number of values equal for further calculations
            if len(traces_results[0]['min_AHP_values']) != len(traces_results[0]['AP_begin_voltage']):
                if len(traces_results[0]['min_AHP_values']) > len(traces_results[0]['AP_begin_voltage']):
                    traces_results[0]['min_AHP_values'] = np.delete(traces_results[0]['min_AHP_values'],-1)
                elif len(traces_results[0]['AP_begin_voltage']) > len(traces_results[0]['min_AHP_values']):
                    traces_results[0]['AP_begin_voltage'] = np.delete(traces_results[0]['AP_begin_voltage'],-1)
                    traces_results[0]['AP_begin_indices'] = np.delete(traces_results[0]['AP_begin_indices'],-1)

            plt.plot(mat['Time'],Cell1[ExptVal][:,TraceVal])
            plt.xlabel('Time (in ms)')
            plt.ylabel('Voltage (in mV)')
            plt.show()
        
            #Calculate AHP amplitude values
            trace_results['AHP'] = traces_results[0]['min_AHP_values'] - traces_results[0]['AP_begin_voltage']
    
            #Calculate Duration of Spiking
            trace_results['SpikeDur'] = mat['Time'][[traces_results[0]['AP_begin_indices'][-1]]] - mat['Time'][[traces_results[0]['AP_begin_indices'][0]]]
                
            #Calculate Frequency Parameters (Mean Instantaneous, Max, and Frequency Adaptation)
            Frequency = 1/trace_results['ISI_values']
            trace_results['MeanInstFreq'] = np.mean(Frequency)
            trace_results['MaxFreq'] = max(Frequency)
            trace_results['FreqAdapt'] = trace_results['ISI_values'][-1] / trace_results['ISI_values'][0]
    
            #Calculate AP Parameters (mean AP Amplitude and Peak Adaptation)
            trace_results['MeanAPAmp'] = np.mean(traces_results[0]['AP_amplitude'])
            trace_results['PeakAdapt'] = traces_results[0]['AP_amplitude'][-1] / traces_results[0]['AP_amplitude'][0]
    
            #Calculate AHP Parameters (mean AHP Amplitude and AHP Peak Adaptation)
            trace_results['MeanAHPAmp'] = np.mean(trace_results['AHP'])
            trace_results['AHPAdapt'] = trace_results['AHP'][-1] / trace_results['AHP'][0]
            
            #Insert all pertinent average data for each trace into a dictionary
            averages = {'AP #': int(traces_results[0]['Spikecount']), 'Duration_of_Spiking': trace_results['SpikeDur'],
            'Mean_Instantaneous_Frequency':trace_results['MeanInstFreq'],'Max_Frequency': trace_results['MaxFreq'],
            'Frequency_Adaptation': trace_results['FreqAdapt'], 'Mean_AP_Amplitude': trace_results['MeanAPAmp'],
            'Peak_Adaptation': trace_results['PeakAdapt'], 'Mean_AHP_Amplitude': trace_results['MeanAHPAmp'],
            'AHP_Adaptation': trace_results['AHPAdapt']}
            
            SingleC1Trace.append(averages)
            
            print('Trace ' + str(TraceVal) + ' of Cell ' + str(CellVal) + ' analyzed successfully!')
            
            break
        
    #Analyze all traces within an experiment
    if TraceVal == 12:
        x = 0
        AllC1Traces = list()
        for i in Cell1[ExptVal][x:11:1]:
            trace1 = {}
            trace1['T'] = mat['Time'][:]
            trace1['V'] = Cell1[ExptVal][:,x]
            trace1['stim_start'] = [201]
            trace1['stim_end'] = [700]
            traces = [trace1]
            traces_results = efel.getFeatureValues(traces,['Spikecount'])
        
            #If a Spikecount of 0 is detected, print message and end loop
            if traces_results[0]['Spikecount'] == 0:
                AllC1Traces.append(0)
                x += 1
                continue
            
            #If a Spikecount of 1 is detected, record threshold AP parameters and end loop
            if traces_results[0]['Spikecount'] == 1:
                traces_results = efel.getFeatureValues(traces,['Spikecount','AP_rise_time','min_AHP_values','AP_begin_voltage',
                                                       'AP_amplitude','AP_begin_indices','spike_half_width'])
                AP_Latency = mat['Time'][[traces_results[0]['AP_begin_indices'][0]]] - 201
                trace_results['AHP'] = traces_results[0]['min_AHP_values'] - traces_results[0]['AP_begin_voltage']
                Threshold_AP = {'AP_Latency': AP_Latency, 'AP_Threshold': traces_results[0]['AP_begin_voltage'][0],
                            'AP_Amplitude': traces_results[0]['AP_amplitude'][0], 'AP_Rise': traces_results[0]['AP_rise_time'][0],
                            'AP_Half-Height_Width': float(traces_results[0]['spike_half_width']),
                            'AHP_Amplitude': trace_results['AHP'][0]}
                
                AllC1Traces.append(Threshold_AP)
                x += 1
                continue
        
            #If Spikecount is greater than 1, the code continues as normal
            traces_results = efel.getFeatureValues(traces,[
                                            'AP_begin_voltage','voltage_base','AP_amplitude','AP_rise_time',
                                            'Spikecount','min_AHP_values','AP_begin_indices','peak_time',
                                            'ISI_values','spike_width2'])
    
            #Algorithm cannot run if no ISI values are detected (Replaces NoneType with an array containing a 0 that will be replaced)
            if traces_results[0]['Spikecount'] == 2:
                traces_results[0]['ISI_values'] = np.array(0)
            
            #Calculate initial ISI value and insert this value into the 0 position of ISI values
            FirstISI = traces_results[0]['peak_time'][1] - traces_results[0]['peak_time'][0]
            trace_results['ISI_values'] = np.insert(traces_results[0]['ISI_values'],0,FirstISI)

            #Calculate AHP amplitude values
            trace_results['AHP'] = traces_results[0]['min_AHP_values'] - traces_results[0]['AP_begin_voltage']
        
            #Calculate Duration of Spiking
            trace_results['SpikeDur'] = mat['Time'][[traces_results[0]['AP_begin_indices'][-1]]] - mat['Time'][[traces_results[0]['AP_begin_indices'][0]]]
                
            #Calculate Frequency Parameters (Mean Instantaneous, Max, and Frequency Adaptation)
            Frequency = 1/trace_results['ISI_values']
            trace_results['MeanInstFreq'] = np.mean(Frequency)
            trace_results['MaxFreq'] = max(Frequency)
            trace_results['FreqAdapt'] = trace_results['ISI_values'][-1] / trace_results['ISI_values'][0]
    
            #Calculate AP Parameters (mean AP Amplitude and Peak Adaptation)
            trace_results['MeanAPAmp'] = np.mean(traces_results[0]['AP_amplitude'])
            trace_results['PeakAdapt'] = traces_results[0]['AP_amplitude'][-1] / traces_results[0]['AP_amplitude'][0]
        
            #Calculate AHP Parameters (mean AHP Amplitude and AHP Peak Adaptation)
            trace_results['MeanAHPAmp'] = np.mean(trace_results['AHP'])
            trace_results['AHPAdapt'] = trace_results['AHP'][-1] / trace_results['AHP'][0]
        
            #Append all salient parameters for each trace
            averages = {'AP #': int(traces_results[0]['Spikecount']), 'Duration_of_Spiking': trace_results['SpikeDur'],
            'Mean_Instantaneous_Frequency':trace_results['MeanInstFreq'],'Max_Frequency': trace_results['MaxFreq'],
            'Frequency_Adaptation': trace_results['FreqAdapt'], 'Mean_AP_Amplitude': trace_results['MeanAPAmp'],
            'Peak_Adaptation': trace_results['PeakAdapt'], 'Mean_AHP_Amplitude': trace_results['MeanAHPAmp'],
            'AHP_Adaptation': trace_results['AHPAdapt']}
        
            AllC1Traces.append(averages)
        
            x += 1

            print('All traces analyzed successfully!')

#Analysis for Cell 2
if CellVal == 2:
    SingleC2Trace = list()
    #Analyze a single trace within an experiment
    if TraceVal <= 11:    
        for i in Cell2[ExptVal][TraceVal]:
            trace1 = {}
            trace1['T'] = mat['Time'][:]
            trace1['V'] = Cell2[ExptVal][:,TraceVal]
            trace1['stim_start'] = [201]
            trace1['stim_end'] = [700]
            traces = [trace1]
            traces_results = efel.getFeatureValues(traces,['Spikecount'])
            
            #If a Spikecount of 0 is detected, print message and end loop
            if traces_results[0]['Spikecount'] == 0:
                print('There are no spikes in this trace')
                break
            
            #If a Spikecount of 1 is detected, record threshold AP parameters and end loop
            if traces_results[0]['Spikecount'] == 1:
                traces_results = efel.getFeatureValues(traces,['Spikecount','AP_rise_time','min_AHP_values','AP_begin_voltage',
                                                       'AP_amplitude','AP_begin_indices','spike_half_width'])
                AP_Latency = mat['Time'][[traces_results[0]['AP_begin_indices'][0]]] - 201
                trace_results['AHP'] = traces_results[0]['min_AHP_values'] - traces_results[0]['AP_begin_voltage']
                Threshold_AP = {'AP_Latency': AP_Latency, 'AP_Threshold': traces_results[0]['AP_begin_voltage'][0],
                            'AP_Amplitude': traces_results[0]['AP_amplitude'][0], 'AP_Rise': traces_results[0]['AP_rise_time'][0],
                            'AP_Half-Height_Width': float(traces_results[0]['spike_half_width']),
                            'AHP_Amplitude': trace_results['AHP'][0]}
                
                SingleC2Trace.append(Threshold_AP)
                
                plt.plot(mat['Time'],Cell2[ExptVal][:,TraceVal])
                plt.xlabel('Time (in ms)')
                plt.ylabel('Voltage (in mV)')
                plt.show()
            
                print('Trace ' + str(TraceVal) + ' of Cell ' + str(CellVal) + ' analyzed successfully!')
                break
            
            #If Spikecount is greater than 1, the code continues as normal
            traces_results = efel.getFeatureValues(traces,[
                                            'AP_begin_voltage','voltage_base','AP_amplitude','AP_rise_time',
                                            'Spikecount','min_AHP_values','AP_begin_indices','peak_time',
                                            'ISI_values','spike_width2'])
            
            saved = plt.figure()
            plt.plot(mat['Time'],Cell2[ExptVal][:,TraceVal])
            plt.xlabel('Time (in ms)')
            plt.ylabel('Voltage (in mV)')
            plt.show()
            saved.savefig(str(CellVal) + '_' + str(ExptVal) + '_' + str(TraceVal) + '.eps', format = 'eps', dpi = 1200)

            #Calculate initial ISI value and insert this value into the 0 position of ISI values
            FirstISI = traces_results[0]['peak_time'][1] - traces_results[0]['peak_time'][0]
            trace_results['ISI_values'] = np.insert(traces_results[0]['ISI_values'],0,FirstISI)
    
            #Another error comes about if more AHP or threshold AP values are detected
            #This code automatically removes the problematic errors and makes the number of values equal for further calculations
            if len(traces_results[0]['min_AHP_values']) != len(traces_results[0]['AP_begin_voltage']):
                if len(traces_results[0]['min_AHP_values']) > len(traces_results[0]['AP_begin_voltage']):
                    traces_results[0]['min_AHP_values'] = np.delete(traces_results[0]['min_AHP_values'],-1)
                elif len(traces_results[0]['AP_begin_voltage']) > len(traces_results[0]['min_AHP_values']):
                    traces_results[0]['AP_begin_voltage'] = np.delete(traces_results[0]['AP_begin_voltage'],-1)
                    traces_results[0]['AP_begin_indices'] = np.delete(traces_results[0]['AP_begin_indices'],-1)
                    
            #Calculate AHP amplitude values
            trace_results['AHP'] = traces_results[0]['min_AHP_values'] - traces_results[0]['AP_begin_voltage']
    
            #Calculate Duration of Spiking
            trace_results['SpikeDur'] = mat['Time'][[traces_results[0]['AP_begin_indices'][-1]]] - mat['Time'][[traces_results[0]['AP_begin_indices'][0]]]
                
            #Calculate Frequency Parameters (Mean Instantaneous, Max, and Frequency Adaptation)
            Frequency = 1/trace_results['ISI_values']
            trace_results['MeanInstFreq'] = np.mean(Frequency)
            trace_results['MaxFreq'] = max(Frequency)
            trace_results['FreqAdapt'] = trace_results['ISI_values'][-1] / trace_results['ISI_values'][0]
    
            #Calculate AP Parameters (mean AP Amplitude and Peak Adaptation)
            trace_results['MeanAPAmp'] = np.mean(traces_results[0]['AP_amplitude'])
            trace_results['PeakAdapt'] = traces_results[0]['AP_amplitude'][-1] / traces_results[0]['AP_amplitude'][0]
    
            #Calculate AHP Parameters (mean AHP Amplitude and AHP Peak Adaptation)
            trace_results['MeanAHPAmp'] = np.mean(trace_results['AHP'])
            trace_results['AHPAdapt'] = trace_results['AHP'][-1] / trace_results['AHP'][0]
            
            #Insert all pertinent average data for each trace into a dictionary
            averages = {'AP #': int(traces_results[0]['Spikecount']), 'Duration_of_Spiking': trace_results['SpikeDur'],
            'Mean_Instantaneous_Frequency':trace_results['MeanInstFreq'],'Max_Frequency': trace_results['MaxFreq'],
            'Frequency_Adaptation': trace_results['FreqAdapt'], 'Mean_AP_Amplitude': trace_results['MeanAPAmp'],
            'Peak_Adaptation': trace_results['PeakAdapt'], 'Mean_AHP_Amplitude': trace_results['MeanAHPAmp'],
            'AHP_Adaptation': trace_results['AHPAdapt']}
            
            SingleC2Trace.append(averages)
            
            print('Trace ' + str(TraceVal) + ' of Cell ' + str(CellVal) + ' analyzed successfully!')
            
            
            break
            
#Analyze all traces within an experiment
    if TraceVal == 12:
        x = 0
        AllC2Traces = list()
        for i in Cell2[ExptVal][x:11:1]:
            trace1 = {}
            trace1['T'] = mat['Time'][:]
            trace1['V'] = Cell2[ExptVal][:,x]
            trace1['stim_start'] = [201]
            trace1['stim_end'] = [700]
            traces = [trace1]
            traces_results = efel.getFeatureValues(traces,['Spikecount'])
        
            #If a Spikecount of 0 is detected, print message and end loop
            if traces_results[0]['Spikecount'] == 0:
                AllC2Traces.append(0)
                x += 1
                continue
            
            #If a Spikecount of 1 is detected, record threshold AP parameters and end loop
            if traces_results[0]['Spikecount'] == 1:
                traces_results = efel.getFeatureValues(traces,['Spikecount','AP_rise_time','min_AHP_values','AP_begin_voltage',
                                                       'AP_amplitude','AP_begin_indices','spike_half_width'])
                AP_Latency = mat['Time'][[traces_results[0]['AP_begin_indices'][0]]] - 201
                trace_results['AHP'] = traces_results[0]['min_AHP_values'] - traces_results[0]['AP_begin_voltage']
                Threshold_AP = {'AP_Latency': AP_Latency, 'AP_Threshold': traces_results[0]['AP_begin_voltage'][0],
                            'AP_Amplitude': traces_results[0]['AP_amplitude'][0], 'AP_Rise': traces_results[0]['AP_rise_time'][0],
                            'AP_Half-Height_Width': float(traces_results[0]['spike_half_width']),
                            'AHP_Amplitude': trace_results['AHP'][0]}
                
                AllC2Traces.append(Threshold_AP)
                
                x += 1
                continue
        
            #If Spikecount is greater than 1, the code continues as normal
            traces_results = efel.getFeatureValues(traces,[
                                            'AP_begin_voltage','voltage_base','AP_amplitude','AP_rise_time',
                                            'Spikecount','min_AHP_values','AP_begin_indices','peak_time',
                                            'ISI_values','spike_width2'])
    
            #Algorithm cannot run if no ISI values are detected (Replaces NoneType with an array containing a 0 that will be replaced)
            if traces_results[0]['Spikecount'] == 2:
                traces_results[0]['ISI_values'] = np.array(0)
            
            #Calculate initial ISI value and insert this value into the 0 position of ISI values
            FirstISI = traces_results[0]['peak_time'][1] - traces_results[0]['peak_time'][0]
            trace_results['ISI_values'] = np.insert(traces_results[0]['ISI_values'],0,FirstISI)

            #Calculate AHP amplitude values
            trace_results['AHP'] = traces_results[0]['min_AHP_values'] - traces_results[0]['AP_begin_voltage']
        
            #Calculate Duration of Spiking
            trace_results['SpikeDur'] = mat['Time'][[traces_results[0]['AP_begin_indices'][-1]]] - mat['Time'][[traces_results[0]['AP_begin_indices'][0]]]
                
            #Calculate Frequency Parameters (Mean Instantaneous, Max, and Frequency Adaptation)
            Frequency = 1/trace_results['ISI_values']
            trace_results['MeanInstFreq'] = np.mean(Frequency)
            trace_results['MaxFreq'] = max(Frequency)
            trace_results['FreqAdapt'] = trace_results['ISI_values'][-1] / trace_results['ISI_values'][0]
    
            #Calculate AP Parameters (mean AP Amplitude and Peak Adaptation)
            trace_results['MeanAPAmp'] = np.mean(traces_results[0]['AP_amplitude'])
            trace_results['PeakAdapt'] = traces_results[0]['AP_amplitude'][-1] / traces_results[0]['AP_amplitude'][0]
        
            #Calculate AHP Parameters (mean AHP Amplitude and AHP Peak Adaptation)
            trace_results['MeanAHPAmp'] = np.mean(trace_results['AHP'])
            trace_results['AHPAdapt'] = trace_results['AHP'][-1] / trace_results['AHP'][0]
        
            #Append all salient parameters for each trace
            averages = {'AP #': int(traces_results[0]['Spikecount']), 'Duration_of_Spiking': trace_results['SpikeDur'],
            'Mean_Instantaneous_Frequency':trace_results['MeanInstFreq'],'Max_Frequency': trace_results['MaxFreq'],
            'Frequency_Adaptation': trace_results['FreqAdapt'], 'Mean_AP_Amplitude': trace_results['MeanAPAmp'],
            'Peak_Adaptation': trace_results['PeakAdapt'], 'Mean_AHP_Amplitude': trace_results['MeanAHPAmp'],
            'AHP_Adaptation': trace_results['AHPAdapt']}
        
            AllC2Traces.append(averages)
        
            x += 1
            
        print('All traces analyzed successfully!')
            
#Analysis for Cell 3            
if CellVal == 3:
    SingleC3Trace = list()
    #Analyze a single trace within an experiment
    if TraceVal <= 11:    
        for i in Cell3[ExptVal][TraceVal]:
            trace1 = {}
            trace1['T'] = mat['Time'][:]
            trace1['V'] = Cell3[ExptVal][:,TraceVal]
            trace1['stim_start'] = [201]
            trace1['stim_end'] = [700]
            traces = [trace1]
            traces_results = efel.getFeatureValues(traces,['Spikecount'])
            
            #If a Spikecount of 0 is detected, print message and end loop
            if traces_results[0]['Spikecount'] == 0:
                print('There are no spikes in this trace')
                break
            
            #If a Spikecount of 1 is detected, record threshold AP parameters and end loop
            if traces_results[0]['Spikecount'] == 1:
                traces_results = efel.getFeatureValues(traces,['Spikecount','AP_rise_time','min_AHP_values','AP_begin_voltage',
                                                       'AP_amplitude','AP_begin_indices','spike_half_width'])
                AP_Latency = mat['Time'][[traces_results[0]['AP_begin_indices'][0]]] - 201
                trace_results['AHP'] = traces_results[0]['min_AHP_values'] - traces_results[0]['AP_begin_voltage']
                Threshold_AP = {'AP_Latency': AP_Latency, 'AP_Threshold': traces_results[0]['AP_begin_voltage'][0],
                            'AP_Amplitude': traces_results[0]['AP_amplitude'][0], 'AP_Rise': traces_results[0]['AP_rise_time'][0],
                            'AP_Half-Height_Width': float(traces_results[0]['spike_half_width']),
                            'AHP_Amplitude': trace_results['AHP'][0]}
                
                SingleC3Trace.append(Threshold_AP)
                
                plt.plot(mat['Time'],Cell3[ExptVal][:,TraceVal])
                plt.xlabel('Time (in ms)')
                plt.ylabel('Voltage (in mV)')
                plt.show()
            
                print('Trace ' + str(TraceVal) + ' of Cell ' + str(CellVal) + ' analyzed successfully!')
                break
            
            #If Spikecount is greater than 1, the code continues as normal
            traces_results = efel.getFeatureValues(traces,[
                                            'AP_begin_voltage','voltage_base','AP_amplitude','AP_rise_time',
                                            'Spikecount','min_AHP_values','AP_begin_indices','peak_time',
                                            'ISI_values','spike_width2'])
            
            plt.plot(mat['Time'],Cell3[ExptVal][:,TraceVal])
            plt.xlabel('Time (in ms)')
            plt.ylabel('Voltage (in mV)')
            plt.show()
            
            #Calculate initial ISI value and insert this value into the 0 position of ISI values
            FirstISI = traces_results[0]['peak_time'][1] - traces_results[0]['peak_time'][0]
            trace_results['ISI_values'] = np.insert(traces_results[0]['ISI_values'],0,FirstISI)
    
            #Another error comes about if more AHP or threshold AP values are detected
            #This code automatically removes the problematic errors and makes the number of values equal for further calculations
            if len(traces_results[0]['min_AHP_values']) != len(traces_results[0]['AP_begin_voltage']):
                if len(traces_results[0]['min_AHP_values']) > len(traces_results[0]['AP_begin_voltage']):
                    traces_results[0]['min_AHP_values'] = np.delete(traces_results[0]['min_AHP_values'],-1)
                elif len(traces_results[0]['AP_begin_voltage']) > len(traces_results[0]['min_AHP_values']):
                    traces_results[0]['AP_begin_voltage'] = np.delete(traces_results[0]['AP_begin_voltage'],-1)
                    traces_results[0]['AP_begin_indices'] = np.delete(traces_results[0]['AP_begin_indices'],-1)
                    
            #Calculate AHP amplitude values
            trace_results['AHP'] = traces_results[0]['min_AHP_values'] - traces_results[0]['AP_begin_voltage']
    
            #Calculate Duration of Spiking
            trace_results['SpikeDur'] = mat['Time'][[traces_results[0]['AP_begin_indices'][-1]]] - mat['Time'][[traces_results[0]['AP_begin_indices'][0]]]
                
            #Calculate Frequency Parameters (Mean Instantaneous, Max, and Frequency Adaptation)
            Frequency = 1/trace_results['ISI_values']
            trace_results['MeanInstFreq'] = np.mean(Frequency)
            trace_results['MaxFreq'] = max(Frequency)
            trace_results['FreqAdapt'] = trace_results['ISI_values'][-1] / trace_results['ISI_values'][0]
    
            #Calculate AP Parameters (mean AP Amplitude and Peak Adaptation)
            trace_results['MeanAPAmp'] = np.mean(traces_results[0]['AP_amplitude'])
            trace_results['PeakAdapt'] = traces_results[0]['AP_amplitude'][-1] / traces_results[0]['AP_amplitude'][0]
    
            #Calculate AHP Parameters (mean AHP Amplitude and AHP Peak Adaptation)
            trace_results['MeanAHPAmp'] = np.mean(trace_results['AHP'])
            trace_results['AHPAdapt'] = trace_results['AHP'][-1] / trace_results['AHP'][0]
            
            #Insert all pertinent average data for each trace into a dictionary
            averages = {'AP #': int(traces_results[0]['Spikecount']), 'Duration_of_Spiking': trace_results['SpikeDur'],
            'Mean_Instantaneous_Frequency':trace_results['MeanInstFreq'],'Max_Frequency': trace_results['MaxFreq'],
            'Frequency_Adaptation': trace_results['FreqAdapt'], 'Mean_AP_Amplitude': trace_results['MeanAPAmp'],
            'Peak_Adaptation': trace_results['PeakAdapt'], 'Mean_AHP_Amplitude': trace_results['MeanAHPAmp'],
            'AHP_Adaptation': trace_results['AHPAdapt']}
            
            SingleC3Trace.append(averages)
            
            print('Trace ' + str(TraceVal) + ' of Cell ' + str(CellVal) + ' analyzed successfully!')
            
            break
            
#Analyze all traces within an experiment
    if TraceVal == 12:
        x = 0
        AllC3Traces = list()
        for i in Cell3[ExptVal][x:11:1]:
            trace1 = {}
            trace1['T'] = mat['Time'][:]
            trace1['V'] = Cell3[ExptVal][:,x]
            trace1['stim_start'] = [201]
            trace1['stim_end'] = [700]
            traces = [trace1]
            traces_results = efel.getFeatureValues(traces,['Spikecount'])
        
            #If a Spikecount of 0 is detected, print message and end loop
            if traces_results[0]['Spikecount'] == 0:
                AllC3Traces.append(0)
                x += 1
                continue
            
            #If a Spikecount of 1 is detected, record threshold AP parameters and end loop
            if traces_results[0]['Spikecount'] == 1:
                traces_results = efel.getFeatureValues(traces,['Spikecount','AP_rise_time','min_AHP_values','AP_begin_voltage',
                                                       'AP_amplitude','AP_begin_indices','spike_half_width'])
                AP_Latency = mat['Time'][[traces_results[0]['AP_begin_indices'][0]]] - 201
                trace_results['AHP'] = traces_results[0]['min_AHP_values'] - traces_results[0]['AP_begin_voltage']
                Threshold_AP = {'AP_Latency': AP_Latency, 'AP_Threshold': traces_results[0]['AP_begin_voltage'][0],
                            'AP_Amplitude': traces_results[0]['AP_amplitude'][0], 'AP_Rise': traces_results[0]['AP_rise_time'][0],
                            'AP_Half-Height_Width': float(traces_results[0]['spike_half_width']),
                            'AHP_Amplitude': trace_results['AHP'][0]}
                
                AllC3Traces.append(Threshold_AP)
                
                x += 1
                continue
        
            #If Spikecount is greater than 1, the code continues as normal
            traces_results = efel.getFeatureValues(traces,[
                                            'AP_begin_voltage','voltage_base','AP_amplitude','AP_rise_time',
                                            'Spikecount','min_AHP_values','AP_begin_indices','peak_time',
                                            'ISI_values','spike_width2'])
    
            #Algorithm cannot run if no ISI values are detected (Replaces NoneType with an array containing a 0 that will be replaced)
            if traces_results[0]['Spikecount'] == 2:
                traces_results[0]['ISI_values'] = np.array(0)
            
            #Calculate initial ISI value and insert this value into the 0 position of ISI values
            FirstISI = traces_results[0]['peak_time'][1] - traces_results[0]['peak_time'][0]
            trace_results['ISI_values'] = np.insert(traces_results[0]['ISI_values'],0,FirstISI)

            #Calculate AHP amplitude values
            trace_results['AHP'] = traces_results[0]['min_AHP_values'] - traces_results[0]['AP_begin_voltage']
        
            #Calculate Duration of Spiking
            trace_results['SpikeDur'] = mat['Time'][[traces_results[0]['AP_begin_indices'][-1]]] - mat['Time'][[traces_results[0]['AP_begin_indices'][0]]]
                
            #Calculate Frequency Parameters (Mean Instantaneous, Max, and Frequency Adaptation)
            Frequency = 1/trace_results['ISI_values']
            trace_results['MeanInstFreq'] = np.mean(Frequency)
            trace_results['MaxFreq'] = max(Frequency)
            trace_results['FreqAdapt'] = trace_results['ISI_values'][-1] / trace_results['ISI_Values'][0]
    
            #Calculate AP Parameters (mean AP Amplitude and Peak Adaptation)
            trace_results['MeanAPAmp'] = np.mean(traces_results[0]['AP_amplitude'])
            trace_results['PeakAdapt'] = traces_results[0]['AP_amplitude'][-1] / traces_results[0]['AP_amplitude'][0]
        
            #Calculate AHP Parameters (mean AHP Amplitude and AHP Peak Adaptation)
            trace_results['MeanAHPAmp'] = np.mean(trace_results['AHP'])
            trace_results['AHPAdapt'] = trace_results['AHP'][-1] / trace_results['AHP'][0]
        
            #Append all salient parameters for each trace
            averages = {'AP #': int(traces_results[0]['Spikecount']), 'Duration_of_Spiking': trace_results['SpikeDur'],
            'Mean_Instantaneous_Frequency':trace_results['MeanInstFreq'],'Max_Frequency': trace_results['MaxFreq'],
            'Frequency_Adaptation': trace_results['FreqAdapt'], 'Mean_AP_Amplitude': trace_results['MeanAPAmp'],
            'Peak_Adaptation': trace_results['PeakAdapt'], 'Mean_AHP_Amplitude': trace_results['MeanAHPAmp'],
            'AHP_Adaptation': trace_results['AHPAdapt']}
        
            AllC3Traces.append(averages)
        
            x += 1
            
            print('All traces analyzed successfully!')

            
#Analysis for Cell 4
if CellVal == 4:
    SingleC4Trace = list()
    #Analyze a single trace within an experiment
    if TraceVal <= 11:    
        for i in Cell4[ExptVal][TraceVal]:
            trace1 = {}
            trace1['T'] = mat['Time'][:]
            trace1['V'] = Cell4[ExptVal][:,TraceVal]
            trace1['stim_start'] = [201]
            trace1['stim_end'] = [700]
            traces = [trace1]
            traces_results = efel.getFeatureValues(traces,['Spikecount'])
            
            #If a Spikecount of 0 is detected, print message and end loop
            if traces_results[0]['Spikecount'] == 0:
                print('There are no spikes in this trace')
                break
            
            #If a Spikecount of 1 is detected, record threshold AP parameters and end loop
            if traces_results[0]['Spikecount'] == 1:
                traces_results = efel.getFeatureValues(traces,['Spikecount','AP_rise_time','min_AHP_values','AP_begin_voltage',
                                                       'AP_amplitude','AP_begin_indices','spike_half_width'])
                AP_Latency = mat['Time'][[traces_results[0]['AP_begin_indices'][0]]] - 201
                trace_results['AHP'] = traces_results[0]['min_AHP_values'] - traces_results[0]['AP_begin_voltage']
                Threshold_AP = {'AP_Latency': AP_Latency, 'AP_Threshold': traces_results[0]['AP_begin_voltage'][0],
                            'AP_Amplitude': traces_results[0]['AP_amplitude'][0], 'AP_Rise': traces_results[0]['AP_rise_time'][0],
                            'AP_Half-Height_Width': float(traces_results[0]['spike_half_width']),
                            'AHP_Amplitude': trace_results['AHP'][0]}
                
                SingleC4Trace.append(Threshold_AP)
                
                plt.plot(mat['Time'],Cell4[ExptVal][:,TraceVal])
                plt.xlabel('Time (in ms)')
                plt.ylabel('Voltage (in mV)')
                plt.show()
            
                print('Trace ' + str(TraceVal) + ' of Cell ' + str(CellVal) + ' analyzed successfully!')
                break
            
            #If Spikecount is greater than 1, the code continues as normal
            traces_results = efel.getFeatureValues(traces,[
                                            'AP_begin_voltage','voltage_base','AP_amplitude','AP_rise_time',
                                            'Spikecount','min_AHP_values','AP_begin_indices','peak_time',
                                            'ISI_values','spike_width2'])
            
            plt.plot(mat['Time'],Cell3[ExptVal][:,TraceVal])
            plt.xlabel('Time (in ms)')
            plt.ylabel('Voltage (in mV)')
            plt.show()
            
            #Calculate initial ISI value and insert this value into the 0 position of ISI values
            FirstISI = traces_results[0]['peak_time'][1] - traces_results[0]['peak_time'][0]
            trace_results['ISI_values'] = np.insert(traces_results[0]['ISI_values'],0,FirstISI)
    
            #Another error comes about if more AHP or threshold AP values are detected
            #This code automatically removes the problematic errors and makes the number of values equal for further calculations
            if len(traces_results[0]['min_AHP_values']) != len(traces_results[0]['AP_begin_voltage']):
                if len(traces_results[0]['min_AHP_values']) > len(traces_results[0]['AP_begin_voltage']):
                    traces_results[0]['min_AHP_values'] = np.delete(traces_results[0]['min_AHP_values'],-1)
                elif len(traces_results[0]['AP_begin_voltage']) > len(traces_results[0]['min_AHP_values']):
                    traces_results[0]['AP_begin_voltage'] = np.delete(traces_results[0]['AP_begin_voltage'],-1)
                    traces_results[0]['AP_begin_indices'] = np.delete(traces_results[0]['AP_begin_indices'],-1)
                    
            #Calculate AHP amplitude values
            trace_results['AHP'] = traces_results[0]['min_AHP_values'] - traces_results[0]['AP_begin_voltage']
    
            #Calculate Duration of Spiking
            trace_results['SpikeDur'] = mat['Time'][[traces_results[0]['AP_begin_indices'][-1]]] - mat['Time'][[traces_results[0]['AP_begin_indices'][0]]]
                
            #Calculate Frequency Parameters (Mean Instantaneous, Max, and Frequency Adaptation)
            Frequency = 1/trace_results['ISI_values']
            trace_results['MeanInstFreq'] = np.mean(Frequency)
            trace_results['MaxFreq'] = max(Frequency)
            trace_results['FreqAdapt'] = trace_results['ISI_values'][-1] / trace_results['ISI_values'][0]
    
            #Calculate AP Parameters (mean AP Amplitude and Peak Adaptation)
            trace_results['MeanAPAmp'] = np.mean(traces_results[0]['AP_amplitude'])
            trace_results['PeakAdapt'] = traces_results[0]['AP_amplitude'][-1] / traces_results[0]['AP_amplitude'][0]
    
            #Calculate AHP Parameters (mean AHP Amplitude and AHP Peak Adaptation)
            trace_results['MeanAHPAmp'] = np.mean(trace_results['AHP'])
            trace_results['AHPAdapt'] = trace_results['AHP'][-1] / trace_results['AHP'][0]
            
            #Insert all pertinent average data for each trace into a dictionary
            averages = {'AP #': int(traces_results[0]['Spikecount']), 'Duration_of_Spiking': trace_results['SpikeDur'],
            'Mean_Instantaneous_Frequency':trace_results['MeanInstFreq'],'Max_Frequency': trace_results['MaxFreq'],
            'Frequency_Adaptation': trace_results['FreqAdapt'], 'Mean_AP_Amplitude': trace_results['MeanAPAmp'],
            'Peak_Adaptation': trace_results['PeakAdapt'], 'Mean_AHP_Amplitude': trace_results['MeanAHPAmp'],
            'AHP_Adaptation': trace_results['AHPAdapt']}
            
            SingleC3Trace.append(averages)
            
            print('Trace ' + str(TraceVal) + ' of Cell ' + str(CellVal) + ' analyzed successfully!')
            
            break
            
#Analyze all traces within an experiment
    if TraceVal == 12:
        x = 0
        AllC4Traces = list()
        for i in Cell4[ExptVal][x:11:1]:
            trace1 = {}
            trace1['T'] = mat['Time'][:]
            trace1['V'] = Cell4[ExptVal][:,x]
            trace1['stim_start'] = [201]
            trace1['stim_end'] = [700]
            traces = [trace1]
            traces_results = efel.getFeatureValues(traces,['Spikecount'])
        
            #If a Spikecount of 0 is detected, print message and end loop
            if traces_results[0]['Spikecount'] == 0:
                AllC4Traces.append(0)
                x += 1
                continue
            
            #If a Spikecount of 1 is detected, record threshold AP parameters and end loop
            if traces_results[0]['Spikecount'] == 1:
                traces_results = efel.getFeatureValues(traces,['Spikecount','AP_rise_time','min_AHP_values','AP_begin_voltage',
                                                       'AP_amplitude','AP_begin_indices','spike_half_width'])
                AP_Latency = mat['Time'][[traces_results[0]['AP_begin_indices'][0]]] - 201
                trace_results['AHP'] = traces_results[0]['min_AHP_values'] - traces_results[0]['AP_begin_voltage']
                Threshold_AP = {'AP_Latency': AP_Latency, 'AP_Threshold': traces_results[0]['AP_begin_voltage'][0],
                            'AP_Amplitude': traces_results[0]['AP_amplitude'][0], 'AP_Rise': traces_results[0]['AP_rise_time'][0],
                            'AP_Half-Height_Width': float(traces_results[0]['spike_half_width']),
                            'AHP_Amplitude': trace_results['AHP'][0]}
                
                AllC4Traces.append(Threshold_AP)
                
                x += 1
                continue
        
            #If Spikecount is greater than 1, the code continues as normal
            traces_results = efel.getFeatureValues(traces,[
                                            'AP_begin_voltage','voltage_base','AP_amplitude','AP_rise_time',
                                            'Spikecount','min_AHP_values','AP_begin_indices','peak_time',
                                            'ISI_values','spike_width2'])
    
            #Algorithm cannot run if no ISI values are detected (Replaces NoneType with an array containing a 0 that will be replaced)
            if traces_results[0]['Spikecount'] == 2:
                traces_results[0]['ISI_values'] = np.array(0)
            
            #Calculate initial ISI value and insert this value into the 0 position of ISI values
            FirstISI = traces_results[0]['peak_time'][1] - traces_results[0]['peak_time'][0]
            trace_results['ISI_values'] = np.insert(traces_results[0]['ISI_values'],0,FirstISI)

            #Calculate AHP amplitude values
            trace_results['AHP'] = traces_results[0]['min_AHP_values'] - traces_results[0]['AP_begin_voltage']
        
            #Calculate Duration of Spiking
            trace_results['SpikeDur'] = mat['Time'][[traces_results[0]['AP_begin_indices'][-1]]] - mat['Time'][[traces_results[0]['AP_begin_indices'][0]]]
                
            #Calculate Frequency Parameters (Mean Instantaneous, Max, and Frequency Adaptation)
            Frequency = 1/trace_results['ISI_values']
            trace_results['MeanInstFreq'] = np.mean(Frequency)
            trace_results['MaxFreq'] = max(Frequency)
            trace_results['FreqAdapt'] = trace_results['ISI_values'][-1] / trace_results['ISI_values'][0]
    
            #Calculate AP Parameters (mean AP Amplitude and Peak Adaptation)
            trace_results['MeanAPAmp'] = np.mean(traces_results[0]['AP_amplitude'])
            trace_results['PeakAdapt'] = traces_results[0]['AP_amplitude'][-1] / traces_results[0]['AP_amplitude'][0]
        
            #Calculate AHP Parameters (mean AHP Amplitude and AHP Peak Adaptation)
            trace_results['MeanAHPAmp'] = np.mean(trace_results['AHP'])
            trace_results['AHPAdapt'] = trace_results['AHP'][-1] / trace_results['AHP'][0]
        
            #Append all salient parameters for each trace
            averages = {'AP #': int(traces_results[0]['Spikecount']), 'Duration_of_Spiking': trace_results['SpikeDur'],
            'Mean_Instantaneous_Frequency':trace_results['MeanInstFreq'],'Max_Frequency': trace_results['MaxFreq'],
            'Frequency_Adaptation': trace_results['FreqAdapt'], 'Mean_AP_Amplitude': trace_results['MeanAPAmp'],
            'Peak_Adaptation': trace_results['PeakAdapt'], 'Mean_AHP_Amplitude': trace_results['MeanAHPAmp'],
            'AHP_Adaptation': trace_results['AHPAdapt']}
        
            AllC4Traces.append(averages)
        
            x += 1
            
            print('All traces analyzed successfully!')