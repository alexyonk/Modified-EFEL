#                   Multi_Train_Analysis v1.0
#                   *Created by AY on 3/1/2022*
#                   *Last Updated on 3/2/2022*
#     *For any issues or bugs, please contact alex.yonk2@gmail.com*
#*This script will iterate through a single folder and open all files with a certain extension (in this case, *.txt)
#* It calculates various Train parameters and plots a grand average line graph and a shaded graph
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
    data = pd.read_csv(files[i],index_col = False, header = None).transpose()
    Datadict[i] = data

#Calculates average trace and maximal PSP value for each cell and places into separate dictionaries
for key,values in Datadict.items():
    Avg = Datadict[key]
    Avg = pd.DataFrame.mean(Avg.iloc[:,0:5],axis = 1)
    Meandict[key] = Avg
    iterstart = 20000
    endstart = 22000
    Maxlist = []
    for i in range(25):
        Max = pd.Series.max(Avg.iloc[iterstart:endstart])
        Maxlist.append(Max)
        iterstart += 2000
        endstart += 2000
    Maxdict[key] = Maxlist

#Merge pulse values from each cell together and calculate mean and std
MaxP = pd.DataFrame.from_dict(Maxdict,orient = 'index')
AvgTrace = pd.DataFrame.from_dict(Meandict)
AvgTrace = pd.DataFrame.mean(AvgTrace,axis = 1)

#Calculates each pulse as a ratio of P1
for i in range(25):
    Ratio[i] = MaxP.loc[:,i] / MaxP.loc[:,0]

#Calculate average PSP and standard deviation value for each pulse
MeanRatio = pd.DataFrame.mean(Ratio)
StdRatio = pd.DataFrame.std(Ratio)

#Plot average PSP value with shaded standard deviation
SaveGraph1 = int(input('Would you like to save the shaded graph? (Input 0): '))
plt.figure()
plt.plot(MeanRatio, c = 'k')
plt.fill_between(range(0,25),MeanRatio-StdRatio,MeanRatio+StdRatio, color = 'lightgrey')
#plt.ylim([0.3,1.6])
if SaveGraph1 == 0:
    plt.savefig('PVTrainShade.svg',format = 'svg',dpi = 1200)
plt.show()
plt.close()

#Creates a line graph detailing the grand average trace and average individual traces
SaveGraph2 = int(input('Would you like to save the average trace graph? (Input 0): '))
plt.figure()
iterate = 20000
plt.plot(AvgTrace, c ='k',linewidth = 3,zorder = 2)
for i in range(CellNum):
    plt.plot(Meandict[i],c = next(cycol2), linewidth = 0.5, zorder = 1)
for i in range(25):
    plt.scatter(iterate,-2,c = 'blue', marker = '|')
    iterate += 2000
#plt.ylim([0,18])
if SaveGraph2 == 0:
    plt.savefig('PVTrainLine.svg',format = 'svg',dpi = 1200)
plt.show()
plt.close()