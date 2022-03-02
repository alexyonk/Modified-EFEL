#                   Multi_PPR_Analysis v1.0
#                   *Created by AY on 3/1/2022*
#                   *Last Updated on 3/2/2022*
#     *For any issues or bugs, please contact alex.yonk2@gmail.com*
#*This script will iterate through a single folder and open all files with a certain extension (in this case, *.txt)
#* It calculates various PPR parameters and plots a grand average line graph and a boxplot graph
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
MaxP = {}
Ratio = pd.DataFrame()
cycol = cycle('bgrcmy')
cycol2 = cycle('bgrcmy')

#For loop through the number of cells to be loaded in and placing them all in a dictionary
for i in range(CellNum):
    data = pd.read_csv(files[i],index_col = False, header = None)
    Datadict[i] = data

#Calculates average trace and maximal PSP value for each cell and places into separate dictionaries
for key,values in Datadict.items():
    Avg = Datadict[key]
    Avg = pd.DataFrame.mean(Avg.iloc[:,0:21],axis = 1)
    Meandict[key] = Avg
    iterstart = 4001
    endstart = 5100
    Maxlist = []
    for i in range(5):
        Max = pd.Series.max(Avg.iloc[iterstart:endstart])
        Maxlist.append(Max)
        iterstart += 1100
        endstart += 1100
    Maxdict[key] = Maxlist

#Merge pulse values from each cell together and calculate mean and std
MaxP = pd.DataFrame.from_dict(Maxdict,orient = 'index')
AvgTrace = pd.DataFrame.from_dict(Meandict)
AvgTrace = pd.DataFrame.mean(AvgTrace,axis = 1)

#Calculates 2x the standard deviation of the baseline average trace
#Use 2x standard deviation as noticeable rise indicator
BaseStdDev = 2*(np.std(AvgTrace.loc[0:3500]))
Rise = (np.argmax(AvgTrace.loc[4000:5000] > BaseStdDev) + 4000)
Latency = (Rise - 4000) * 0.05

#Calculates each pulse as a ratio of P1
for i in range(5):
    Ratio[i] = MaxP.loc[:,i] / MaxP.loc[:,0]

#Creates boxplot with individual data points matching the grand average trace graph
SaveGraph1 = int(input('Would you like to save the boxplot graph? (Input 0): '))
plt.figure()
plt.boxplot(Ratio)
for i in range(CellNum):
    plt.plot(range(1,6),Ratio.loc[i,:], c = next(cycol),ls = '-', marker = 'o')
#plt.ylim([0,2])
if SaveGraph1 == 0:
    plt.savefig('PVPPRBox.svg', format = 'svg',dpi = 1200)
plt.show()

#Creates a line graph detailing the grand average trace and average individual traces
SaveGraph2 = int(input('Would you like to save the average trace graph? (Input 0): '))
plt.figure()
iterate = 4000
plt.plot(AvgTrace, c ='k',linewidth = 3,zorder = 2)
for i in range(CellNum):
    plt.plot(Meandict[i],c = next(cycol2), linewidth = 0.5, zorder = 1)
for i in range(5):
    plt.scatter(iterate,-2,c = 'blue', marker = '|')
    iterate += 1050
#plt.ylim([0,18])
if SaveGraph2 == 0:
    plt.savefig('PVPPRLine.svg',format = 'svg',dpi = 1200)
plt.show()
plt.close()

print('The latency to rise is ' + str(float(Latency)) + ' ms.')