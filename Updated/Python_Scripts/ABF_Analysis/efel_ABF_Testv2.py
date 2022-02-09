#                EFEL for ABF Formatted Files TEST FILE v2
#                   *Created by AY on 02/09/2022*
#                   *Last Updated on 02/09/2022*
#     *For any issues or bugs, please contact alex.yonk2@gmail.com*
#*This script is designed to plot each sweep to visualize where errors in the main script (ABF_EFELv2) may be occurring

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

    plt.plot(Time,SortedData[:,IterVar])
    plt.show()
    
    IterVar += 1