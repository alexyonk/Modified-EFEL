#                   EFEL for HEKA DAT Files v4.0
#                   *Created by AY on 5/26/2021*
#                   *Last Updated on 3/2/2022*
#     *For any issues or bugs, please contact alex.yonk2@gmail.com*
#*This script was designed to analyze electrophysiological parameters from HEKA .dat files converted into mat files
#*It must be used in conjunction with the HEKA_importer MATLAB script
#*The output can be combined with the EI_Balance_Analysis to perform E/I analysis
#*****However, the E/I analysis requires text file output from the SP CC and the SP E/I analysis from this script
#*Averages can be calculated through the accompanying Multi_SP/PPR/Train scripts

#Import these scripts (Install them too!)
from scipy.io import loadmat, matlab
import efel
import pandas as pd
import numpy as np
from tkinter import filedialog
from matplotlib import pyplot as plt
from csv import DictWriter
import csv
from os import chdir, getcwd

#Enable EFEL Settings
efel.setDoubleSetting('interp_step',0.05) #Must be set to the sampling rate (20,000 Hz = 0.05)
efel.setDoubleSetting('voltage_base_start_perc',0.1)
efel.setDoubleSetting('voltage_base_end_perc',0.8)
efel.setDerivativeThreshold(10) #Value can be changed, but normally set to 10
efel.setThreshold(10)

#Create global variable to store parameter information
Results = list()
trace_calc = dict()
User_choices = dict()
Cell = dict()

#Function that loads nested mat structures into a dictionary instead of using dot notation to
#extract individual pieces of data
def load_mat(filename):
    """
    This function should be called instead of direct scipy.io.loadmat
    as it cures the problem of not properly recovering python dictionaries
    from mat files. It calls the function check keys to cure all entries
    which are still mat-objects
    """

    def _check_vars(d):
        """
        Checks if entries in dictionary are mat-objects. If yes
        todict is called to change them to nested dictionaries
        """
        for key in d:
            if isinstance(d[key], matlab.mio5_params.mat_struct):
                d[key] = _todict(d[key])
            elif isinstance(d[key], np.ndarray):
                d[key] = _toarray(d[key])
        return d

    def _todict(matobj):
        """
        A recursive function which constructs from matobjects nested dictionaries
        """
        d = {}
        for strg in matobj._fieldnames:
            elem = matobj.__dict__[strg]
            if isinstance(elem, matlab.mio5_params.mat_struct):
                d[strg] = _todict(elem)
            elif isinstance(elem, np.ndarray):
                d[strg] = _toarray(elem)
            else:
                d[strg] = elem
        return d

    def _toarray(ndarray):
        """
        A recursive function which constructs ndarray from cellarrays
        (which are loaded as numpy ndarrays), recursing into the elements
        if they contain matobjects.
        """
        if ndarray.dtype != 'float64':
            elem_list = []
            for sub_elem in ndarray:
                if isinstance(sub_elem, matlab.mio5_params.mat_struct):
                    elem_list.append(_todict(sub_elem))
                elif isinstance(sub_elem, np.ndarray):
                    elem_list.append(_toarray(sub_elem))
                else:
                    elem_list.append(sub_elem)
            return np.array(elem_list)
        else:
            return ndarray

    data = loadmat(filename, struct_as_record=False, squeeze_me=True)
    return _check_vars(data)

#Allows user to select and set working directory
wd = filedialog.askdirectory()
chdir(wd)

#Opens a dialog box allowing the user to select the file and removes the extension from the file name & load in the file
file_path = filedialog.askopenfilename()
AllData = load_mat(file_path)

#Describe the number of cells present in the file
print('There are *** ' +str(int(AllData['Data']['CellNum'])) + ' *** cells in this file.')

#Allows user to choose which cell they want to analyze
User_choices['CellVal'] = int(input('Which cell would you like to analyze?: '))

#Selects and stores data in a new variable that can be more easily accessed
SelectCell = AllData['Data']['Cell' + str(User_choices['CellVal'])]

#Prints the number of experiments and type of each experiment for user selection
print('There are *** ' + str(int(SelectCell['Expts'])) + ' *** experiments for this cell.' + '\n')
for i in range(SelectCell['Expts']):
    Cols = np.shape([SelectCell['Exp' + str(i + 1)][1]])
    print('Experiment ' + str(i + 1) + ' is a(n) ' + str(SelectCell['ExptID' + str(i + 1)]) + ' contains *** ' + str(Cols[1]) + ' *** traces.')
    
User_choices['ExptVal'] = int(input('Which experiment would you like to analyze?:'))

#Stores all pertinent information into a new variable that will be accessed for all analyses
Cell['ExptID'] = AllData['Data']['Cell' + str(User_choices['CellVal'])]['ExptID' + str(User_choices['ExptVal'])]
Cell['Data'] = AllData['Data']['Cell' + str(User_choices['CellVal'])]['Exp' + str(User_choices['ExptVal'])]
Cell['Stim'] = AllData['Data']['Cell' + str(User_choices['CellVal'])]['Stim' + str(User_choices['ExptVal'])]
Cell['TraceMax'] = np.shape(SelectCell['Exp' + str(User_choices['ExptVal'])])
Cell['Time'] = AllData['Data']['Time'][0:Cell['Data'].shape[0]]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Calculates IV curve parameters including spikecount, RMP, Rin, Freq, etc.
if 'IV' in Cell['ExptID']:
    User_choices['IV_graph'] = int(input('Would you like to save the graph? (Input 1 if yes): '))
    User_choices['IV_output'] = int(input('Would you like to output the results as a CSV? (Input 1 if yes): '))
    
    x = 0
    for i in Cell['Data'][x:Cell['TraceMax'][1]:1]:
        trace1 = {}
        trace1['T'] = Cell['Time'][:]
        trace1['V'] = Cell['Data'][:,x]
        trace1['stim_start'] = [201]
        trace1['stim_end'] = [700]
        traces = [trace1]
        traces_results = efel.getFeatureValues(traces,['Spikecount','voltage_base','peak_voltage','peak_time'])
    
        #If a Spikecount of 0 is detected, continue for loop
        #Cannot append "N/A" as the DictWriter won't work
        if traces_results[0]['Spikecount'] == 0:
            x += 1
            continue
        
        #If a Spikecount of 1 is detected, plot graph and continue
        #Potential to be modified if Threshold_AP is needed for each trace
        if traces_results[0]['Spikecount'] == 1:
            #Calculate input resistance based on lowest hyperpolarizing step (Hard coded hyperpolarizing step)
            trace_calc['Vin'] = (((Cell['Data'][6000,5]) - (Cell['Data'][2000,5])) / 1000) #Voltage is calculated in mV, but converted to V
            trace_calc['Iin'] = (((Cell['Stim'][6000,5]) - (Cell['Stim'][2000,5])) / 1000000) #Current is calculated in microA, but converted to A
            trace_calc['Rin'] = ((trace_calc['Vin']/trace_calc['Iin']) / 1000) #Resistance is provided in MOhms
            trace_calc['Rheo'] = ((Cell['Stim'][4001,x])*1000)+1
            Trace_Results = {'AP #': int(traces_results[0]['Spikecount']), 'RMP': float(traces_results[0]['voltage_base']),
                             'Rin': trace_calc['Rin'],'Rheobase': int(trace_calc['Rheo'])}
            
            Results.append(Trace_Results)
            
            #Plot individual traces with one spike
            plt.plot(Cell['Time'],Cell['Data'][:,x])
            plt.title('Cell ' + str(User_choices['CellVal']) + ', Trace ' + str(x))
            plt.scatter(traces_results[0]['peak_time'],traces_results[0]['peak_voltage'] + 20,c='r',marker = '+')
            plt.xlabel('Time (in ms)')
            plt.ylabel('Voltage (in mV)')
            plt.show()
            x+= 1
            continue
        
        #If Spikecount is greater than 1, the code continues as normal
        if traces_results[0]['Spikecount'] >= 2:
            traces_results = efel.getFeatureValues(traces,[
                'AP_begin_voltage','voltage_base','AP_amplitude','AP_rise_time',
                'Spikecount','min_AHP_values','min_AHP_indices','AP_begin_indices','peak_time','spike_half_width',
                'peak_voltage'])

        #Removes erroneously detected AP_begin_indices at the end of the trace if present
        if traces_results[0]['AP_begin_indices'][-1] > 14000:
            traces_results[0]['AP_begin_indices'] = np.delete(traces_results[0]['AP_begin_indices'], -1)
            traces_results[0]['AP_begin_voltage'] = np.delete(traces_results[0]['AP_begin_voltage'], -1)
        
        #Converts peak time values into individual sampling points for comparison against AP_begin_indices values
        traces_results[0]['peak_time'] = traces_results[0]['peak_time'] / 0.05

        #An error occurs when the number of peak_time indices does not equal the number of AP begin indices
        #To correct for erroneous values, a while loop circles through and removes inappropriate values
        #until the number of peak_time and AP_begin indices are equal
        while len(traces_results[0]['AP_begin_indices']) != len(traces_results[0]['peak_time']):
            oper_ind_list = [traces_results[0]['AP_begin_indices'],traces_results[0]['peak_time']]
            operdifflist = np.empty((max(y.shape[0] for y in oper_ind_list), len(oper_ind_list)))
            operdifflist[:] = np.nan
            for i,y in enumerate(oper_ind_list):
                operdifflist[0:len(y), i] = y.T
            oper_diff = np.diff(operdifflist)
            oper_del = np.where(oper_diff < 0)
            
            #Conditional if statement to catch when the difference is 0, but the parameters are not equal
            #Usually means that there is an extra value (read NaN) at the end
            if len(oper_del[0]) == 0:
                oper_del = np.argwhere(np.isnan(oper_diff))
            
            #Deletes the value corresponding to inappropriate values from specified parameters
            traces_results[0]['peak_time'] = np.delete(traces_results[0]['peak_time'], oper_del[0][0])
            traces_results[0]['peak_voltage'] = np.delete(traces_results[0]['peak_voltage'], oper_del[0][0])    
            traces_results[0]['Spikecount'] = traces_results[0]['Spikecount'] - 1    
            
            if len(traces_results[0]['AP_begin_indices']) == len(traces_results[0]['peak_time']):
                break
        
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

        #Based on EFEL's calculation of specific parameters, there may be erroneous spike_half_width values
        #that need to be removed. This while loop removes inappropriate values if present
        while np.any(traces_results[0]['spike_half_width'] < 0.1):
            oper_del3 = np.where(traces_results[0]['spike_half_width'] < 0.1)
            traces_results[0]['spike_half_width'] = np.delete(traces_results[0]['spike_half_width'], oper_del3[0][0])
            
        while np.any(traces_results[0]['spike_half_width'] > 5):
            oper_del4 = np.where(traces_results[0]['spike_half_width'] > 5)
            traces_results[0]['spike_half_width'] = np.delete(traces_results[0]['spike_half_width'], oper_del4[0][0])
        
        #Converts peak time values back to ms for proper graph plotting
        #Also, calculates rheobase when the first spiking sweep has multiple APs
        traces_results[0]['peak_time'] = traces_results[0]['peak_time'] * 0.05
        if not Results:
            trace_calc['Rheo'] = ((Cell['Stim'][4001,x])*1000)+1

        #Calculate ISI values based on AP_begin_indices and multiply each value by the sampling point value (0.05ms)
        traces_results[0]['ISI_values'] = np.diff(traces_results[0]['AP_begin_indices']) * 0.05
        
        #Calculate AP amplitude by subtracting peak voltage from AP threshold values
        traces_results[0]['AP_Amplitude'] = traces_results[0]['peak_voltage'] - traces_results[0]['AP_begin_voltage']
    
        #Calculate AHP values by subtracting the minimum AHP values from the AP threshold values
        traces_results[0]['AHP'] = traces_results[0]['min_AHP_values'] - traces_results[0]['AP_begin_voltage']

        #Calculate Duration of Spiking by subtracting the x-axis index of the last spike from the x-axis index
        #of the first spike
        traces_results[0]['DurSpike'] = Cell['Time'][[traces_results[0]['AP_begin_indices'][-1]]] - Cell['Time'][[traces_results[0]['AP_begin_indices'][0]]]
        
        #Calculate iniput resistance based on the lowest hyperpolarizing step (Hard coded hyperpolarizing step)
        trace_calc['Vin'] = (((Cell['Data'][6000,5]) - (Cell['Data'][2000,5])) / 1000) #Voltage is calculated in mV, but converted to V
        trace_calc['Iin'] = (((Cell['Stim'][6000,5]) - (Cell['Stim'][2000,5])) / 1000000) #Current is calculated in microA, but converted to A
        traces_results[0]['Rin'] = ((trace_calc['Vin']/trace_calc['Iin']) / 1000) #Resistance is provided in MOhms
        
        #Calculate frequency and adaptation parameters
        Frequency = 1 / traces_results[0]['ISI_values']
        traces_results[0]['MeanInstFreq'] = np.mean(Frequency) * 1000
        traces_results[0]['MaxFreq'] = np.max(Frequency) * 1000
        traces_results[0]['FreqAdapt'] = traces_results[0]['ISI_values'][-1] / traces_results[0]['ISI_values'][0]
        traces_results[0]['PeakAdapt'] = traces_results[0]['AP_Amplitude'][-1] / traces_results[0]['AP_Amplitude'][0]

        #Plot individual sweeps in the output window
        plt.plot(Cell['Time'],Cell['Data'][:,x])
        plt.title('Trace ' + str(x))
        plt.scatter(traces_results[0]['peak_time'],traces_results[0]['peak_voltage'] + 20, c = 'r', marker = '+')
        plt.xlabel('Time (in ms)')
        plt.ylabel('Voltage (in mV)')
        plt.show()

        #Save all sweep results in a dictionary
        Trace_Results = {'AP #': int(traces_results[0]['Spikecount']), 'RMP': float(traces_results[0]['voltage_base']),
                         'Rin': traces_results[0]['Rin'], 'Duration_of_Spiking': float(traces_results[0]['DurSpike']),
                         'Mean_Half-Height_Width': np.mean(traces_results[0]['spike_half_width']),
                         'Mean_AP_Amplitude': np.mean(traces_results[0]['AP_Amplitude']), 'Mean_Inst_Freq': traces_results[0]['MeanInstFreq'],
                         'Max_Freq': traces_results[0]['MaxFreq'], 'Freq_Adapt': traces_results[0]['FreqAdapt'],
                         'Peak_Adapt': traces_results[0]['PeakAdapt'], 'Mean_ISI': np.mean(traces_results[0]['ISI_values']),
                         'Mean_AHP_Amplitude': np.mean(traces_results[0]['AHP']), 'Rheobase': int(trace_calc['Rheo'])}
            
        #Append each dictionary into a list
        Results.append(Trace_Results)
            
        #Variable to iterate through the traces
        x += 1
    
    plt.plot(Cell['Time'],Cell['Data'])
    plt.title('All Traces')
    plt.xlabel('Time (in ms)')
    plt.ylabel('Voltage (in mV)')
    if User_choices['IV_graph'] == 1:
        #Change the string here to modify the output graph name
        plt.savefig('IV.svg',format='svg',dpi = 1200)
    plt.show()
    
    #Outputs IV parameters into a CSV
    if User_choices['IV_output'] == 1:
        with open(str(AllData['filename']) + '_IV.csv','w') as IV:
            writer1 = DictWriter(IV,('AP #','RMP','Rin','Rheobase','Duration_of_Spiking',
                                     'Mean_Half-Height_Width','Mean_AP_Amplitude',
                                     'Mean_Inst_Freq','Max_Freq','Freq_Adapt','Peak_Adapt',
                                     'Mean_ISI','Mean_AHP_Amplitude'))
            writer1.writeheader()
            writer1.writerows(Results)
            IV.close()            

    if not Results:
        print('\n' + 'No spikes detected in Experiment ' + str(User_choices['ExptVal']) + ' for Cell ' + str(User_choices['CellVal']))
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Used to calculate single pulse parameters (all sweeps)
elif 'SP CC' in Cell['ExptID']:
    #Allows the user to save the average graph, if needed
    User_choices['SPCCGraph'] = input('Would you like to save the average/individual trace graph? (Input "Yes" or "No"): ')
    
    #Asks the user if any traces need to be NaNed out
    #If the user chooses 0, continue with the analysis
    #If the user chooses 1, script asks user for number of traces to be NaNed
    #and runs a for loop to nan out selected traces
    User_choices['SP NaN'] = int(input('If traces need to be NaNed, input 1. Otherwise, input 0: '))
    if User_choices['SP NaN'] == 0:
        print('Continuing to SP Analysis')
    if User_choices['SP NaN'] == 1:
        User_choices['SP_NaN_Trace'] = int(input('Please input the number of traces to be NaNed: '))
        for i in range(User_choices['SP_NaN_Trace']):
            User_choices['SP_Traces'] = int(input('Please input the trace to be Naned from 0 to ' + str(Cell['TraceMax'][1]) + ' : '))
            Cell['Data'][:,User_choices['SP_Traces']] = np.nan
    
    #Set up lists to append data
    SPAmp = list()
    SPLat = list()
    SP_Indamp = list()
    
    #Calculate baseline, max amplitude, latency (from beginning of stim to max value), and trace values for each sweep
    for i in range(Cell['TraceMax'][1]):
       trace_base = np.nanmean(Cell['Data'][0:4000,i])
       zero_trace = Cell['Data'][:,i] - trace_base
       latency = ((np.argmax(zero_trace[9500:12000]) + 9500) - 10000) * 0.05
       PSP = np.nanmax(zero_trace[9500:12000])
       SPAmp.append(zero_trace)
       SPLat.append(latency)
       SP_Indamp.append(PSP)

    #Calculate the average latency and jitter to determine monosynaptic/disynaptic effect
    AvgLat = np.nanmean(SPLat)
    Jitter = np.std(SPLat)
       
    #Concatenate list of np arrays into a single array to calculate average trace plot
    AvgTrace = np.column_stack(SPAmp)
    AvgTrace = np.nanmean(AvgTrace,axis = 1)
    AvgPSP = np.nanmax(AvgTrace[10000:11000])

    #Plot average trace with all sweeps
    fig,ax = plt.subplots()
    for i in range(Cell['TraceMax'][1]):
        ax.plot(Cell['Time'][9500:12000],SPAmp[i][9500:12000], c ='lightgray',linewidth = 0.3)
        ax.plot(Cell['Time'][9500:12000],AvgTrace[9500:12000], c = 'k')
        ax.scatter(500,-2,c = 'blue', marker = 's')
    ax.title.set_text('Average PSP')
    ax.set_xlabel('Time (in ms)')
    ax.set_ylabel('PSP Amplitude (in mV)')
    if User_choices['SPCCGraph'] == 'Yes':
        plt.savefig('SPNSP.svg',format = 'svg',dpi = 1200)
    plt.show()
    plt.close()
    
    #Print what the maximal PSP is in the output window
    print('The mean PSP is ' + str(AvgPSP) + ' mV.')
    
    np.savetxt(str(AllData['filename']) + '_C' + str(User_choices['CellVal']) + '_SP.txt', SP_Indamp)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Calculates the PPR Ratio of pulses 2-5 compared to the amplitude of pulse 1
elif 'PPR CC' in Cell['ExptID']:
    #Allows the user to save the average graph, if needed
    User_choices['PPRGraph'] = input('Would you like to save the average/individual trace graph? (Input "Yes" or "No"): ')
    
    #Same NaNing method as SP
    User_choices['PPR NaN'] = int(input('If traces need to be NaNed, input 1. Otherwise, input 0: '))
    if User_choices['PPR NaN'] == 0:
        print('Continuing to SP Analysis')
    if User_choices['PPR NaN'] == 1:
        User_choices['PPR_NaN_Trace'] = int(input('Please input the number of traces to be NaNed: '))
        for i in range(User_choices['PPR_NaN_Trace']):
            User_choices['PPR_Traces'] = int(input('Please input the trace to be Naned from 0 to ' + str(Cell['TraceMax'][1]) + ' : '))
            Cell['Data'][:,User_choices['PPR_Traces']] = np.nan

    PPRBase = list()
    PPRAmp = list()
    PPRPSP = list()
    AvgPSP = list()
    AvgPPR = list()
    
    #Calculate initial baseline and subtract it from all sweep values for a baseline of 00
    for i in range(Cell['TraceMax'][1]):
        base = np.nanmean(Cell['Data'][0:4000,i])
        zero_trace = Cell['Data'][:,i] - base
        PPRAmp.append(zero_trace)
    
    #Calculate max amplitude for all 5 peaks compared to single baseline value for each sweep
    PPRAmp = np.transpose(PPRAmp)
    for i in range(int(Cell['TraceMax'][1])):
        iterstart = 4001
        iterend = 5000
        for ii in range(5):
            psp = np.nanmax(PPRAmp[iterstart:iterend,i])
            PPRPSP.append(psp)
            iterstart += 1000
            iterend += 1000
    
    #Concatenate all PSP values together
    PPRPSP = np.array(PPRPSP)
    PPRPSP = np.split(PPRPSP,int(Cell['TraceMax'][1]),0)
    PPRPSP = np.column_stack(PPRPSP)
    
    #Calculate the average PSP for each pulse
    for i in range(5):
        MeanPSP = np.nanmean(PPRPSP[i])
        AvgPSP.append(MeanPSP)
    
    #Calculate pulse ratios compared to pulse 1
    FinalPSP = np.array([AvgPSP[0]/AvgPSP[0], AvgPSP[1]/AvgPSP[0], AvgPSP[2]/AvgPSP[0], AvgPSP[3]/AvgPSP[0], AvgPSP[4]/AvgPSP[0]])
    
    #Calculate final averaged plot
    AvgTrace = np.nanmean(PPRAmp,axis = 1)
    
    #Plot all individual traces of RawPPRCC
    plt.plot(Cell['Time'],Cell['Data'])
    plt.xlabel('Time (in ms)')
    plt.ylabel('Voltage (in mV)')
    plt.show()
    
    #Plots box plot of PPR compared to P1
    x = 1,2,3,4,5
    plt.axhline(1,linestyle = '--',c = 'b')
    #plt.errorbar(x, PPR, yerr= PPRSEM, ls = 'none', c = 'k')
    plt.scatter(x,FinalPSP,marker = '+',s = 20**2, c = 'r')
    plt.xticks([1,2,3,4,5])
    plt.title('PPR of Cell ' + str(User_choices['CellVal']) + ', Experiment ' + str(User_choices['ExptVal']))
    plt.xlabel('Pulse #')
    plt.ylabel('PPR (Ratio of P1)')
    #plt.ylim([0.75,1.25])
    plt.show()

    #Plots average trace in black overlaid on individual PPR sweeps
    fig,ax = plt.subplots()
    for i in range(Cell['TraceMax'][1]):
        ax.plot(PPRAmp[3700:9500,i], c ='lightgray')
        ax.plot(AvgTrace[3700:9500], c = 'k')
        ax.scatter(301,-2,c = 'blue', marker = 's')
        ax.scatter(1351,-2,c = 'blue', marker = 's')
        ax.scatter(2401,-2,c = 'blue', marker = 's')
        ax.scatter(3451,-2,c = 'blue',marker = 's')
        ax.scatter(4501,-2,c = 'blue',marker = 's')
    ax.title.set_text('Average PPR')
    ax.set_xlabel('Time (in ms)')
    ax.set_ylabel('PSP Amplitude (in mV)')
    if User_choices['PPRGraph'] == 'Yes':
        plt.savefig('SPNPPR.svg',format='svg',dpi=1200)
    plt.show()
    plt.close()

    #Automatically save all indivdiual traces to a txt file
    output = open(str(AllData['filename']) + 'PPR_IndividualTraces_' + str(User_choices['CellVal']) + '.txt', 'w')
    a = csv.writer(output)
    a.writerows(PPRAmp)
    output.close()
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
elif 'Train CC' in Cell['ExptID']:
    #Allows the user to save the average graph, if needed
    User_choices['TrainGraph'] = input('Would you like to save the average/individual trace graph? (Input "Yes" or "No"): ')
    
    #Same NaNing method as SP
    User_choices['Train NaN'] = int(input('If traces need to be NaNed, input 1. Otherwise, input 0: '))
    if User_choices['Train NaN'] == 0:
        print('Continuing to SP Analysis')
    if User_choices['Train NaN'] == 1:
        User_choices['Train_NaN_Trace'] = int(input('Please input the number of traces to be NaNed: '))
        for i in range(User_choices['Train_NaN_Trace']):
            User_choices['Train_Traces'] = int(input('Please input the trace to be Naned from 0 to ' + str(Cell['TraceMax'][1]) + ' : '))
            Cell['Data'][:,User_choices['Train_Traces']] = np.nan
    
    #Set up lists that will save certain values
    Ratio = pd.DataFrame()
    Zero_Trace = []
    PSP_dict = {}
    
    #Calculate the average baseline and zero by subtracting baseline from all values
    for i in range(Cell['TraceMax'][1]):
        baseline = np.nanmean(Cell['Data'][0:20000,i])
        zeroed_trace = Cell['Data'][:,i] - baseline
        Zero_Trace.append(zeroed_trace)
    
    #Calculates maximal PSP value for each of the 25 pulses from each trace and places it into a dictionary
    for i in range(Cell['TraceMax'][1]):
        iterstart = 20000
        iterend = 22000
        PSPlist = []
        for ii in range(25):
            PSP = np.nanmax(Zero_Trace[i][iterstart:iterend])
            PSPlist.append(PSP)
            iterstart += 2000
            iterend += 2000
        PSP_dict[i] = PSPlist
    
    #Convert data into Dataframe to use pandas mean and std functions
    MaxP = pd.DataFrame.from_dict(PSP_dict,orient = 'index')

    #Calculate each pulse as a ratio of P1
    for i in range(25):
        Ratio[i] = MaxP.loc[:,i] / MaxP.loc[:,0]

    #Calculate the average PSP and standard deviation values for each pulse and average train values
    MeanRatio = pd.DataFrame.mean(Ratio)
    StdRatio = pd.DataFrame.std(Ratio)
    AvgTrain = np.nanmean(Cell['Data'], axis = 1)
    AvgTrain = AvgTrain - (np.nanmean(AvgTrain[0:20000]))

    #Plot all traces simultaneously for visualization
    plt.plot(Cell['Time'],Cell['Data'])
    plt.title('All Traces for Cell ' + str(User_choices['CellVal']) + ', Experiment ' + str(User_choices['ExptVal']))
    plt.xlabel('Time (in ms)')
    plt.ylabel('Voltage (in mV)')
    plt.show()

    #Plot average PSP value with shaded standard deviation
    plt.figure()
    plt.plot(MeanRatio, c = 'k')
    plt.fill_between(range(0,25),MeanRatio-StdRatio,MeanRatio+StdRatio, color = 'lightgrey')
    plt.show()
    plt.close()
    
    #plot average train with individual traces
    plt.figure()
    plt.plot(AvgTrain, c = 'k', zorder = 2)
    for i in range(Cell['TraceMax'][1]):
        plt.plot(Zero_Trace[i], c = 'lightgrey',zorder = 1)
        iterate = 20000
    for i in range(25):
        plt.scatter(iterate,-2,c = 'blue', marker = '|')
        iterate += 2000
    if User_choices['TrainGraph'] == 'Yes':
        plt.savefig('SPNTrain.svg',format='svg',dpi=1200)
    plt.show()
    plt.close()

    #Outputs the processed data as a CSV
    with open(str(AllData['filename']) + 'Train_IndividualTraces_' + str(User_choices['CellVal']) + '.txt', 'w') as Train:
        writer = csv.writer(Train)
        writer.writerows(Zero_Trace)
        Train.close()
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
elif 'SP E/I' in Cell['ExptID']:
    #Same NaNing method as SP
    User_choices['EI NaN'] = int(input('If traces need to be NaNed, input 1. Otherwise, input 0: '))
    if User_choices['EI NaN'] == 0:
        print('Continuing to SP E/I Analysis')
    if User_choices['EI NaN'] == 1:
        User_choices['EI_NaN_Trace'] = int(input('Please input the number of traces to be NaNed: '))
        for i in range(User_choices['EI_NaN_Trace']):
            User_choices['EI_Traces'] = int(input('Please input the trace to be Naned from 0 to ' + str(Cell['TraceMax'][1]) + ' : '))
            Cell['Data'][:,User_choices['EI_Traces']] = np.nan
        
    #Set up list to append data zero trace data for average trace calculation
    EI_zeroed = list()
    EI_indamp = list()
    
    #Calculate baseline, max amplitude, and trace values for each sweep
    for i in range(Cell['TraceMax'][1]):
       base = np.nanmean(Cell['Data'][0:4000,i])
       zero_trace = Cell['Data'][:,i] - base
       PSP = np.nanmax(zero_trace[9500:12000])
       EI_zeroed.append(zero_trace)
       EI_indamp.append(PSP)
       
    #Concatenate list of np arrays into a single array to calculate average trace plot
    AvgTrace = np.column_stack(EI_zeroed)
    AvgTrace = np.nanmean(AvgTrace,axis = 1)
    AvgPSP = np.nanmean(EI_indamp)

    plt.plot(Cell['Time'],AvgTrace)
    plt.title('SP E/I Average Trace')
    plt.xlabel('Time (in ms)')
    plt.ylabel('PSP Amplitude (in mV)')
    plt.show()
    
    #Outputs the average trace, indivdiual amplitudes, and average amplitude as a txt file
    np.savetxt(str(AllData['filename']) + '_C' + str(User_choices['CellVal']) + '_EI.txt', EI_indamp)