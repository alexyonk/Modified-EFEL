#                   Multi_SP_Analysis v1.0
#                   *Created by AY on 3/1/2022*
#                   *Last Updated on 3/2/2022*
#     *For any issues or bugs, please contact alex.yonk2@gmail.com*
#*This script will iterate through a single folder and open all files with a certain extension (in this case, *.txt)
#* It calculates various SP parameters and plots a grand average line graph and a bar graph
#* Must be used in conjunction with the Multi_Ephys_Analysis script

#Install/import these libraries
import pandas as pd
from tkinter import filedialog
from matplotlib import pyplot as plt
import numpy as np
from itertools import cycle
import glob
from os import chdir, getcwd

#Allows user to select and set working directory
wd = filedialog.askdirectory()
chdir(wd)

#Cycles through the files looking for a txt extension
files = glob.glob('*.txt')

#Allows the user to input how many text files they want to analyze
CellNum = len(files)
Datadict = {}
Meandict = {}
Maxdict = {}
cycol = cycle('bgrcmy')
cycol2 = cycle('bgrcmy')
Time = np.arange(0,4500,0.05)

#For loop through the number of cells to be loaded in and placing them all in a dictionary
for i in range(CellNum):
    data = pd.read_csv(files[i],index_col = False, header = None)
    data = data.transpose()
    Datadict[i] = data

#Calculates average trace and maximal PSP value for each cell and places into separate dictionaries
for key,values in Datadict.items():
    Avg = Datadict[key]
    Avg = pd.DataFrame.mean(Avg.iloc[:,0:21],axis = 1)
    Max = pd.Series.max(Avg.iloc[9500:12000])
    Meandict[key] = Avg
    Maxdict[key] = Max

#Calculates the mean and std of the maximal values and calculates the average trace
BoxMean = np.mean(list(Maxdict.values()))
BoxStd = np.std(list(Maxdict.values()))
AvgTrace = pd.DataFrame.from_dict(Meandict)
AvgTrace = pd.DataFrame.mean(AvgTrace,axis = 1)

#Calculates 2x the standard deviation of the baseline average trace
#Use 2x standard deviation as noticeable rise indicator
#Calculates maximal trace value for slope analysis
BaseStdDev = 2*(np.std(AvgTrace.loc[0:9500]))
MaxPeak = (np.argmax(AvgTrace.loc[10000:10500]) + 10000)
Rise = (np.argmax(AvgTrace.loc[10000:12000] > BaseStdDev) + 10000)

'''
Potentially change this section to be the first derivative for the latency instead of 2X the std
'''
Latency = (Rise - 10000) * 0.05
Slope = np.polyfit(Time[Rise:MaxPeak+1],AvgTrace.loc[Rise:MaxPeak],1)
FirstDeriv = ((AvgTrace.loc[MaxPeak] - AvgTrace.loc[Rise]) / (Time[MaxPeak] - Time[Rise]))

#Creates a bar graph with the average PSP value and individual data points
SaveGraph = int(input('Would you like to save the bar graph? (Input 0): '))
plt.figure()
plt.bar(1,BoxMean,zorder = 1, color = 'w', edgecolor = 'k')
for i in range(CellNum):
    plt.scatter(1,Maxdict[i], c = next(cycol),zorder = 3)
plt.errorbar(1,BoxMean,yerr = BoxStd, c = 'k', capsize = 5,zorder = 2)
#plt.ylim([0,20])
plt.xlim([0,2])
if SaveGraph == 0:
    plt.savefig('PVSPBar.svg',format = 'svg',dpi = 1200)
plt.show()
plt.close()

#Creates a line graph detailing the grand average trace and average individual traces
SaveGraph2 = int(input('Would you like to save the average trace graph? (Input 0): '))
plt.figure()
plt.plot(AvgTrace[9500:12000], c ='k',linewidth = 5)
for i in range(CellNum):
    plt.plot(Meandict[i][9500:12000],c = next(cycol2))
plt.scatter(10000,-2,c = 'blue', marker = '|')
#plt.ylim([0,16])
if SaveGraph2 == 0:
    plt.savefig('PVSPLine.svg',format = 'svg',dpi = 1200)
plt.show()
plt.close()

print('The maximal PSP value is ' + str(float(BoxMean)) + ' mV.')
print('The latency to rise is ' + str(float(Latency)) + ' ms.')
print('The subthreshold slope rise is ' + str(float(Slope[0])))
print('The first derivative is ' + str(float(FirstDeriv)))