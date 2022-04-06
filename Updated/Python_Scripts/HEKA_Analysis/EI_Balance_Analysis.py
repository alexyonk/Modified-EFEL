#              E:I Balance Analysis
#          *Created by AY on 1/19/2022*
#           *Last Updated on 2/10/2022*
#     *For any issues or bugs, please contact alex.yonk2@gmail.com*
#*This script was designed to analyze the excitatory:inhibitory (E:I) balance
#*It must be used in conjunction with the Multi_Ephys_Analysis script output
#* Requires both the SP CC and the SP E/I text file outputs

#Install/import these libraries
import pandas as pd
from tkinter import filedialog
from os import chdir, getcwd

#Allows user to set working directory
wd = filedialog.askdirectory()
chdir(wd)

#Opens dialog boxes allowing the user to select and load files into separate dataframes
#NOTE = MUST READ IN THE PRE SP FIRST AND THE SP E/I SECOND
Pre_filepath = filedialog.askopenfilename()
Pre_Data = pd.read_csv(Pre_filepath, index_col = False, header = None)
Post_filepath = filedialog.askopenfilename()
Post_Data = pd.read_csv(Post_filepath, index_col = False, header = None)

#Calculate the average PSP for pre- and post-bicuculline
Pre_Avg = float(Pre_Data.mean())
Post_Avg = float(Post_Data.mean())

#Calculate the E and I components
#E = Max PSP amplitude with bicuculline
#I = Difference between Max PSP amplitude with bicuculline and Max PSP amplitude without bicuculline
E = Post_Avg
I = Post_Avg - Pre_Avg

#Calculate the E:I Balance via the Milstein Formula: E / (E + I)
EI_Bal = (E / (E + I))