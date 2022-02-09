#Install and Import these scripts
import scipy.io
from scipy import stats
import efel
import numpy as np
from tkinter import filedialog
from matplotlib import pyplot as plt
from csv import DictWriter
import csv

#Enable EFEL Settings
efel.setDoubleSetting('interp_step',0.05) #Must be set to the sampling rate (20,000 Hz = 0.05)
efel.setDoubleSetting('voltage_base_start_perc',0.1)
efel.setDoubleSetting('voltage_base_end_perc',0.8)
efel.setDerivativeThreshold(10) #Value can be changed, but normally set to 10
efel.setThreshold(10)

#Create global variable to store parameter information
Results = list()
trace_calc = dict()
Data = dict()
User_choices = dict()

#Opens a dialog box allowing the user to select the file and removes the extension from the file name & load in the file
file_path = filedialog.askopenfilename()
mat = scipy.io.loadmat(file_path,struct_as_record = False,squeeze_me = True)
file = mat['filename']

#Describe the number of cells present in the file
print('There are *** ' +str(int(mat['Data'].CellNum)) + ' *** cells in this file.')

#Allows user to choose which cell they want to analyze
User_choices['CellVal'] = int(input('Which cell would you like to analyze?: '))

#Allows user to choose which experiment they want to analyze
if User_choices['CellVal'] == 1:
    print('There are *** ' + str(int(mat['Data'].Cell1.Expts)) + ' *** experiments for this cell.' + '\n')
    if mat['Data'].Cell1.Expts == 1:
        rows,cols1 = mat['Data'].Cell1.Exp1.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
    elif mat['Data'].Cell1.Expts == 2:
        rows,cols1 = mat['Data'].Cell1.Exp1.shape
        rows,cols2 = mat['Data'].Cell1.Exp2.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
    elif mat['Data'].Cell1.Expts == 3:
        rows,cols1 = mat['Data'].Cell1.Exp1.shape
        rows,cols2 = mat['Data'].Cell1.Exp2.shape
        rows,cols3 = mat['Data'].Cell1.Exp3.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
    elif mat['Data'].Cell1.Expts == 4:
        rows,cols1 = mat['Data'].Cell1.Exp1.shape
        rows,cols2 = mat['Data'].Cell1.Exp2.shape
        rows,cols3 = mat['Data'].Cell1.Exp3.shape
        rows,cols4 = mat['Data'].Cell1.Exp4.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
    elif mat['Data'].Cell1.Expts == 5:
        rows,cols1 = mat['Data'].Cell1.Exp1.shape
        rows,cols2 = mat['Data'].Cell1.Exp2.shape
        rows,cols3 = mat['Data'].Cell1.Exp3.shape
        rows,cols4 = mat['Data'].Cell1.Exp4.shape
        rows,cols5 = mat['Data'].Cell1.Exp5.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
    elif mat['Data'].Cell1.Expts == 6:
        rows,cols1 = mat['Data'].Cell1.Exp1.shape
        rows,cols2 = mat['Data'].Cell1.Exp2.shape
        rows,cols3 = mat['Data'].Cell1.Exp3.shape
        rows,cols4 = mat['Data'].Cell1.Exp4.shape
        rows,cols5 = mat['Data'].Cell1.Exp5.shape
        rows,cols6 = mat['Data'].Cell1.Exp6.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
    elif mat['Data'].Cell1.Expts == 7:
        rows,cols1 = mat['Data'].Cell1.Exp1.shape
        rows,cols2 = mat['Data'].Cell1.Exp2.shape
        rows,cols3 = mat['Data'].Cell1.Exp3.shape
        rows,cols4 = mat['Data'].Cell1.Exp4.shape
        rows,cols5 = mat['Data'].Cell1.Exp5.shape
        rows,cols6 = mat['Data'].Cell1.Exp6.shape
        rows,cols7 = mat['Data'].Cell1.Exp7.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')        
    elif mat['Data'].Cell1.Expts == 8:   
        rows,cols1 = mat['Data'].Cell1.Exp1.shape
        rows,cols2 = mat['Data'].Cell1.Exp2.shape
        rows,cols3 = mat['Data'].Cell1.Exp3.shape
        rows,cols4 = mat['Data'].Cell1.Exp4.shape
        rows,cols5 = mat['Data'].Cell1.Exp5.shape
        rows,cols6 = mat['Data'].Cell1.Exp6.shape
        rows,cols7 = mat['Data'].Cell1.Exp7.shape
        rows,cols8 = mat['Data'].Cell1.Exp8.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
    elif mat['Data'].Cell1.Expts == 9:
        rows,cols1 = mat['Data'].Cell1.Exp1.shape
        rows,cols2 = mat['Data'].Cell1.Exp2.shape
        rows,cols3 = mat['Data'].Cell1.Exp3.shape
        rows,cols4 = mat['Data'].Cell1.Exp4.shape
        rows,cols5 = mat['Data'].Cell1.Exp5.shape
        rows,cols6 = mat['Data'].Cell1.Exp6.shape
        rows,cols7 = mat['Data'].Cell1.Exp7.shape
        rows,cols8 = mat['Data'].Cell1.Exp8.shape
        rows,cols9 = mat['Data'].Cell1.Exp9.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
    elif mat['Data'].Cell1.Expts == 10:        
        rows,cols1 = mat['Data'].Cell1.Exp1.shape
        rows,cols2 = mat['Data'].Cell1.Exp2.shape
        rows,cols3 = mat['Data'].Cell1.Exp3.shape
        rows,cols4 = mat['Data'].Cell1.Exp4.shape
        rows,cols5 = mat['Data'].Cell1.Exp5.shape
        rows,cols6 = mat['Data'].Cell1.Exp6.shape
        rows,cols7 = mat['Data'].Cell1.Exp7.shape
        rows,cols8 = mat['Data'].Cell1.Exp8.shape
        rows,cols9 = mat['Data'].Cell1.Exp9.shape
        rows,cols10 = mat['Data'].Cell1.Exp10.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
    elif mat['Data'].Cell1.Expts == 11:        
        rows,cols1 = mat['Data'].Cell1.Exp1.shape
        rows,cols2 = mat['Data'].Cell1.Exp2.shape
        rows,cols3 = mat['Data'].Cell1.Exp3.shape
        rows,cols4 = mat['Data'].Cell1.Exp4.shape
        rows,cols5 = mat['Data'].Cell1.Exp5.shape
        rows,cols6 = mat['Data'].Cell1.Exp6.shape
        rows,cols7 = mat['Data'].Cell1.Exp7.shape
        rows,cols8 = mat['Data'].Cell1.Exp8.shape
        rows,cols9 = mat['Data'].Cell1.Exp9.shape
        rows,cols10 = mat['Data'].Cell1.Exp10.shape
        rows,cols11 = mat['Data'].Cell1.Exp11.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
    elif mat['Data'].Cell1.Expts == 12:
        rows,cols1 = mat['Data'].Cell1.Exp1.shape
        rows,cols2 = mat['Data'].Cell1.Exp2.shape
        rows,cols3 = mat['Data'].Cell1.Exp3.shape
        rows,cols4 = mat['Data'].Cell1.Exp4.shape
        rows,cols5 = mat['Data'].Cell1.Exp5.shape
        rows,cols6 = mat['Data'].Cell1.Exp6.shape
        rows,cols7 = mat['Data'].Cell1.Exp7.shape
        rows,cols8 = mat['Data'].Cell1.Exp8.shape
        rows,cols9 = mat['Data'].Cell1.Exp9.shape
        rows,cols10 = mat['Data'].Cell1.Exp10.shape
        rows,cols11 = mat['Data'].Cell1.Exp11.shape
        rows,cols12 = mat['Data'].Cell1.Exp12.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
    elif mat['Data'].Cell1.Expts == 13:
        rows,cols1 = mat['Data'].Cell1.Exp1.shape
        rows,cols2 = mat['Data'].Cell1.Exp2.shape
        rows,cols3 = mat['Data'].Cell1.Exp3.shape
        rows,cols4 = mat['Data'].Cell1.Exp4.shape
        rows,cols5 = mat['Data'].Cell1.Exp5.shape
        rows,cols6 = mat['Data'].Cell1.Exp6.shape
        rows,cols7 = mat['Data'].Cell1.Exp7.shape
        rows,cols8 = mat['Data'].Cell1.Exp8.shape
        rows,cols9 = mat['Data'].Cell1.Exp9.shape
        rows,cols10 = mat['Data'].Cell1.Exp10.shape
        rows,cols11 = mat['Data'].Cell1.Exp11.shape
        rows,cols12 = mat['Data'].Cell1.Exp12.shape
        rows,cols13 = mat['Data'].Cell1.Exp13.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
    elif mat['Data'].Cell1.Expts == 14:
        rows,cols1 = mat['Data'].Cell1.Exp1.shape
        rows,cols2 = mat['Data'].Cell1.Exp2.shape
        rows,cols3 = mat['Data'].Cell1.Exp3.shape
        rows,cols4 = mat['Data'].Cell1.Exp4.shape
        rows,cols5 = mat['Data'].Cell1.Exp5.shape
        rows,cols6 = mat['Data'].Cell1.Exp6.shape
        rows,cols7 = mat['Data'].Cell1.Exp7.shape
        rows,cols8 = mat['Data'].Cell1.Exp8.shape
        rows,cols9 = mat['Data'].Cell1.Exp9.shape
        rows,cols10 = mat['Data'].Cell1.Exp10.shape
        rows,cols11 = mat['Data'].Cell1.Exp11.shape
        rows,cols12 = mat['Data'].Cell1.Exp12.shape
        rows,cols13 = mat['Data'].Cell1.Exp13.shape
        rows,cols14 = mat['Data'].Cell1.Exp14.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
        print('Experiment ' + str(14) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID14) + ' contains *** ' + str(int(cols14)) + ' *** traces.')
    elif mat['Data'].Cell1.Expts == 15:
        rows,cols1 = mat['Data'].Cell1.Exp1.shape
        rows,cols2 = mat['Data'].Cell1.Exp2.shape
        rows,cols3 = mat['Data'].Cell1.Exp3.shape
        rows,cols4 = mat['Data'].Cell1.Exp4.shape
        rows,cols5 = mat['Data'].Cell1.Exp5.shape
        rows,cols6 = mat['Data'].Cell1.Exp6.shape
        rows,cols7 = mat['Data'].Cell1.Exp7.shape
        rows,cols8 = mat['Data'].Cell1.Exp8.shape
        rows,cols9 = mat['Data'].Cell1.Exp9.shape
        rows,cols10 = mat['Data'].Cell1.Exp10.shape
        rows,cols11 = mat['Data'].Cell1.Exp11.shape
        rows,cols12 = mat['Data'].Cell1.Exp12.shape
        rows,cols13 = mat['Data'].Cell1.Exp13.shape
        rows,cols14 = mat['Data'].Cell1.Exp14.shape
        rows,cols15 = mat['Data'].Cell1.Exp15.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
        print('Experiment ' + str(14) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID14) + ' contains *** ' + str(int(cols14)) + ' *** traces.')
        print('Experiment ' + str(15) + ' is a(n) ' + str(mat['Data'].Cell1.ExptID15) + ' contains *** ' + str(int(cols15)) + ' *** traces.')
    User_choices['ExptVal'] = int(input('Which experiment would you like to analyze: '))
        
if User_choices['CellVal'] == 2:
    print('There are *** ' +str(int(mat['Data'].Cell2.Expts)) + ' *** experiments for this cell.')
    if mat['Data'].Cell2.Expts == 1:
        rows,cols1 = mat['Data'].Cell2.Exp1.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
    elif mat['Data'].Cell2.Expts == 2:
        rows,cols1 = mat['Data'].Cell2.Exp1.shape
        rows,cols2 = mat['Data'].Cell2.Exp2.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
    elif mat['Data'].Cell2.Expts == 3:
        rows,cols1 = mat['Data'].Cell2.Exp1.shape
        rows,cols2 = mat['Data'].Cell2.Exp2.shape
        rows,cols3 = mat['Data'].Cell2.Exp3.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
    elif mat['Data'].Cell2.Expts == 4:
        rows,cols1 = mat['Data'].Cell2.Exp1.shape
        rows,cols2 = mat['Data'].Cell2.Exp2.shape
        rows,cols3 = mat['Data'].Cell2.Exp3.shape
        rows,cols4 = mat['Data'].Cell2.Exp4.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
    elif mat['Data'].Cell2.Expts == 5:
        rows,cols1 = mat['Data'].Cell2.Exp1.shape
        rows,cols2 = mat['Data'].Cell2.Exp2.shape
        rows,cols3 = mat['Data'].Cell2.Exp3.shape
        rows,cols4 = mat['Data'].Cell2.Exp4.shape
        rows,cols5 = mat['Data'].Cell2.Exp5.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
    elif mat['Data'].Cell2.Expts == 6:
        rows,cols1 = mat['Data'].Cell2.Exp1.shape
        rows,cols2 = mat['Data'].Cell2.Exp2.shape
        rows,cols3 = mat['Data'].Cell2.Exp3.shape
        rows,cols4 = mat['Data'].Cell2.Exp4.shape
        rows,cols5 = mat['Data'].Cell2.Exp5.shape
        rows,cols6 = mat['Data'].Cell2.Exp6.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
    elif mat['Data'].Cell2.Expts == 7:
        rows,cols1 = mat['Data'].Cell2.Exp1.shape
        rows,cols2 = mat['Data'].Cell2.Exp2.shape
        rows,cols3 = mat['Data'].Cell2.Exp3.shape
        rows,cols4 = mat['Data'].Cell2.Exp4.shape
        rows,cols5 = mat['Data'].Cell2.Exp5.shape
        rows,cols6 = mat['Data'].Cell2.Exp6.shape
        rows,cols7 = mat['Data'].Cell2.Exp7.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')        
    elif mat['Data'].Cell2.Expts == 8:
        rows,cols1 = mat['Data'].Cell2.Exp1.shape
        rows,cols2 = mat['Data'].Cell2.Exp2.shape
        rows,cols3 = mat['Data'].Cell2.Exp3.shape
        rows,cols4 = mat['Data'].Cell2.Exp4.shape
        rows,cols5 = mat['Data'].Cell2.Exp5.shape
        rows,cols6 = mat['Data'].Cell2.Exp6.shape
        rows,cols7 = mat['Data'].Cell2.Exp7.shape
        rows,cols8 = mat['Data'].Cell2.Exp8.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
    elif mat['Data'].Cell2.Expts == 9:
        rows,cols1 = mat['Data'].Cell2.Exp1.shape
        rows,cols2 = mat['Data'].Cell2.Exp2.shape
        rows,cols3 = mat['Data'].Cell2.Exp3.shape
        rows,cols4 = mat['Data'].Cell2.Exp4.shape
        rows,cols5 = mat['Data'].Cell2.Exp5.shape
        rows,cols6 = mat['Data'].Cell2.Exp6.shape
        rows,cols7 = mat['Data'].Cell2.Exp7.shape
        rows,cols8 = mat['Data'].Cell2.Exp8.shape
        rows,cols9 = mat['Data'].Cell2.Exp9.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
    elif mat['Data'].Cell2.Expts == 10:        
        rows,cols1 = mat['Data'].Cell2.Exp1.shape
        rows,cols2 = mat['Data'].Cell2.Exp2.shape
        rows,cols3 = mat['Data'].Cell2.Exp3.shape
        rows,cols4 = mat['Data'].Cell2.Exp4.shape
        rows,cols5 = mat['Data'].Cell2.Exp5.shape
        rows,cols6 = mat['Data'].Cell2.Exp6.shape
        rows,cols7 = mat['Data'].Cell2.Exp7.shape
        rows,cols8 = mat['Data'].Cell2.Exp8.shape
        rows,cols9 = mat['Data'].Cell2.Exp9.shape
        rows,cols10 = mat['Data'].Cell2.Exp10.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
    elif mat['Data'].Cell2.Expts == 11:        
        rows,cols1 = mat['Data'].Cell2.Exp1.shape
        rows,cols2 = mat['Data'].Cell2.Exp2.shape
        rows,cols3 = mat['Data'].Cell2.Exp3.shape
        rows,cols4 = mat['Data'].Cell2.Exp4.shape
        rows,cols5 = mat['Data'].Cell2.Exp5.shape
        rows,cols6 = mat['Data'].Cell2.Exp6.shape
        rows,cols7 = mat['Data'].Cell2.Exp7.shape
        rows,cols8 = mat['Data'].Cell2.Exp8.shape
        rows,cols9 = mat['Data'].Cell2.Exp9.shape
        rows,cols10 = mat['Data'].Cell2.Exp10.shape
        rows,cols11 = mat['Data'].Cell2.Exp11.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
    elif mat['Data'].Cell2.Expts == 12:
        rows,cols1 = mat['Data'].Cell2.Exp1.shape
        rows,cols2 = mat['Data'].Cell2.Exp2.shape
        rows,cols3 = mat['Data'].Cell2.Exp3.shape
        rows,cols4 = mat['Data'].Cell2.Exp4.shape
        rows,cols5 = mat['Data'].Cell2.Exp5.shape
        rows,cols6 = mat['Data'].Cell2.Exp6.shape
        rows,cols7 = mat['Data'].Cell2.Exp7.shape
        rows,cols8 = mat['Data'].Cell2.Exp8.shape
        rows,cols9 = mat['Data'].Cell2.Exp9.shape
        rows,cols10 = mat['Data'].Cell2.Exp10.shape
        rows,cols11 = mat['Data'].Cell2.Exp11.shape
        rows,cols12 = mat['Data'].Cell2.Exp12.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
    elif mat['Data'].Cell2.Expts == 13:
        rows,cols1 = mat['Data'].Cell2.Exp1.shape
        rows,cols2 = mat['Data'].Cell2.Exp2.shape
        rows,cols3 = mat['Data'].Cell2.Exp3.shape
        rows,cols4 = mat['Data'].Cell2.Exp4.shape
        rows,cols5 = mat['Data'].Cell2.Exp5.shape
        rows,cols6 = mat['Data'].Cell2.Exp6.shape
        rows,cols7 = mat['Data'].Cell2.Exp7.shape
        rows,cols8 = mat['Data'].Cell2.Exp8.shape
        rows,cols9 = mat['Data'].Cell2.Exp9.shape
        rows,cols10 = mat['Data'].Cell2.Exp10.shape
        rows,cols11 = mat['Data'].Cell2.Exp11.shape
        rows,cols12 = mat['Data'].Cell2.Exp12.shape
        rows,cols13 = mat['Data'].Cell2.Exp13.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
    elif mat['Data'].Cell2.Expts == 14:
        rows,cols1 = mat['Data'].Cell2.Exp1.shape
        rows,cols2 = mat['Data'].Cell2.Exp2.shape
        rows,cols3 = mat['Data'].Cell2.Exp3.shape
        rows,cols4 = mat['Data'].Cell2.Exp4.shape
        rows,cols5 = mat['Data'].Cell2.Exp5.shape
        rows,cols6 = mat['Data'].Cell2.Exp6.shape
        rows,cols7 = mat['Data'].Cell2.Exp7.shape
        rows,cols8 = mat['Data'].Cell2.Exp8.shape
        rows,cols9 = mat['Data'].Cell2.Exp9.shape
        rows,cols10 = mat['Data'].Cell2.Exp10.shape
        rows,cols11 = mat['Data'].Cell2.Exp11.shape
        rows,cols12 = mat['Data'].Cell2.Exp12.shape
        rows,cols13 = mat['Data'].Cell2.Exp13.shape
        rows,cols14 = mat['Data'].Cell2.Exp14.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
        print('Experiment ' + str(14) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID14) + ' contains *** ' + str(int(cols14)) + ' *** traces.')
    elif mat['Data'].Cell2.Expts == 15:
        rows,cols1 = mat['Data'].Cell2.Exp1.shape
        rows,cols2 = mat['Data'].Cell2.Exp2.shape
        rows,cols3 = mat['Data'].Cell2.Exp3.shape
        rows,cols4 = mat['Data'].Cell2.Exp4.shape
        rows,cols5 = mat['Data'].Cell2.Exp5.shape
        rows,cols6 = mat['Data'].Cell2.Exp6.shape
        rows,cols7 = mat['Data'].Cell2.Exp7.shape
        rows,cols8 = mat['Data'].Cell2.Exp8.shape
        rows,cols9 = mat['Data'].Cell2.Exp9.shape
        rows,cols10 = mat['Data'].Cell2.Exp10.shape
        rows,cols11 = mat['Data'].Cell2.Exp11.shape
        rows,cols12 = mat['Data'].Cell2.Exp12.shape
        rows,cols13 = mat['Data'].Cell2.Exp13.shape
        rows,cols14 = mat['Data'].Cell2.Exp14.shape
        rows,cols15 = mat['Data'].Cell2.Exp15.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
        print('Experiment ' + str(14) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID14) + ' contains *** ' + str(int(cols14)) + ' *** traces.')
        print('Experiment ' + str(15) + ' is a(n) ' + str(mat['Data'].Cell2.ExptID15) + ' contains *** ' + str(int(cols15)) + ' *** traces.')
    User_choices['ExptVal'] = int(input('Which experiment would you like to analyze?:'))

if User_choices['CellVal'] == 3:
    print('There are *** ' +str(int(mat['Data'].Cell3.Expts)) + ' *** experiments for this cell.')
    if mat['Data'].Cell3.Expts == 1:
        rows,cols1 = mat['Data'].Cell3.Exp1.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
    elif mat['Data'].Cell3.Expts == 2:
        rows,cols1 = mat['Data'].Cell3.Exp1.shape
        rows,cols2 = mat['Data'].Cell3.Exp2.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
    elif mat['Data'].Cell3.Expts == 3:
        rows,cols1 = mat['Data'].Cell3.Exp1.shape
        rows,cols2 = mat['Data'].Cell3.Exp2.shape
        rows,cols3 = mat['Data'].Cell3.Exp3.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
    elif mat['Data'].Cell3.Expts == 4:
        rows,cols1 = mat['Data'].Cell3.Exp1.shape
        rows,cols2 = mat['Data'].Cell3.Exp2.shape
        rows,cols3 = mat['Data'].Cell3.Exp3.shape
        rows,cols4 = mat['Data'].Cell4.Exp4.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
    elif mat['Data'].Cell3.Expts == 5:
        rows,cols1= mat['Data'].Cell3.Exp1.shape
        rows,cols2 = mat['Data'].Cell3.Exp2.shape
        rows,cols3 = mat['Data'].Cell3.Exp3.shape
        rows,cols4 = mat['Data'].Cell3.Exp4.shape
        rows,cols5 = mat['Data'].Cell3.Exp5.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
    elif mat['Data'].Cell3.Expts == 6:
        rows,cols1 = mat['Data'].Cell3.Exp1.shape
        rows,cols2 = mat['Data'].Cell3.Exp2.shape
        rows,cols3 = mat['Data'].Cell3.Exp3.shape
        rows,cols4 = mat['Data'].Cell3.Exp4.shape
        rows,cols5 = mat['Data'].Cell3.Exp5.shape
        rows,cols6 = mat['Data'].Cell3.Exp6.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
    elif mat['Data'].Cell3.Expts == 7:
        rows,cols1 = mat['Data'].Cell3.Exp1.shape
        rows,cols2 = mat['Data'].Cell3.Exp2.shape
        rows,cols3 = mat['Data'].Cell3.Exp3.shape
        rows,cols4 = mat['Data'].Cell3.Exp4.shape
        rows,cols5 = mat['Data'].Cell3.Exp5.shape
        rows,cols6 = mat['Data'].Cell3.Exp6.shape
        rows,cols7 = mat['Data'].Cell3.Exp7.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')        
    elif mat['Data'].Cell3.Expts == 8:
        rows,cols1 = mat['Data'].Cell3.Exp1.shape
        rows,cols2 = mat['Data'].Cell3.Exp2.shape
        rows,cols3 = mat['Data'].Cell3.Exp3.shape
        rows,cols4 = mat['Data'].Cell3.Exp4.shape
        rows,cols5 = mat['Data'].Cell3.Exp5.shape
        rows,cols6 = mat['Data'].Cell3.Exp6.shape
        rows,cols7 = mat['Data'].Cell3.Exp7.shape
        rows,cols8 = mat['Data'].Cell3.Exp8.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
    elif mat['Data'].Cell3.Expts == 9:
        rows,cols1 = mat['Data'].Cell3.Exp1.shape
        rows,cols2 = mat['Data'].Cell3.Exp2.shape
        rows,cols3 = mat['Data'].Cell3.Exp3.shape
        rows,cols4 = mat['Data'].Cell3.Exp4.shape
        rows,cols5 = mat['Data'].Cell3.Exp5.shape
        rows,cols6 = mat['Data'].Cell3.Exp6.shape
        rows,cols7 = mat['Data'].Cell3.Exp7.shape
        rows,cols8 = mat['Data'].Cell3.Exp8.shape
        rows,cols9 = mat['Data'].Cell3.Exp9.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
    elif mat['Data'].Cell3.Expts == 10:        
        rows,cols1 = mat['Data'].Cell3.Exp1.shape
        rows,cols2 = mat['Data'].Cell3.Exp2.shape
        rows,cols3 = mat['Data'].Cell3.Exp3.shape
        rows,cols4 = mat['Data'].Cell3.Exp4.shape
        rows,cols5 = mat['Data'].Cell3.Exp5.shape
        rows,cols6 = mat['Data'].Cell3.Exp6.shape
        rows,cols7 = mat['Data'].Cell3.Exp7.shape
        rows,cols8 = mat['Data'].Cell3.Exp8.shape
        rows,cols9 = mat['Data'].Cell3.Exp9.shape
        rows,cols10 = mat['Data'].Cell3.Exp10.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
    elif mat['Data'].Cell3.Expts == 11:        
        rows,cols1 = mat['Data'].Cell3.Exp1.shape
        rows,cols2 = mat['Data'].Cell3.Exp2.shape
        rows,cols3 = mat['Data'].Cell3.Exp3.shape
        rows,cols4 = mat['Data'].Cell3.Exp4.shape
        rows,cols5 = mat['Data'].Cell3.Exp5.shape
        rows,cols6 = mat['Data'].Cell3.Exp6.shape
        rows,cols7 = mat['Data'].Cell3.Exp7.shape
        rows,cols8 = mat['Data'].Cell3.Exp8.shape
        rows,cols9 = mat['Data'].Cell3.Exp9.shape
        rows,cols10 = mat['Data'].Cell3.Exp10.shape
        rows,cols11 = mat['Data'].Cell3.Exp11.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
    elif mat['Data'].Cell3.Expts == 12:
        rows,cols1 = mat['Data'].Cell3.Exp1.shape
        rows,cols2 = mat['Data'].Cell3.Exp2.shape
        rows,cols3 = mat['Data'].Cell3.Exp3.shape
        rows,cols4 = mat['Data'].Cell3.Exp4.shape
        rows,cols5 = mat['Data'].Cell3.Exp5.shape
        rows,cols6 = mat['Data'].Cell3.Exp6.shape
        rows,cols7 = mat['Data'].Cell3.Exp7.shape
        rows,cols8 = mat['Data'].Cell3.Exp8.shape
        rows,cols9 = mat['Data'].Cell3.Exp9.shape
        rows,cols10 = mat['Data'].Cell3.Exp10.shape
        rows,cols11 = mat['Data'].Cell3.Exp11.shape
        rows,cols12 = mat['Data'].Cell3.Exp12.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
    elif mat['Data'].Cell3.Expts == 13:
        rows,cols1 = mat['Data'].Cell3.Exp1.shape
        rows,cols2 = mat['Data'].Cell3.Exp2.shape
        rows,cols3 = mat['Data'].Cell3.Exp3.shape
        rows,cols4 = mat['Data'].Cell3.Exp4.shape
        rows,cols5 = mat['Data'].Cell3.Exp5.shape
        rows,cols6 = mat['Data'].Cell3.Exp6.shape
        rows,cols7 = mat['Data'].Cell3.Exp7.shape
        rows,cols8 = mat['Data'].Cell3.Exp8.shape
        rows,cols9 = mat['Data'].Cell3.Exp9.shape
        rows,cols10 = mat['Data'].Cell3.Exp10.shape
        rows,cols11 = mat['Data'].Cell3.Exp11.shape
        rows,cols12 = mat['Data'].Cell3.Exp12.shape
        rows,cols13 = mat['Data'].Cell3.Exp13.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
    elif mat['Data'].Cell3.Expts == 14:
        rows,cols1 = mat['Data'].Cell3.Exp1.shape
        rows,cols2 = mat['Data'].Cell3.Exp2.shape
        rows,cols3 = mat['Data'].Cell3.Exp3.shape
        rows,cols4 = mat['Data'].Cell3.Exp4.shape
        rows,cols5 = mat['Data'].Cell3.Exp5.shape
        rows,cols6 = mat['Data'].Cell3.Exp6.shape
        rows,cols7 = mat['Data'].Cell3.Exp7.shape
        rows,cols8 = mat['Data'].Cell3.Exp8.shape
        rows,cols9 = mat['Data'].Cell3.Exp9.shape
        rows,cols10 = mat['Data'].Cell3.Exp10.shape
        rows,cols11 = mat['Data'].Cell3.Exp11.shape
        rows,cols12 = mat['Data'].Cell3.Exp12.shape
        rows,cols13 = mat['Data'].Cell3.Exp13.shape
        rows,cols14 = mat['Data'].Cell3.Exp14.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
        print('Experiment ' + str(14) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID14) + ' contains *** ' + str(int(cols14)) + ' *** traces.')
    elif mat['Data'].Cell3.Expts == 15:
        rows,cols1 = mat['Data'].Cell3.Exp1.shape
        rows,cols2 = mat['Data'].Cell3.Exp2.shape
        rows,cols3 = mat['Data'].Cell3.Exp3.shape
        rows,cols4 = mat['Data'].Cell3.Exp4.shape
        rows,cols5 = mat['Data'].Cell3.Exp5.shape
        rows,cols6 = mat['Data'].Cell3.Exp6.shape
        rows,cols7 = mat['Data'].Cell3.Exp7.shape
        rows,cols8 = mat['Data'].Cell3.Exp8.shape
        rows,cols9 = mat['Data'].Cell3.Exp9.shape
        rows,cols10 = mat['Data'].Cell3.Exp10.shape
        rows,cols11 = mat['Data'].Cell3.Exp11.shape
        rows,cols12 = mat['Data'].Cell3.Exp12.shape
        rows,cols13 = mat['Data'].Cell3.Exp13.shape
        rows,cols14 = mat['Data'].Cell3.Exp14.shape
        rows,cols15 = mat['Data'].Cell3.Exp15.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
        print('Experiment ' + str(14) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID14) + ' contains *** ' + str(int(cols14)) + ' *** traces.')
        print('Experiment ' + str(15) + ' is a(n) ' + str(mat['Data'].Cell3.ExptID15) + ' contains *** ' + str(int(cols15)) + ' *** traces.')
    User_choices['ExptVal'] = int(input('Which experiment would you like to analyze?:'))
    
if User_choices['CellVal'] == 4:
    print('There are *** ' +str(int(mat['Data'].Cell4.Expts)) + ' *** experiments for this cell.')
    if mat['Data'].Cell4.Expts == 1:
        rows,cols1 = mat['Data'].Cell4.Exp1.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
    elif mat['Data'].Cell4.Expts == 2:
        rows,cols1 = mat['Data'].Cell4.Exp1.shape
        rows,cols2 = mat['Data'].Cell4.Exp2.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
    elif mat['Data'].Cell4.Expts == 3:
        rows,cols1 = mat['Data'].Cell4.Exp1.shape
        rows,cols2 = mat['Data'].Cell4.Exp2.shape
        rows,cols3 = mat['Data'].Cell4.Exp3.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
    elif mat['Data'].Cell4.Expts == 4:
        rows,cols1 = mat['Data'].Cell4.Exp1.shape
        rows,cols2 = mat['Data'].Cell4.Exp2.shape
        rows,cols3 = mat['Data'].Cell4.Exp3.shape
        rows,cols4 = mat['Data'].Cell4.Exp4.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
    elif mat['Data'].Cell4.Expts == 5:
        rows,cols1 = mat['Data'].Cell4.Exp1.shape
        rows,cols2 = mat['Data'].Cell4.Exp2.shape
        rows,cols3 = mat['Data'].Cell4.Exp3.shape
        rows,cols4 = mat['Data'].Cell4.Exp4.shape
        rows,cols5 = mat['Data'].Cell4.Exp5.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
    elif mat['Data'].Cell4.Expts == 6:
        rows,cols1 = mat['Data'].Cell4.Exp1.shape
        rows,cols2 = mat['Data'].Cell4.Exp2.shape
        rows,cols3 = mat['Data'].Cell4.Exp3.shape
        rows,cols4 = mat['Data'].Cell4.Exp4.shape
        rows,cols5 = mat['Data'].Cell4.Exp5.shape
        rows,cols6 = mat['Data'].Cell4.Exp6.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
    elif mat['Data'].Cell4.Expts == 7:
        rows,cols1 = mat['Data'].Cell4.Exp1.shape
        rows,cols2 = mat['Data'].Cell4.Exp2.shape
        rows,cols3 = mat['Data'].Cell4.Exp3.shape
        rows,cols4 = mat['Data'].Cell4.Exp4.shape
        rows,cols5 = mat['Data'].Cell4.Exp5.shape
        rows,cols6 = mat['Data'].Cell4.Exp6.shape
        rows,cols7 = mat['Data'].Cell4.Exp7.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')        
    elif mat['Data'].Cell4.Expts == 8:
        rows,cols1 = mat['Data'].Cell4.Exp1.shape
        rows,cols2 = mat['Data'].Cell4.Exp2.shape
        rows,cols3 = mat['Data'].Cell4.Exp3.shape
        rows,cols4 = mat['Data'].Cell4.Exp4.shape
        rows,cols5 = mat['Data'].Cell4.Exp5.shape
        rows,cols6 = mat['Data'].Cell4.Exp6.shape
        rows,cols7 = mat['Data'].Cell4.Exp7.shape
        rows,cols8 = mat['Data'].Cell4.Exp8.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
    elif mat['Data'].Cell4.Expts == 9:
        rows,cols1 = mat['Data'].Cell4.Exp1.shape
        rows,cols2 = mat['Data'].Cell4.Exp2.shape
        rows,cols3 = mat['Data'].Cell4.Exp3.shape
        rows,cols4 = mat['Data'].Cell4.Exp4.shape
        rows,cols5 = mat['Data'].Cell4.Exp5.shape
        rows,cols6 = mat['Data'].Cell4.Exp6.shape
        rows,cols7 = mat['Data'].Cell4.Exp7.shape
        rows,cols8 = mat['Data'].Cell4.Exp8.shape
        rows,cols9 = mat['Data'].Cell4.Exp9.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
    elif mat['Data'].Cell4.Expts == 10:        
        rows,cols1 = mat['Data'].Cell4.Exp1.shape
        rows,cols2 = mat['Data'].Cell4.Exp2.shape
        rows,cols3 = mat['Data'].Cell4.Exp3.shape
        rows,cols4 = mat['Data'].Cell4.Exp4.shape
        rows,cols5 = mat['Data'].Cell4.Exp5.shape
        rows,cols6 = mat['Data'].Cell4.Exp6.shape
        rows,cols7 = mat['Data'].Cell4.Exp7.shape
        rows,cols8 = mat['Data'].Cell4.Exp8.shape
        rows,cols9 = mat['Data'].Cell4.Exp9.shape
        rows,cols10 = mat['Data'].Cell4.Exp10.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
    elif mat['Data'].Cell4.Expts == 11:        
        rows,cols1 = mat['Data'].Cell4.Exp1.shape
        rows,cols2 = mat['Data'].Cell4.Exp2.shape
        rows,cols3 = mat['Data'].Cell4.Exp3.shape
        rows,cols4 = mat['Data'].Cell4.Exp4.shape
        rows,cols5 = mat['Data'].Cell4.Exp5.shape
        rows,cols6 = mat['Data'].Cell4.Exp6.shape
        rows,cols7 = mat['Data'].Cell4.Exp7.shape
        rows,cols8 = mat['Data'].Cell4.Exp8.shape
        rows,cols9 = mat['Data'].Cell4.Exp9.shape
        rows,cols10 = mat['Data'].Cell4.Exp10.shape
        rows,cols11 = mat['Data'].Cell4.Exp11.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
    elif mat['Data'].Cell4.Expts == 12:
        rows,cols1 = mat['Data'].Cell4.Exp1.shape
        rows,cols2 = mat['Data'].Cell4.Exp2.shape
        rows,cols3 = mat['Data'].Cell4.Exp3.shape
        rows,cols4 = mat['Data'].Cell4.Exp4.shape
        rows,cols5 = mat['Data'].Cell4.Exp5.shape
        rows,cols6 = mat['Data'].Cell4.Exp6.shape
        rows,cols7 = mat['Data'].Cell4.Exp7.shape
        rows,cols8 = mat['Data'].Cell4.Exp8.shape
        rows,cols9 = mat['Data'].Cell4.Exp9.shape
        rows,cols10 = mat['Data'].Cell4.Exp10.shape
        rows,cols11 = mat['Data'].Cell4.Exp11.shape
        rows,cols12 = mat['Data'].Cell4.Exp12.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
    elif mat['Data'].Cell4.Expts == 13:
        rows,cols1 = mat['Data'].Cell4.Exp1.shape
        rows,cols2 = mat['Data'].Cell4.Exp2.shape
        rows,cols3 = mat['Data'].Cell4.Exp3.shape
        rows,cols4 = mat['Data'].Cell4.Exp4.shape
        rows,cols5 = mat['Data'].Cell4.Exp5.shape
        rows,cols6 = mat['Data'].Cell4.Exp6.shape
        rows,cols7 = mat['Data'].Cell4.Exp7.shape
        rows,cols8 = mat['Data'].Cell4.Exp8.shape
        rows,cols9 = mat['Data'].Cell4.Exp9.shape
        rows,cols10 = mat['Data'].Cell4.Exp10.shape
        rows,cols11 = mat['Data'].Cell4.Exp11.shape
        rows,cols12 = mat['Data'].Cell4.Exp12.shape
        rows,cols13 = mat['Data'].Cell4.Exp13.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
    elif mat['Data'].Cell4.Expts == 14:
        rows,cols1 = mat['Data'].Cell4.Exp1.shape
        rows,cols2 = mat['Data'].Cell4.Exp2.shape
        rows,cols3 = mat['Data'].Cell4.Exp3.shape
        rows,cols4 = mat['Data'].Cell4.Exp4.shape
        rows,cols5 = mat['Data'].Cell4.Exp5.shape
        rows,cols6 = mat['Data'].Cell4.Exp6.shape
        rows,cols7 = mat['Data'].Cell4.Exp7.shape
        rows,cols8 = mat['Data'].Cell4.Exp8.shape
        rows,cols9 = mat['Data'].Cell4.Exp9.shape
        rows,cols10 = mat['Data'].Cell4.Exp10.shape
        rows,cols11 = mat['Data'].Cell4.Exp11.shape
        rows,cols12 = mat['Data'].Cell4.Exp12.shape
        rows,cols13 = mat['Data'].Cell4.Exp13.shape
        rows,cols14 = mat['Data'].Cell4.Exp14.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
        print('Experiment ' + str(14) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID14) + ' contains *** ' + str(int(cols14)) + ' *** traces.')
    elif mat['Data'].Cell4.Expts == 15:
        rows,cols1 = mat['Data'].Cell4.Exp1.shape
        rows,cols2 = mat['Data'].Cell4.Exp2.shape
        rows,cols3 = mat['Data'].Cell4.Exp3.shape
        rows,cols4 = mat['Data'].Cell4.Exp4.shape
        rows,cols5 = mat['Data'].Cell4.Exp5.shape
        rows,cols6 = mat['Data'].Cell4.Exp6.shape
        rows,cols7 = mat['Data'].Cell4.Exp7.shape
        rows,cols8 = mat['Data'].Cell4.Exp8.shape
        rows,cols9 = mat['Data'].Cell4.Exp9.shape
        rows,cols10 = mat['Data'].Cell4.Exp10.shape
        rows,cols11 = mat['Data'].Cell4.Exp11.shape
        rows,cols12 = mat['Data'].Cell4.Exp12.shape
        rows,cols13 = mat['Data'].Cell4.Exp13.shape
        rows,cols14 = mat['Data'].Cell4.Exp14.shape
        rows,cols15 = mat['Data'].Cell4.Exp15.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
        print('Experiment ' + str(14) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID14) + ' contains *** ' + str(int(cols14)) + ' *** traces.')
        print('Experiment ' + str(15) + ' is a(n) ' + str(mat['Data'].Cell4.ExptID15) + ' contains *** ' + str(int(cols15)) + ' *** traces.')
    User_choices['ExptVal'] = int(input('Which experiment would you like to analyze?:'))

if User_choices['CellVal'] == 5:
    print('There are *** ' +str(int(mat['Data'].Cell5.Expts)) + ' *** experiments for this cell.')
    if mat['Data'].Cell5.Expts == 1:
        rows,cols1 = mat['Data'].Cell5.Exp1.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
    elif mat['Data'].Cell5.Expts == 2:
        rows,cols1 = mat['Data'].Cell5.Exp1.shape
        rows,cols2 = mat['Data'].Cell5.Exp2.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
    elif mat['Data'].Cell5.Expts == 3:
        rows,cols1 = mat['Data'].Cell5.Exp1.shape
        rows,cols2 = mat['Data'].Cell5.Exp2.shape
        rows,cols3 = mat['Data'].Cell5.Exp3.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
    elif mat['Data'].Cell5.Expts == 4:
        rows,cols1 = mat['Data'].Cell5.Exp1.shape
        rows,cols2 = mat['Data'].Cell5.Exp2.shape
        rows,cols3 = mat['Data'].Cell5.Exp3.shape
        rows,cols4 = mat['Data'].Cell5.Exp4.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
    elif mat['Data'].Cell5.Expts == 5:
        rows,cols1 = mat['Data'].Cell5.Exp1.shape
        rows,cols2 = mat['Data'].Cell5.Exp2.shape
        rows,cols3 = mat['Data'].Cell5.Exp3.shape
        rows,cols4 = mat['Data'].Cell5.Exp4.shape
        rows,cols5 = mat['Data'].Cell5.Exp5.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
    elif mat['Data'].Cell5.Expts == 6:
        rows,cols1 = mat['Data'].Cell5.Exp1.shape
        rows,cols2 = mat['Data'].Cell5.Exp2.shape
        rows,cols3 = mat['Data'].Cell5.Exp3.shape
        rows,cols4 = mat['Data'].Cell5.Exp4.shape
        rows,cols5 = mat['Data'].Cell5.Exp5.shape
        rows,cols6 = mat['Data'].Cell5.Exp6.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
    elif mat['Data'].Cell5.Expts == 7:
        rows,cols1 = mat['Data'].Cell5.Exp1.shape
        rows,cols2 = mat['Data'].Cell5.Exp2.shape
        rows,cols3 = mat['Data'].Cell5.Exp3.shape
        rows,cols4 = mat['Data'].Cell5.Exp4.shape
        rows,cols5 = mat['Data'].Cell5.Exp5.shape
        rows,cols6 = mat['Data'].Cell5.Exp6.shape
        rows,cols7 = mat['Data'].Cell5.Exp7.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')        
    elif mat['Data'].Cell5.Expts == 8:
        rows,cols1 = mat['Data'].Cell5.Exp1.shape
        rows,cols2 = mat['Data'].Cell5.Exp2.shape
        rows,cols3 = mat['Data'].Cell5.Exp3.shape
        rows,cols4 = mat['Data'].Cell5.Exp4.shape
        rows,cols5 = mat['Data'].Cell5.Exp5.shape
        rows,cols6 = mat['Data'].Cell5.Exp6.shape
        rows,cols7 = mat['Data'].Cell5.Exp7.shape
        rows,cols8 = mat['Data'].Cell5.Exp8.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
    elif mat['Data'].Cell5.Expts == 9:
        rows,cols1 = mat['Data'].Cell5.Exp1.shape
        cols2 = mat['Data'].Cell5.Exp2.shape
        rows,cols3 = mat['Data'].Cell5.Exp3.shape
        rows,cols4 = mat['Data'].Cell5.Exp4.shape
        rows,cols5 = mat['Data'].Cell5.Exp5.shape
        rows,cols6 = mat['Data'].Cell5.Exp6.shape
        rows,cols7 = mat['Data'].Cell5.Exp7.shape
        rows,cols8 = mat['Data'].Cell5.Exp8.shape
        rows,cols9 = mat['Data'].Cell5.Exp9.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID2) + ' contains *** ' + str(int(cols2[0])) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
    elif mat['Data'].Cell5.Expts == 10:        
        rows,cols1 = mat['Data'].Cell5.Exp1.shape
        rows,cols2 = mat['Data'].Cell5.Exp2.shape
        rows,cols3 = mat['Data'].Cell5.Exp3.shape
        rows,cols4 = mat['Data'].Cell5.Exp4.shape
        rows,cols5 = mat['Data'].Cell5.Exp5.shape
        rows,cols6 = mat['Data'].Cell5.Exp6.shape
        rows,cols7 = mat['Data'].Cell5.Exp7.shape
        rows,cols8 = mat['Data'].Cell5.Exp8.shape
        rows,cols9 = mat['Data'].Cell5.Exp9.shape
        rows,cols10 = mat['Data'].Cell5.Exp10.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
    elif mat['Data'].Cell5.Expts == 11:        
        rows,cols1 = mat['Data'].Cell5.Exp1.shape
        rows,cols2 = mat['Data'].Cell5.Exp2.shape
        rows,cols3 = mat['Data'].Cell5.Exp3.shape
        rows,cols4 = mat['Data'].Cell5.Exp4.shape
        rows,cols5 = mat['Data'].Cell5.Exp5.shape
        rows,cols6 = mat['Data'].Cell5.Exp6.shape
        rows,cols7 = mat['Data'].Cell5.Exp7.shape
        rows,cols8 = mat['Data'].Cell5.Exp8.shape
        rows,cols9 = mat['Data'].Cell5.Exp9.shape
        rows,cols10 = mat['Data'].Cell5.Exp10.shape
        rows,cols11 = mat['Data'].Cell5.Exp11.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
    elif mat['Data'].Cell5.Expts == 12:
        rows,cols1 = mat['Data'].Cell5.Exp1.shape
        rows,cols2 = mat['Data'].Cell5.Exp2.shape
        rows,cols3 = mat['Data'].Cell5.Exp3.shape
        rows,cols4 = mat['Data'].Cell5.Exp4.shape
        rows,cols5 = mat['Data'].Cell5.Exp5.shape
        rows,cols6 = mat['Data'].Cell5.Exp6.shape
        rows,cols7 = mat['Data'].Cell5.Exp7.shape
        rows,cols8 = mat['Data'].Cell5.Exp8.shape
        rows,cols9 = mat['Data'].Cell5.Exp9.shape
        rows,cols10 = mat['Data'].Cell5.Exp10.shape
        rows,cols11 = mat['Data'].Cell5.Exp11.shape
        rows,cols12 = mat['Data'].Cell5.Exp12.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
    elif mat['Data'].Cell5.Expts == 13:
        rows,cols1 = mat['Data'].Cell5.Exp1.shape
        rows,cols2 = mat['Data'].Cell5.Exp2.shape
        rows,cols3 = mat['Data'].Cell5.Exp3.shape
        rows,cols4 = mat['Data'].Cell5.Exp4.shape
        rows,cols5 = mat['Data'].Cell5.Exp5.shape
        rows,cols6 = mat['Data'].Cell5.Exp6.shape
        rows,cols7 = mat['Data'].Cell5.Exp7.shape
        rows,cols8 = mat['Data'].Cell5.Exp8.shape
        rows,cols9 = mat['Data'].Cell5.Exp9.shape
        rows,cols10 = mat['Data'].Cell5.Exp10.shape
        rows,cols11 = mat['Data'].Cell5.Exp11.shape
        rows,cols12 = mat['Data'].Cell5.Exp12.shape
        rows,cols13 = mat['Data'].Cell5.Exp13.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
    elif mat['Data'].Cell5.Expts == 14:
        rows,cols1 = mat['Data'].Cell5.Exp1.shape
        rows,cols2 = mat['Data'].Cell5.Exp2.shape
        rows,cols3 = mat['Data'].Cell5.Exp3.shape
        rows,cols4 = mat['Data'].Cell5.Exp4.shape
        rows,cols5 = mat['Data'].Cell5.Exp5.shape
        rows,cols6 = mat['Data'].Cell5.Exp6.shape
        rows,cols7 = mat['Data'].Cell5.Exp7.shape
        rows,cols8 = mat['Data'].Cell5.Exp8.shape
        rows,cols9 = mat['Data'].Cell5.Exp9.shape
        rows,cols10 = mat['Data'].Cell5.Exp10.shape
        rows,cols11 = mat['Data'].Cell5.Exp11.shape
        rows,cols12 = mat['Data'].Cell5.Exp12.shape
        rows,cols13 = mat['Data'].Cell5.Exp13.shape
        rows,cols14 = mat['Data'].Cell5.Exp14.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
        print('Experiment ' + str(14) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID14) + ' contains *** ' + str(int(cols14)) + ' *** traces.')
    elif mat['Data'].Cell5.Expts == 15:
        rows,cols1 = mat['Data'].Cell5.Exp1.shape
        rows,cols2 = mat['Data'].Cell5.Exp2.shape
        rows,cols3 = mat['Data'].Cell5.Exp3.shape
        rows,cols4 = mat['Data'].Cell5.Exp4.shape
        rows,cols5 = mat['Data'].Cell5.Exp5.shape
        rows,cols6 = mat['Data'].Cell5.Exp6.shape
        rows,cols7 = mat['Data'].Cell5.Exp7.shape
        rows,cols8 = mat['Data'].Cell5.Exp8.shape
        rows,cols9 = mat['Data'].Cell5.Exp9.shape
        rows,cols10 = mat['Data'].Cell5.Exp10.shape
        rows,cols11 = mat['Data'].Cell5.Exp11.shape
        rows,cols12 = mat['Data'].Cell5.Exp12.shape
        rows,cols13 = mat['Data'].Cell5.Exp13.shape
        rows,cols14 = mat['Data'].Cell5.Exp14.shape
        rows,cols15 = mat['Data'].Cell5.Exp15.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
        print('Experiment ' + str(14) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID14) + ' contains *** ' + str(int(cols14)) + ' *** traces.')
        print('Experiment ' + str(15) + ' is a(n) ' + str(mat['Data'].Cell5.ExptID15) + ' contains *** ' + str(int(cols15)) + ' *** traces.')
    User_choices['ExptVal'] = int(input('Which experiment would you like to analyze?:'))

if User_choices['CellVal'] == 6:
    print('There are *** ' +str(int(mat['Data'].Cell6.Expts)) + ' *** experiments for this cell.')
    if mat['Data'].Cell6.Expts == 1:
        rows,cols1 = mat['Data'].Cell6.Exp1.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
    elif mat['Data'].Cell6.Expts == 2:
        rows,cols1 = mat['Data'].Cell6.Exp1.shape
        rows,cols2 = mat['Data'].Cell6.Exp2.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
    elif mat['Data'].Cell6.Expts == 3:
        rows,cols1 = mat['Data'].Cell6.Exp1.shape
        rows,cols2 = mat['Data'].Cell6.Exp2.shape
        rows,cols3 = mat['Data'].Cell6.Exp3.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
    elif mat['Data'].Cell6.Expts == 4:
        rows,cols1 = mat['Data'].Cell6.Exp1.shape
        rows,cols2 = mat['Data'].Cell6.Exp2.shape
        rows,cols3 = mat['Data'].Cell6.Exp3.shape
        rows,cols4 = mat['Data'].Cell6.Exp4.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
    elif mat['Data'].Cell6.Expts == 5:
        rows,cols1 = mat['Data'].Cell6.Exp1.shape
        rows,cols2 = mat['Data'].Cell6.Exp2.shape
        rows,cols3 = mat['Data'].Cell6.Exp3.shape
        rows,cols4 = mat['Data'].Cell6.Exp4.shape
        rows,cols5 = mat['Data'].Cell6.Exp5.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
    elif mat['Data'].Cell6.Expts == 6:
        rows,cols1 = mat['Data'].Cell6.Exp1.shape
        rows,cols2 = mat['Data'].Cell6.Exp2.shape
        rows,cols3 = mat['Data'].Cell6.Exp3.shape
        rows,cols4 = mat['Data'].Cell6.Exp4.shape
        rows,cols5 = mat['Data'].Cell6.Exp5.shape
        rows,cols6 = mat['Data'].Cell6.Exp6.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
    elif mat['Data'].Cell6.Expts == 7:
        rows,cols1 = mat['Data'].Cell6.Exp1.shape
        rows,cols2 = mat['Data'].Cell6.Exp2.shape
        rows,cols3 = mat['Data'].Cell6.Exp3.shape
        rows,cols4 = mat['Data'].Cell6.Exp4.shape
        rows,cols5 = mat['Data'].Cell6.Exp5.shape
        rows,cols6 = mat['Data'].Cell6.Exp6.shape
        rows,cols7 = mat['Data'].Cell6.Exp7.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')        
    elif mat['Data'].Cell6.Expts == 8:
        rows,cols1 = mat['Data'].Cell6.Exp1.shape
        rows,cols2 = mat['Data'].Cell6.Exp2.shape
        rows,cols3 = mat['Data'].Cell6.Exp3.shape
        rows,cols4 = mat['Data'].Cell6.Exp4.shape
        rows,cols5 = mat['Data'].Cell6.Exp5.shape
        rows,cols6 = mat['Data'].Cell6.Exp6.shape
        rows,cols7 = mat['Data'].Cell6.Exp7.shape
        rows,cols8 = mat['Data'].Cell6.Exp8.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
    elif mat['Data'].Cell6.Expts == 9:
        rows,cols1 = mat['Data'].Cell6.Exp1.shape
        rows,cols2 = mat['Data'].Cell6.Exp2.shape
        rows,cols3 = mat['Data'].Cell6.Exp3.shape
        rows,cols4 = mat['Data'].Cell6.Exp4.shape
        rows,cols5 = mat['Data'].Cell6.Exp5.shape
        rows,cols6 = mat['Data'].Cell6.Exp6.shape
        rows,cols7 = mat['Data'].Cell6.Exp7.shape
        rows,cols8 = mat['Data'].Cell6.Exp8.shape
        rows,cols9 = mat['Data'].Cell6.Exp9.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
    elif mat['Data'].Cell6.Expts == 10:        
        rows,cols1 = mat['Data'].Cell6.Exp1.shape
        rows,cols2 = mat['Data'].Cell6.Exp2.shape
        rows,cols3 = mat['Data'].Cell6.Exp3.shape
        rows,cols4 = mat['Data'].Cell6.Exp4.shape
        rows,cols5 = mat['Data'].Cell6.Exp5.shape
        rows,cols6 = mat['Data'].Cell6.Exp6.shape
        rows,cols7 = mat['Data'].Cell6.Exp7.shape
        rows,cols8 = mat['Data'].Cell6.Exp8.shape
        rows,cols9 = mat['Data'].Cell6.Exp9.shape
        rows,cols10 = mat['Data'].Cell6.Exp10.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
    elif mat['Data'].Cell6.Expts == 11:        
        rows,cols1 = mat['Data'].Cell6.Exp1.shape
        rows,cols2 = mat['Data'].Cell6.Exp2.shape
        rows,cols3 = mat['Data'].Cell6.Exp3.shape
        rows,cols4 = mat['Data'].Cell6.Exp4.shape
        rows,cols5 = mat['Data'].Cell6.Exp5.shape
        rows,cols6 = mat['Data'].Cell6.Exp6.shape
        rows,cols7 = mat['Data'].Cell6.Exp7.shape
        rows,cols8 = mat['Data'].Cell6.Exp8.shape
        rows,cols9 = mat['Data'].Cell6.Exp9.shape
        rows,cols10 = mat['Data'].Cell6.Exp10.shape
        rows,cols11 = mat['Data'].Cell6.Exp11.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
    elif mat['Data'].Cell6.Expts == 12:
        rows,cols1 = mat['Data'].Cell6.Exp1.shape
        rows,cols2 = mat['Data'].Cell6.Exp2.shape
        rows,cols3 = mat['Data'].Cell6.Exp3.shape
        rows,cols4 = mat['Data'].Cell6.Exp4.shape
        rows,cols5 = mat['Data'].Cell6.Exp5.shape
        rows,cols6 = mat['Data'].Cell6.Exp6.shape
        rows,cols7 = mat['Data'].Cell6.Exp7.shape
        rows,cols8 = mat['Data'].Cell6.Exp8.shape
        rows,cols9 = mat['Data'].Cell6.Exp9.shape
        rows,cols10 = mat['Data'].Cell6.Exp10.shape
        rows,cols11 = mat['Data'].Cell6.Exp11.shape
        rows,cols12 = mat['Data'].Cell6.Exp12.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
    elif mat['Data'].Cell6.Expts == 13:
        rows,cols1 = mat['Data'].Cell6.Exp1.shape
        rows,cols2 = mat['Data'].Cell6.Exp2.shape
        rows,cols3 = mat['Data'].Cell6.Exp3.shape
        rows,cols4 = mat['Data'].Cell6.Exp4.shape
        rows,cols5 = mat['Data'].Cell6.Exp5.shape
        rows,cols6 = mat['Data'].Cell6.Exp6.shape
        rows,cols7 = mat['Data'].Cell6.Exp7.shape
        rows,cols8 = mat['Data'].Cell6.Exp8.shape
        rows,cols9 = mat['Data'].Cell6.Exp9.shape
        rows,cols10 = mat['Data'].Cell6.Exp10.shape
        rows,cols11 = mat['Data'].Cell6.Exp11.shape
        rows,cols12 = mat['Data'].Cell6.Exp12.shape
        rows,cols13 = mat['Data'].Cell6.Exp13.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
    elif mat['Data'].Cell6.Expts == 14:
        rows,cols1 = mat['Data'].Cell6.Exp1.shape
        rows,cols2 = mat['Data'].Cell6.Exp2.shape
        rows,cols3 = mat['Data'].Cell6.Exp3.shape
        rows,cols4 = mat['Data'].Cell6.Exp4.shape
        rows,cols5 = mat['Data'].Cell6.Exp5.shape
        rows,cols6 = mat['Data'].Cell6.Exp6.shape
        rows,cols7 = mat['Data'].Cell6.Exp7.shape
        rows,cols8 = mat['Data'].Cell6.Exp8.shape
        rows,cols9 = mat['Data'].Cell6.Exp9.shape
        rows,cols10 = mat['Data'].Cell6.Exp10.shape
        rows,cols11 = mat['Data'].Cell6.Exp11.shape
        rows,cols12 = mat['Data'].Cell6.Exp12.shape
        rows,cols13 = mat['Data'].Cell6.Exp13.shape
        rows,cols14 = mat['Data'].Cell6.Exp14.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
        print('Experiment ' + str(14) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID14) + ' contains *** ' + str(int(cols14)) + ' *** traces.')
    elif mat['Data'].Cell6.Expts == 15:
        rows,cols1 = mat['Data'].Cell6.Exp1.shape
        rows,cols2 = mat['Data'].Cell6.Exp2.shape
        rows,cols3 = mat['Data'].Cell6.Exp3.shape
        rows,cols4 = mat['Data'].Cell6.Exp4.shape
        rows,cols5 = mat['Data'].Cell6.Exp5.shape
        rows,cols6 = mat['Data'].Cell6.Exp6.shape
        rows,cols7 = mat['Data'].Cell6.Exp7.shape
        rows,cols8 = mat['Data'].Cell6.Exp8.shape
        rows,cols9 = mat['Data'].Cell6.Exp9.shape
        rows,cols10 = mat['Data'].Cell6.Exp10.shape
        rows,cols11 = mat['Data'].Cell6.Exp11.shape
        rows,cols12 = mat['Data'].Cell6.Exp12.shape
        rows,cols13 = mat['Data'].Cell6.Exp13.shape
        rows,cols14 = mat['Data'].Cell6.Exp14.shape
        rows,cols15 = mat['Data'].Cell6.Exp15.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
        print('Experiment ' + str(14) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID14) + ' contains *** ' + str(int(cols14)) + ' *** traces.')
        print('Experiment ' + str(15) + ' is a(n) ' + str(mat['Data'].Cell6.ExptID15) + ' contains *** ' + str(int(cols15)) + ' *** traces.')
    User_choices['ExptVal'] = int(input('Which experiment would you like to analyze?:'))

if User_choices['CellVal'] == 7:
    print('There are *** ' +str(int(mat['Data'].Cell7.Expts)) + ' *** experiments for this cell.')
    if mat['Data'].Cell7.Expts == 1:
        rows,cols1 = mat['Data'].Cell7.Exp1.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
    elif mat['Data'].Cell7.Expts == 2:
        rows,cols1 = mat['Data'].Cell7.Exp1.shape
        rows,cols2 = mat['Data'].Cell7.Exp2.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
    elif mat['Data'].Cell7.Expts == 3:
        rows,cols1 = mat['Data'].Cell7.Exp1.shape
        rows,cols2 = mat['Data'].Cell7.Exp2.shape
        rows,cols3 = mat['Data'].Cell7.Exp3.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
    elif mat['Data'].Cell7.Expts == 4:
        rows,cols1 = mat['Data'].Cell7.Exp1.shape
        rows,cols2 = mat['Data'].Cell7.Exp2.shape
        rows,cols3 = mat['Data'].Cell7.Exp3.shape
        rows,cols4 = mat['Data'].Cell7.Exp4.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
    elif mat['Data'].Cell7.Expts == 5:
        rows,cols1 = mat['Data'].Cell7.Exp1.shape
        rows,cols2 = mat['Data'].Cell7.Exp2.shape
        rows,cols3 = mat['Data'].Cell7.Exp3.shape
        rows,cols4 = mat['Data'].Cell7.Exp4.shape
        rows,cols5 = mat['Data'].Cell7.Exp5.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
    elif mat['Data'].Cell7.Expts == 6:
        rows,cols1 = mat['Data'].Cell7.Exp1.shape
        rows,cols2 = mat['Data'].Cell7.Exp2.shape
        rows,cols3 = mat['Data'].Cell7.Exp3.shape
        rows,cols4 = mat['Data'].Cell7.Exp4.shape
        rows,cols5 = mat['Data'].Cell7.Exp5.shape
        rows,cols6 = mat['Data'].Cell7.Exp6.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
    elif mat['Data'].Cell7.Expts == 7:
        rows,cols1 = mat['Data'].Cell7.Exp1.shape
        rows,cols2 = mat['Data'].Cell7.Exp2.shape
        rows,cols3 = mat['Data'].Cell7.Exp3.shape
        rows,cols4 = mat['Data'].Cell7.Exp4.shape
        rows,cols5 = mat['Data'].Cell7.Exp5.shape
        rows,cols6 = mat['Data'].Cell7.Exp6.shape
        rows,cols7 = mat['Data'].Cell7.Exp7.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')        
    elif mat['Data'].Cell7.Expts == 8:
        rows,cols1 = mat['Data'].Cell7.Exp1.shape
        rows,cols2 = mat['Data'].Cell7.Exp2.shape
        rows,cols3 = mat['Data'].Cell7.Exp3.shape
        rows,cols4 = mat['Data'].Cell7.Exp4.shape
        rows,cols5 = mat['Data'].Cell7.Exp5.shape
        rows,cols6 = mat['Data'].Cell7.Exp6.shape
        rows,cols7 = mat['Data'].Cell7.Exp7.shape
        rows,cols8 = mat['Data'].Cell7.Exp8.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
    elif mat['Data'].Cell7.Expts == 9:
        rows,cols1 = mat['Data'].Cell7.Exp1.shape
        rows,cols2 = mat['Data'].Cell7.Exp2.shape
        rows,cols3 = mat['Data'].Cell7.Exp3.shape
        rows,cols4 = mat['Data'].Cell7.Exp4.shape
        rows,cols5 = mat['Data'].Cell7.Exp5.shape
        rows,cols6 = mat['Data'].Cell7.Exp6.shape
        rows,cols7 = mat['Data'].Cell7.Exp7.shape
        rows,cols8 = mat['Data'].Cell7.Exp8.shape
        rows,cols9 = mat['Data'].Cell7.Exp9.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
    elif mat['Data'].Cell7.Expts == 10:        
        rows,cols1 = mat['Data'].Cell7.Exp1.shape
        rows,cols2 = mat['Data'].Cell7.Exp2.shape
        rows,cols3 = mat['Data'].Cell7.Exp3.shape
        rows,cols4 = mat['Data'].Cell7.Exp4.shape
        rows,cols5 = mat['Data'].Cell7.Exp5.shape
        rows,cols6 = mat['Data'].Cell7.Exp6.shape
        rows,cols7 = mat['Data'].Cell7.Exp7.shape
        rows,cols8 = mat['Data'].Cell7.Exp8.shape
        rows,cols9 = mat['Data'].Cell7.Exp9.shape
        rows,cols10 = mat['Data'].Cell7.Exp10.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
    elif mat['Data'].Cell7.Expts == 11:        
        rows,cols1 = mat['Data'].Cell7.Exp1.shape
        rows,cols2 = mat['Data'].Cell7.Exp2.shape
        rows,cols3 = mat['Data'].Cell7.Exp3.shape
        rows,cols4 = mat['Data'].Cell7.Exp4.shape
        rows,cols5 = mat['Data'].Cell7.Exp5.shape
        rows,cols6 = mat['Data'].Cell7.Exp6.shape
        rows,cols7 = mat['Data'].Cell7.Exp7.shape
        rows,cols8 = mat['Data'].Cell7.Exp8.shape
        rows,cols9 = mat['Data'].Cell7.Exp9.shape
        rows,cols10 = mat['Data'].Cell7.Exp10.shape
        rows,cols11 = mat['Data'].Cell7.Exp11.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
    elif mat['Data'].Cell7.Expts == 12:
        rows,cols1 = mat['Data'].Cell7.Exp1.shape
        rows,cols2 = mat['Data'].Cell7.Exp2.shape
        rows,cols3 = mat['Data'].Cell7.Exp3.shape
        rows,cols4 = mat['Data'].Cell7.Exp4.shape
        rows,cols5 = mat['Data'].Cell7.Exp5.shape
        rows,cols6 = mat['Data'].Cell7.Exp6.shape
        rows,cols7 = mat['Data'].Cell7.Exp7.shape
        rows,cols8 = mat['Data'].Cell7.Exp8.shape
        rows,cols9 = mat['Data'].Cell7.Exp9.shape
        rows,cols10 = mat['Data'].Cell7.Exp10.shape
        rows,cols11 = mat['Data'].Cell7.Exp11.shape
        rows,cols12 = mat['Data'].Cell7.Exp12.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
    elif mat['Data'].Cell7.Expts == 13:
        rows,cols1 = mat['Data'].Cell7.Exp1.shape
        rows,cols2 = mat['Data'].Cell7.Exp2.shape
        rows,cols3 = mat['Data'].Cell7.Exp3.shape
        rows,cols4 = mat['Data'].Cell7.Exp4.shape
        rows,cols5 = mat['Data'].Cell7.Exp5.shape
        rows,cols6 = mat['Data'].Cell7.Exp6.shape
        rows,cols7 = mat['Data'].Cell7.Exp7.shape
        rows,cols8 = mat['Data'].Cell7.Exp8.shape
        rows,cols9 = mat['Data'].Cell7.Exp9.shape
        rows,cols10 = mat['Data'].Cell7.Exp10.shape
        rows,cols11 = mat['Data'].Cell7.Exp11.shape
        rows,cols12 = mat['Data'].Cell7.Exp12.shape
        rows,cols13 = mat['Data'].Cell7.Exp13.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
    elif mat['Data'].Cell7.Expts == 14:
        rows,cols1 = mat['Data'].Cell7.Exp1.shape
        rows,cols2 = mat['Data'].Cell7.Exp2.shape
        rows,cols3 = mat['Data'].Cell7.Exp3.shape
        rows,cols4 = mat['Data'].Cell7.Exp4.shape
        rows,cols5 = mat['Data'].Cell7.Exp5.shape
        rows,cols6 = mat['Data'].Cell7.Exp6.shape
        rows,cols7 = mat['Data'].Cell7.Exp7.shape
        rows,cols8 = mat['Data'].Cell7.Exp8.shape
        rows,cols9 = mat['Data'].Cell7.Exp9.shape
        rows,cols10 = mat['Data'].Cell7.Exp10.shape
        rows,cols11 = mat['Data'].Cell7.Exp11.shape
        rows,cols12 = mat['Data'].Cell7.Exp12.shape
        rows,cols13 = mat['Data'].Cell7.Exp13.shape
        rows,cols14 = mat['Data'].Cell7.Exp14.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
        print('Experiment ' + str(14) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID14) + ' contains *** ' + str(int(cols14)) + ' *** traces.')
    elif mat['Data'].Cell7.Expts == 15:
        rows,cols1 = mat['Data'].Cell7.Exp1.shape
        rows,cols2 = mat['Data'].Cell7.Exp2.shape
        rows,cols3 = mat['Data'].Cell7.Exp3.shape
        rows,cols4 = mat['Data'].Cell7.Exp4.shape
        rows,cols5 = mat['Data'].Cell7.Exp5.shape
        rows,cols6 = mat['Data'].Cell7.Exp6.shape
        rows,cols7 = mat['Data'].Cell7.Exp7.shape
        rows,cols8 = mat['Data'].Cell7.Exp8.shape
        rows,cols9 = mat['Data'].Cell7.Exp9.shape
        rows,cols10 = mat['Data'].Cell7.Exp10.shape
        rows,cols11 = mat['Data'].Cell7.Exp11.shape
        rows,cols12 = mat['Data'].Cell7.Exp12.shape
        rows,cols13 = mat['Data'].Cell7.Exp13.shape
        rows,cols14 = mat['Data'].Cell7.Exp14.shape
        rows,cols15 = mat['Data'].Cell7.Exp15.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
        print('Experiment ' + str(14) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID14) + ' contains *** ' + str(int(cols14)) + ' *** traces.')
        print('Experiment ' + str(15) + ' is a(n) ' + str(mat['Data'].Cell7.ExptID15) + ' contains *** ' + str(int(cols15)) + ' *** traces.')
    User_choices['ExptVal'] = int(input('Which experiment would you like to analyze?:'))

if User_choices['CellVal'] == 8:
    print('There are *** ' +str(int(mat['Data'].Cell8.Expts)) + ' *** experiments for this cell.')
    if mat['Data'].Cell8.Expts == 1:
        rows,cols1 = mat['Data'].Cell8.Exp1.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
    elif mat['Data'].Cell8.Expts == 2:
        rows,cols1 = mat['Data'].Cell8.Exp1.shape
        rows,cols2 = mat['Data'].Cell8.Exp2.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
    elif mat['Data'].Cell8.Expts == 3:
        rows,cols1 = mat['Data'].Cell8.Exp1.shape
        rows,cols2 = mat['Data'].Cell8.Exp2.shape
        rows,cols3 = mat['Data'].Cell8.Exp3.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
    elif mat['Data'].Cell8.Expts == 4:
        rows,cols1 = mat['Data'].Cell8.Exp1.shape
        rows,cols2 = mat['Data'].Cell8.Exp2.shape
        rows,cols3 = mat['Data'].Cell8.Exp3.shape
        rows,cols4 = mat['Data'].Cell8.Exp4.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
    elif mat['Data'].Cell8.Expts == 5:
        rows,cols1 = mat['Data'].Cell8.Exp1.shape
        rows,cols2 = mat['Data'].Cell8.Exp2.shape
        rows,cols3 = mat['Data'].Cell8.Exp3.shape
        rows,cols4 = mat['Data'].Cell8.Exp4.shape
        rows,cols5 = mat['Data'].Cell8.Exp5.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
    elif mat['Data'].Cell8.Expts == 6:
        rows,cols1 = mat['Data'].Cell8.Exp1.shape
        rows,cols2 = mat['Data'].Cell8.Exp2.shape
        rows,cols3 = mat['Data'].Cell8.Exp3.shape
        rows,cols4 = mat['Data'].Cell8.Exp4.shape
        rows,cols5 = mat['Data'].Cell8.Exp5.shape
        rows,cols6 = mat['Data'].Cell8.Exp6.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
    elif mat['Data'].Cell8.Expts == 7:
        rows,cols1 = mat['Data'].Cell8.Exp1.shape
        rows,cols2 = mat['Data'].Cell8.Exp2.shape
        rows,cols3 = mat['Data'].Cell8.Exp3.shape
        rows,cols4 = mat['Data'].Cell8.Exp4.shape
        rows,cols5 = mat['Data'].Cell8.Exp5.shape
        rows,cols6 = mat['Data'].Cell8.Exp6.shape
        rows,cols7 = mat['Data'].Cell8.Exp7.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')        
    elif mat['Data'].Cell8.Expts == 8:
        rows,cols1 = mat['Data'].Cell8.Exp1.shape
        rows,cols2 = mat['Data'].Cell8.Exp2.shape
        rows,cols3 = mat['Data'].Cell8.Exp3.shape
        rows,cols4 = mat['Data'].Cell8.Exp4.shape
        rows,cols5 = mat['Data'].Cell8.Exp5.shape
        rows,cols6 = mat['Data'].Cell8.Exp6.shape
        rows,cols7 = mat['Data'].Cell8.Exp7.shape
        rows,cols8 = mat['Data'].Cell8.Exp8.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
    elif mat['Data'].Cell8.Expts == 9:
        rows,cols1 = mat['Data'].Cell8.Exp1.shape
        rows,cols2 = mat['Data'].Cell8.Exp2.shape
        rows,cols3 = mat['Data'].Cell8.Exp3.shape
        rows,cols4 = mat['Data'].Cell8.Exp4.shape
        rows,cols5 = mat['Data'].Cell8.Exp5.shape
        rows,cols6 = mat['Data'].Cell8.Exp6.shape
        rows,cols7 = mat['Data'].Cell8.Exp7.shape
        rows,cols8 = mat['Data'].Cell8.Exp8.shape
        rows,cols9 = mat['Data'].Cell8.Exp9.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
    elif mat['Data'].Cell8.Expts == 10:        
        rows,cols1 = mat['Data'].Cell8.Exp1.shape
        rows,cols2 = mat['Data'].Cell8.Exp2.shape
        rows,cols3 = mat['Data'].Cell8.Exp3.shape
        rows,cols4 = mat['Data'].Cell8.Exp4.shape
        rows,cols5 = mat['Data'].Cell8.Exp5.shape
        rows,cols6 = mat['Data'].Cell8.Exp6.shape
        rows,cols7 = mat['Data'].Cell8.Exp7.shape
        rows,cols8 = mat['Data'].Cell8.Exp8.shape
        rows,cols9 = mat['Data'].Cell8.Exp9.shape
        rows,cols10 = mat['Data'].Cell8.Exp10.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
    elif mat['Data'].Cell8.Expts == 11:        
        rows,cols1 = mat['Data'].Cell8.Exp1.shape
        rows,cols2 = mat['Data'].Cell8.Exp2.shape
        rows,cols3 = mat['Data'].Cell8.Exp3.shape
        rows,cols4 = mat['Data'].Cell8.Exp4.shape
        rows,cols5 = mat['Data'].Cell8.Exp5.shape
        rows,cols6 = mat['Data'].Cell8.Exp6.shape
        rows,cols7 = mat['Data'].Cell8.Exp7.shape
        rows,cols8 = mat['Data'].Cell8.Exp8.shape
        rows,cols9 = mat['Data'].Cell8.Exp9.shape
        rows,cols10 = mat['Data'].Cell8.Exp10.shape
        rows,cols11 = mat['Data'].Cell8.Exp11.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
    elif mat['Data'].Cell8.Expts == 12:
        rows,cols1 = mat['Data'].Cell8.Exp1.shape
        rows,cols2 = mat['Data'].Cell8.Exp2.shape
        rows,cols3 = mat['Data'].Cell8.Exp3.shape
        rows,cols4 = mat['Data'].Cell8.Exp4.shape
        rows,cols5 = mat['Data'].Cell8.Exp5.shape
        rows,cols6 = mat['Data'].Cell8.Exp6.shape
        rows,cols7 = mat['Data'].Cell8.Exp7.shape
        rows,cols8 = mat['Data'].Cell8.Exp8.shape
        rows,cols9 = mat['Data'].Cell8.Exp9.shape
        rows,cols10 = mat['Data'].Cell8.Exp10.shape
        rows,cols11 = mat['Data'].Cell8.Exp11.shape
        rows,cols12 = mat['Data'].Cell8.Exp12.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
    elif mat['Data'].Cell8.Expts == 13:
        rows,cols1 = mat['Data'].Cell8.Exp1.shape
        rows,cols2 = mat['Data'].Cell8.Exp2.shape
        rows,cols3 = mat['Data'].Cell8.Exp3.shape
        rows,cols4 = mat['Data'].Cell8.Exp4.shape
        rows,cols5 = mat['Data'].Cell8.Exp5.shape
        rows,cols6 = mat['Data'].Cell8.Exp6.shape
        rows,cols7 = mat['Data'].Cell8.Exp7.shape
        rows,cols8 = mat['Data'].Cell8.Exp8.shape
        rows,cols9 = mat['Data'].Cell8.Exp9.shape
        rows,cols10 = mat['Data'].Cell8.Exp10.shape
        rows,cols11 = mat['Data'].Cell8.Exp11.shape
        rows,cols12 = mat['Data'].Cell8.Exp12.shape
        rows,cols13 = mat['Data'].Cell8.Exp13.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
    elif mat['Data'].Cell8.Expts == 14:
        rows,cols1 = mat['Data'].Cell8.Exp1.shape
        rows,cols2 = mat['Data'].Cell8.Exp2.shape
        rows,cols3 = mat['Data'].Cell8.Exp3.shape
        rows,cols4 = mat['Data'].Cell8.Exp4.shape
        rows,cols5 = mat['Data'].Cell8.Exp5.shape
        rows,cols6 = mat['Data'].Cell8.Exp6.shape
        rows,cols7 = mat['Data'].Cell8.Exp7.shape
        rows,cols8 = mat['Data'].Cell8.Exp8.shape
        rows,cols9 = mat['Data'].Cell8.Exp9.shape
        rows,cols10 = mat['Data'].Cell8.Exp10.shape
        rows,cols11 = mat['Data'].Cell8.Exp11.shape
        rows,cols12 = mat['Data'].Cell8.Exp12.shape
        rows,cols13 = mat['Data'].Cell8.Exp13.shape
        rows,cols14 = mat['Data'].Cell8.Exp14.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
        print('Experiment ' + str(14) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID14) + ' contains *** ' + str(int(cols14)) + ' *** traces.')
    elif mat['Data'].Cell8.Expts == 15:
        rows,cols1 = mat['Data'].Cell8.Exp1.shape
        rows,cols2 = mat['Data'].Cell8.Exp2.shape
        rows,cols3 = mat['Data'].Cell8.Exp3.shape
        rows,cols4 = mat['Data'].Cell8.Exp4.shape
        rows,cols5 = mat['Data'].Cell8.Exp5.shape
        rows,cols6 = mat['Data'].Cell8.Exp6.shape
        rows,cols7 = mat['Data'].Cell8.Exp7.shape
        rows,cols8 = mat['Data'].Cell8.Exp8.shape
        rows,cols9 = mat['Data'].Cell8.Exp9.shape
        rows,cols10 = mat['Data'].Cell8.Exp10.shape
        rows,cols11 = mat['Data'].Cell8.Exp11.shape
        rows,cols12 = mat['Data'].Cell8.Exp12.shape
        rows,cols13 = mat['Data'].Cell8.Exp13.shape
        rows,cols14 = mat['Data'].Cell8.Exp14.shape
        rows,cols15 = mat['Data'].Cell8.Exp15.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
        print('Experiment ' + str(14) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID14) + ' contains *** ' + str(int(cols14)) + ' *** traces.')
        print('Experiment ' + str(15) + ' is a(n) ' + str(mat['Data'].Cell8.ExptID15) + ' contains *** ' + str(int(cols15)) + ' *** traces.')
    User_choices['ExptVal'] = int(input('Which experiment would you like to analyze?:'))        

if User_choices['CellVal'] == 9:
    print('There are *** ' +str(int(mat['Data'].Cell9.Expts)) + ' *** experiments for this cell.')
    if mat['Data'].Cell9.Expts == 1:
        rows,cols1 = mat['Data'].Cell9.Exp1.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
    elif mat['Data'].Cell9.Expts == 2:
        rows,cols1 = mat['Data'].Cell9.Exp1.shape
        rows,cols2 = mat['Data'].Cell9.Exp2.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
    elif mat['Data'].Cell9.Expts == 3:
        rows,cols1 = mat['Data'].Cell9.Exp1.shape
        rows,cols2 = mat['Data'].Cell9.Exp2.shape
        rows,cols3 = mat['Data'].Cell9.Exp3.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
    elif mat['Data'].Cell9.Expts == 4:
        rows,cols1 = mat['Data'].Cell9.Exp1.shape
        rows,cols2 = mat['Data'].Cell9.Exp2.shape
        rows,cols3 = mat['Data'].Cell9.Exp3.shape
        rows,cols4 = mat['Data'].Cell9.Exp4.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
    elif mat['Data'].Cell9.Expts == 5:
        rows,cols1 = mat['Data'].Cell9.Exp1.shape
        rows,cols2 = mat['Data'].Cell9.Exp2.shape
        rows,cols3 = mat['Data'].Cell9.Exp3.shape
        rows,cols4 = mat['Data'].Cell9.Exp4.shape
        rows,cols5 = mat['Data'].Cell9.Exp5.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
    elif mat['Data'].Cell9.Expts == 6:
        rows,cols1 = mat['Data'].Cell9.Exp1.shape
        rows,cols2 = mat['Data'].Cell9.Exp2.shape
        rows,cols3 = mat['Data'].Cell9.Exp3.shape
        rows,cols4 = mat['Data'].Cell9.Exp4.shape
        rows,cols5 = mat['Data'].Cell9.Exp5.shape
        rows,cols6 = mat['Data'].Cell9.Exp6.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
    elif mat['Data'].Cell9.Expts == 7:
        rows,cols1 = mat['Data'].Cell9.Exp1.shape
        rows,cols2 = mat['Data'].Cell9.Exp2.shape
        rows,cols3 = mat['Data'].Cell9.Exp3.shape
        rows,cols4 = mat['Data'].Cell9.Exp4.shape
        rows,cols5 = mat['Data'].Cell9.Exp5.shape
        rows,cols6 = mat['Data'].Cell9.Exp6.shape
        rows,cols7 = mat['Data'].Cell9.Exp7.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')        
    elif mat['Data'].Cell9.Expts == 8:
        rows,cols1 = mat['Data'].Cell9.Exp1.shape
        rows,cols2 = mat['Data'].Cell9.Exp2.shape
        rows,cols3 = mat['Data'].Cell9.Exp3.shape
        rows,cols4 = mat['Data'].Cell9.Exp4.shape
        rows,cols5 = mat['Data'].Cell9.Exp5.shape
        rows,cols6 = mat['Data'].Cell9.Exp6.shape
        rows,cols7 = mat['Data'].Cell9.Exp7.shape
        rows,cols8 = mat['Data'].Cell9.Exp8.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
    elif mat['Data'].Cell9.Expts == 9:
        rows,cols1 = mat['Data'].Cell9.Exp1.shape
        rows,cols2 = mat['Data'].Cell9.Exp2.shape
        rows,cols3 = mat['Data'].Cell9.Exp3.shape
        rows,cols4 = mat['Data'].Cell9.Exp4.shape
        rows,cols5 = mat['Data'].Cell9.Exp5.shape
        rows,cols6 = mat['Data'].Cell9.Exp6.shape
        rows,cols7 = mat['Data'].Cell9.Exp7.shape
        rows,cols8 = mat['Data'].Cell9.Exp8.shape
        rows,cols9 = mat['Data'].Cell9.Exp9.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
    elif mat['Data'].Cell9.Expts == 10:        
        rows,cols1 = mat['Data'].Cell9.Exp1.shape
        rows,cols2 = mat['Data'].Cell9.Exp2.shape
        rows,cols3 = mat['Data'].Cell9.Exp3.shape
        rows,cols4 = mat['Data'].Cell9.Exp4.shape
        rows,cols5 = mat['Data'].Cell9.Exp5.shape
        rows,cols6 = mat['Data'].Cell9.Exp6.shape
        rows,cols7 = mat['Data'].Cell9.Exp7.shape
        rows,cols8 = mat['Data'].Cell9.Exp8.shape
        rows,cols9 = mat['Data'].Cell9.Exp9.shape
        rows,cols10 = mat['Data'].Cell9.Exp10.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
    elif mat['Data'].Cell9.Expts == 11:        
        rows,cols1 = mat['Data'].Cell9.Exp1.shape
        rows,cols2 = mat['Data'].Cell9.Exp2.shape
        rows,cols3 = mat['Data'].Cell9.Exp3.shape
        rows,cols4 = mat['Data'].Cell9.Exp4.shape
        rows,cols5 = mat['Data'].Cell9.Exp5.shape
        rows,cols6 = mat['Data'].Cell9.Exp6.shape
        rows,cols7 = mat['Data'].Cell9.Exp7.shape
        rows,cols8 = mat['Data'].Cell9.Exp8.shape
        rows,cols9 = mat['Data'].Cell9.Exp9.shape
        rows,cols10 = mat['Data'].Cell9.Exp10.shape
        rows,cols11 = mat['Data'].Cell9.Exp11.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
    elif mat['Data'].Cell9.Expts == 12:
        rows,cols1 = mat['Data'].Cell9.Exp1.shape
        rows,cols2 = mat['Data'].Cell9.Exp2.shape
        rows,cols3 = mat['Data'].Cell9.Exp3.shape
        rows,cols4 = mat['Data'].Cell9.Exp4.shape
        rows,cols5 = mat['Data'].Cell9.Exp5.shape
        rows,cols6 = mat['Data'].Cell9.Exp6.shape
        rows,cols7 = mat['Data'].Cell9.Exp7.shape
        rows,cols8 = mat['Data'].Cell9.Exp8.shape
        rows,cols9 = mat['Data'].Cell9.Exp9.shape
        rows,cols10 = mat['Data'].Cell9.Exp10.shape
        rows,cols11 = mat['Data'].Cell9.Exp11.shape
        rows,cols12 = mat['Data'].Cell9.Exp12.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
    elif mat['Data'].Cell9.Expts == 13:
        rows,cols1 = mat['Data'].Cell9.Exp1.shape
        rows,cols2 = mat['Data'].Cell9.Exp2.shape
        rows,cols3 = mat['Data'].Cell9.Exp3.shape
        rows,cols4 = mat['Data'].Cell9.Exp4.shape
        rows,cols5 = mat['Data'].Cell9.Exp5.shape
        rows,cols6 = mat['Data'].Cell9.Exp6.shape
        rows,cols7 = mat['Data'].Cell9.Exp7.shape
        rows,cols8 = mat['Data'].Cell9.Exp8.shape
        rows,cols9 = mat['Data'].Cell9.Exp9.shape
        rows,cols10 = mat['Data'].Cell9.Exp10.shape
        rows,cols11 = mat['Data'].Cell9.Exp11.shape
        rows,cols12 = mat['Data'].Cell9.Exp12.shape
        rows,cols13 = mat['Data'].Cell9.Exp13.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
    elif mat['Data'].Cell9.Expts == 14:
        rows,cols1 = mat['Data'].Cell9.Exp1.shape
        rows,cols2 = mat['Data'].Cell9.Exp2.shape
        rows,cols3 = mat['Data'].Cell9.Exp3.shape
        rows,cols4 = mat['Data'].Cell9.Exp4.shape
        rows,cols5 = mat['Data'].Cell9.Exp5.shape
        rows,cols6 = mat['Data'].Cell9.Exp6.shape
        rows,cols7 = mat['Data'].Cell9.Exp7.shape
        rows,cols8 = mat['Data'].Cell9.Exp8.shape
        rows,cols9 = mat['Data'].Cell9.Exp9.shape
        rows,cols10 = mat['Data'].Cell9.Exp10.shape
        rows,cols11 = mat['Data'].Cell9.Exp11.shape
        rows,cols12 = mat['Data'].Cell9.Exp12.shape
        rows,cols13 = mat['Data'].Cell9.Exp13.shape
        rows,cols14 = mat['Data'].Cell9.Exp14.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
        print('Experiment ' + str(14) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID14) + ' contains *** ' + str(int(cols14)) + ' *** traces.')
    elif mat['Data'].Cell9.Expts == 15:
        rows,cols1 = mat['Data'].Cell9.Exp1.shape
        rows,cols2 = mat['Data'].Cell9.Exp2.shape
        rows,cols3 = mat['Data'].Cell9.Exp3.shape
        rows,cols4 = mat['Data'].Cell9.Exp4.shape
        rows,cols5 = mat['Data'].Cell9.Exp5.shape
        rows,cols6 = mat['Data'].Cell9.Exp6.shape
        rows,cols7 = mat['Data'].Cell9.Exp7.shape
        rows,cols8 = mat['Data'].Cell9.Exp8.shape
        rows,cols9 = mat['Data'].Cell9.Exp9.shape
        rows,cols10 = mat['Data'].Cell9.Exp10.shape
        rows,cols11 = mat['Data'].Cell9.Exp11.shape
        rows,cols12 = mat['Data'].Cell9.Exp12.shape
        rows,cols13 = mat['Data'].Cell9.Exp13.shape
        rows,cols14 = mat['Data'].Cell9.Exp14.shape
        rows,cols15 = mat['Data'].Cell9.Exp15.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
        print('Experiment ' + str(14) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID14) + ' contains *** ' + str(int(cols14)) + ' *** traces.')
        print('Experiment ' + str(15) + ' is a(n) ' + str(mat['Data'].Cell9.ExptID15) + ' contains *** ' + str(int(cols15)) + ' *** traces.')
    User_choices['ExptVal'] = int(input('Which experiment would you like to analyze?:'))        

if User_choices['CellVal'] == 10:
    print('There are *** ' +str(int(mat['Data'].Cell10.Expts)) + ' *** experiments for this cell.')
    if mat['Data'].Cell10.Expts == 1:
        rows,cols1 = mat['Data'].Cell10.Exp1.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
    elif mat['Data'].Cell10.Expts == 2:
        rows,cols1 = mat['Data'].Cell10.Exp1.shape
        rows,cols2 = mat['Data'].Cell10.Exp2.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
    elif mat['Data'].Cell10.Expts == 3:
        rows,cols1 = mat['Data'].Cell10.Exp1.shape
        rows,cols2 = mat['Data'].Cell10.Exp2.shape
        rows,cols3 = mat['Data'].Cell10.Exp3.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
    elif mat['Data'].Cell10.Expts == 4:
        rows,cols1 = mat['Data'].Cell10.Exp1.shape
        rows,cols2 = mat['Data'].Cell10.Exp2.shape
        rows,cols3 = mat['Data'].Cell10.Exp3.shape
        rows,cols4 = mat['Data'].Cell10.Exp4.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
    elif mat['Data'].Cell10.Expts == 5:
        rows,cols1 = mat['Data'].Cell10.Exp1.shape
        rows,cols2 = mat['Data'].Cell10.Exp2.shape
        rows,cols3 = mat['Data'].Cell10.Exp3.shape
        rows,cols4 = mat['Data'].Cell10.Exp4.shape
        rows,cols5 = mat['Data'].Cell10.Exp5.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
    elif mat['Data'].Cell10.Expts == 6:
        rows,cols1 = mat['Data'].Cell10.Exp1.shape
        rows,cols2 = mat['Data'].Cell10.Exp2.shape
        rows,cols3 = mat['Data'].Cell10.Exp3.shape
        rows,cols4 = mat['Data'].Cell10.Exp4.shape
        rows,cols5 = mat['Data'].Cell10.Exp5.shape
        rows,cols6 = mat['Data'].Cell10.Exp6.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
    elif mat['Data'].Cell10.Expts == 7:
        rows,cols1 = mat['Data'].Cell10.Exp1.shape
        rows,cols2 = mat['Data'].Cell10.Exp2.shape
        rows,cols3 = mat['Data'].Cell10.Exp3.shape
        rows,cols4 = mat['Data'].Cell10.Exp4.shape
        rows,cols5 = mat['Data'].Cell10.Exp5.shape
        rows,cols6 = mat['Data'].Cell10.Exp6.shape
        rows,cols7 = mat['Data'].Cell10.Exp7.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')        
    elif mat['Data'].Cell10.Expts == 8:
        rows,cols1 = mat['Data'].Cell10.Exp1.shape
        rows,cols2 = mat['Data'].Cell10.Exp2.shape
        rows,cols3 = mat['Data'].Cell10.Exp3.shape
        rows,cols4 = mat['Data'].Cell10.Exp4.shape
        rows,cols5 = mat['Data'].Cell10.Exp5.shape
        rows,cols6 = mat['Data'].Cell10.Exp6.shape
        rows,cols7 = mat['Data'].Cell10.Exp7.shape
        rows,cols8 = mat['Data'].Cell10.Exp8.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
    elif mat['Data'].Cell10.Expts == 9:
        rows,cols1 = mat['Data'].Cell10.Exp1.shape
        rows,cols2 = mat['Data'].Cell10.Exp2.shape
        rows,cols3 = mat['Data'].Cell10.Exp3.shape
        rows,cols4 = mat['Data'].Cell10.Exp4.shape
        rows,cols5 = mat['Data'].Cell10.Exp5.shape
        rows,cols6 = mat['Data'].Cell10.Exp6.shape
        rows,cols7 = mat['Data'].Cell10.Exp7.shape
        rows,cols8 = mat['Data'].Cell10.Exp8.shape
        rows,cols9 = mat['Data'].Cell10.Exp9.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
    elif mat['Data'].Cell10.Expts == 10:        
        rows,cols1 = mat['Data'].Cell10.Exp1.shape
        rows,cols2 = mat['Data'].Cell10.Exp2.shape
        rows,cols3 = mat['Data'].Cell10.Exp3.shape
        rows,cols4 = mat['Data'].Cell10.Exp4.shape
        rows,cols5 = mat['Data'].Cell10.Exp5.shape
        rows,cols6 = mat['Data'].Cell10.Exp6.shape
        rows,cols7 = mat['Data'].Cell10.Exp7.shape
        rows,cols8 = mat['Data'].Cell10.Exp8.shape
        rows,cols9 = mat['Data'].Cell10.Exp9.shape
        rows,cols10 = mat['Data'].Cell10.Exp10.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
    elif mat['Data'].Cell10.Expts == 11:        
        rows,cols1 = mat['Data'].Cell10.Exp1.shape
        rows,cols2 = mat['Data'].Cell10.Exp2.shape
        rows,cols3 = mat['Data'].Cell10.Exp3.shape
        rows,cols4 = mat['Data'].Cell10.Exp4.shape
        rows,cols5 = mat['Data'].Cell10.Exp5.shape
        rows,cols6 = mat['Data'].Cell10.Exp6.shape
        rows,cols7 = mat['Data'].Cell10.Exp7.shape
        rows,cols8 = mat['Data'].Cell10.Exp8.shape
        rows,cols9 = mat['Data'].Cell10.Exp9.shape
        rows,cols10 = mat['Data'].Cell10.Exp10.shape
        rows,cols11 = mat['Data'].Cell10.Exp11.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
    elif mat['Data'].Cell10.Expts == 12:
        rows,cols1 = mat['Data'].Cell10.Exp1.shape
        rows,cols2 = mat['Data'].Cell10.Exp2.shape
        rows,cols3 = mat['Data'].Cell10.Exp3.shape
        rows,cols4 = mat['Data'].Cell10.Exp4.shape
        rows,cols5 = mat['Data'].Cell10.Exp5.shape
        rows,cols6 = mat['Data'].Cell10.Exp6.shape
        rows,cols7 = mat['Data'].Cell10.Exp7.shape
        rows,cols8 = mat['Data'].Cell10.Exp8.shape
        rows,cols9 = mat['Data'].Cell10.Exp9.shape
        rows,cols10 = mat['Data'].Cell10.Exp10.shape
        rows,cols11 = mat['Data'].Cell10.Exp11.shape
        rows,cols12 = mat['Data'].Cell10.Exp12.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
    elif mat['Data'].Cell10.Expts == 13:
        rows,cols1 = mat['Data'].Cell10.Exp1.shape
        rows,cols2 = mat['Data'].Cell10.Exp2.shape
        rows,cols3 = mat['Data'].Cell10.Exp3.shape
        rows,cols4 = mat['Data'].Cell10.Exp4.shape
        rows,cols5 = mat['Data'].Cell10.Exp5.shape
        rows,cols6 = mat['Data'].Cell10.Exp6.shape
        rows,cols7 = mat['Data'].Cell10.Exp7.shape
        rows,cols8 = mat['Data'].Cell10.Exp8.shape
        rows,cols9 = mat['Data'].Cell10.Exp9.shape
        rows,cols10 = mat['Data'].Cell10.Exp10.shape
        rows,cols11 = mat['Data'].Cell10.Exp11.shape
        rows,cols12 = mat['Data'].Cell10.Exp12.shape
        rows,cols13 = mat['Data'].Cell10.Exp13.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
    elif mat['Data'].Cell10.Expts == 14:
        rows,cols1 = mat['Data'].Cell10.Exp1.shape
        rows,cols2 = mat['Data'].Cell10.Exp2.shape
        rows,cols3 = mat['Data'].Cell10.Exp3.shape
        rows,cols4 = mat['Data'].Cell10.Exp4.shape
        rows,cols5 = mat['Data'].Cell10.Exp5.shape
        rows,cols6 = mat['Data'].Cell10.Exp6.shape
        rows,cols7 = mat['Data'].Cell10.Exp7.shape
        rows,cols8 = mat['Data'].Cell10.Exp8.shape
        rows,cols9 = mat['Data'].Cell10.Exp9.shape
        rows,cols10 = mat['Data'].Cell10.Exp10.shape
        rows,cols11 = mat['Data'].Cell10.Exp11.shape
        rows,cols12 = mat['Data'].Cell10.Exp12.shape
        rows,cols13 = mat['Data'].Cell10.Exp13.shape
        rows,cols14 = mat['Data'].Cell10.Exp14.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
        print('Experiment ' + str(14) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID14) + ' contains *** ' + str(int(cols14)) + ' *** traces.')
    elif mat['Data'].Cell10.Expts == 15:
        rows,cols1 = mat['Data'].Cell10.Exp1.shape
        rows,cols2 = mat['Data'].Cell10.Exp2.shape
        rows,cols3 = mat['Data'].Cell10.Exp3.shape
        rows,cols4 = mat['Data'].Cell10.Exp4.shape
        rows,cols5 = mat['Data'].Cell10.Exp5.shape
        rows,cols6 = mat['Data'].Cell10.Exp6.shape
        rows,cols7 = mat['Data'].Cell10.Exp7.shape
        rows,cols8 = mat['Data'].Cell10.Exp8.shape
        rows,cols9 = mat['Data'].Cell10.Exp9.shape
        rows,cols10 = mat['Data'].Cell10.Exp10.shape
        rows,cols11 = mat['Data'].Cell10.Exp11.shape
        rows,cols12 = mat['Data'].Cell10.Exp12.shape
        rows,cols13 = mat['Data'].Cell10.Exp13.shape
        rows,cols14 = mat['Data'].Cell10.Exp14.shape
        rows,cols15 = mat['Data'].Cell10.Exp15.shape
        print('Experiment ' + str(1) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID1) + ' contains *** ' + str(int(cols1)) + ' *** traces.')
        print('Experiment ' + str(2) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID2) + ' contains *** ' + str(int(cols2)) + ' *** traces.')
        print('Experiment ' + str(3) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID3) + ' contains *** ' + str(int(cols3)) + ' *** traces.')
        print('Experiment ' + str(4) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID4) + ' contains *** ' + str(int(cols4)) + ' *** traces.')
        print('Experiment ' + str(5) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID5) + ' contains *** ' + str(int(cols5)) + ' *** traces.')
        print('Experiment ' + str(6) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID6) + ' contains *** ' + str(int(cols6)) + ' *** traces.')
        print('Experiment ' + str(7) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID7) + ' contains *** ' + str(int(cols7)) + ' *** traces.')
        print('Experiment ' + str(8) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID8) + ' contains *** ' + str(int(cols8)) + ' *** traces.')
        print('Experiment ' + str(9) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID9) + ' contains *** ' + str(int(cols9)) + ' *** traces.')
        print('Experiment ' + str(10) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID10) + ' contains *** ' + str(int(cols10)) + ' *** traces.')
        print('Experiment ' + str(11) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID11) + ' contains *** ' + str(int(cols11)) + ' *** traces.')
        print('Experiment ' + str(12) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID12) + ' contains *** ' + str(int(cols12)) + ' *** traces.')
        print('Experiment ' + str(13) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID13) + ' contains *** ' + str(int(cols13)) + ' *** traces.')
        print('Experiment ' + str(14) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID14) + ' contains *** ' + str(int(cols14)) + ' *** traces.')
        print('Experiment ' + str(15) + ' is a(n) ' + str(mat['Data'].Cell10.ExptID15) + ' contains *** ' + str(int(cols15)) + ' *** traces.')
    User_choices['ExptVal'] = int(input('Which experiment would you like to analyze?:'))
    
#Extracts relevant data from nested matlab structure and stores in a similarly named variable "Data"
#This dictionary contains the appropriate information including Raw Data, Stim, Trace Max, and Time
if User_choices['CellVal'] == 1:
    if User_choices['ExptVal'] == 1 and mat['Data'].Cell1.ExptID1 == 'IV':
        Data['Raw'] = mat['Data'].Cell1.Exp1
        Data['Stim'] = mat['Data'].Cell1.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell1.ExptID1 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell1.Exp1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell1.ExptID1 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell1.Exp1
        Data['Stim'] = mat['Data'].Cell1.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell1.ExptID1 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell1.Exp1
        Data['Stim'] = mat['Data'].Cell1.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell1.ExptID1 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell1.Exp1
        Data['Stim'] = mat['Data'].Cell1.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell.ExptID1 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell1.Exp1
        Data['Stim'] = mat['Data'].Cell1.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell1.ExptID1 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell1.Exp1
        Data['Stim'] = mat['Data'].Cell1.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell1.ExptID1 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell1.Exp1
        Data['Stim'] = mat['Data'].Cell1.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell1.ExptID1 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell1.Exp1
        Data['Stim'] = mat['Data'].Cell1.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 2 and mat['Data'].Cell1.ExptID2 == 'IV':
        Data['Raw'] = mat['Data'].Cell1.Exp2
        Data['Stim'] = mat['Data'].Cell1.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell1.ExptID2 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell1.Exp2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell1.ExptID2 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell1.Exp2
        Data['Stim'] = mat['Data'].Cell1.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell1.ExptID2 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell1.Exp2
        Data['Stim'] = mat['Data'].Cell1.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell1.ExptID2 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell1.Exp2
        Data['Stim'] = mat['Data'].Cell1.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell1.ExptID2 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell1.Exp2
        Data['Stim'] = mat['Data'].Cell1.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell1.ExptID2 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell1.Exp2
        Data['Stim'] = mat['Data'].Cell1.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell1.ExptID2 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell1.Exp2
        Data['Stim'] = mat['Data'].Cell1.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell1.ExptID2 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell2.Exp2
        Data['Stim'] = mat['Data'].Cell2.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 3 and mat['Data'].Cell1.ExptID3 == 'IV':
        Data['Raw'] = mat['Data'].Cell1.Exp3
        Data['Stim'] = mat['Data'].Cell1.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell1.ExptID3 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell1.Exp3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell1.ExptID3 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell1.Exp3
        Data['Stim'] = mat['Data'].Cell1.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell1.ExptID3 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell1.Exp3
        Data['Stim'] = mat['Data'].Cell1.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell1.ExptID3 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell1.Exp3
        Data['Stim'] = mat['Data'].Cell1.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell1.ExptID3 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell1.Exp3
        Data['Stim'] = mat['Data'].Cell1.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell1.ExptID3 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell1.Exp3
        Data['Stim'] = mat['Data'].Cell1.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell1.ExptID3 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell1.Exp3
        Data['Stim'] = mat['Data'].Cell1.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell1.ExptID3 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell1.Exp3
        Data['Stim'] = mat['Data'].Cell1.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
    
    if User_choices['ExptVal'] == 4 and mat['Data'].Cell1.ExptID4 == 'IV':
        Data['Raw'] = mat['Data'].Cell1.Exp4
        Data['Stim'] = mat['Data'].Cell1.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell1.ExptID4 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell1.Exp4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell1.ExptID4 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell1.Exp4
        Data['Stim'] = mat['Data'].Cell1.Stim4
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell1.ExptID4 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell1.Exp4
        Data['Stim'] = mat['Data'].Cell1.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell1.ExptID4 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell1.Exp4
        Data['Stim'] = mat['Data'].Cell1.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell1.ExptID4 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell1.Exp4
        Data['Stim'] = mat['Data'].Cell1.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell1.ExptID4 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell1.Exp4
        Data['Stim'] = mat['Data'].Cell1.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell1.ExptID4 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell1.Exp4
        Data['Stim'] = mat['Data'].Cell1.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell1.ExptID4 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell1.Exp4
        Data['Stim'] = mat['Data'].Cell1.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 5 and mat['Data'].Cell1.ExptID5 == 'IV':
        Data['Raw'] = mat['Data'].Cell1.Exp5
        Data['Stim'] = mat['Data'].Cell1.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell1.ExptID5 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell1.Exp5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell1.ExptID5 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell1.Exp5
        Data['Stim'] = mat['Data'].Cell1.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell1.ExptID5 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell1.Exp5
        Data['Stim'] = mat['Data'].Cell1.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell1.ExptID5 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell1.Exp5
        Data['Stim'] = mat['Data'].Cell1.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell1.ExptID5 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell1.Exp5
        Data['Stim'] = mat['Data'].Cell1.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell1.ExptID5 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell1.Exp5
        Data['Stim'] = mat['Data'].Cell1.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell1.ExptID5 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell1.Exp5
        Data['Stim'] = mat['Data'].Cell1.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell1.ExptID5 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell1.Exp5
        Data['Stim'] = mat['Data'].Cell1.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]        
        
    if User_choices['ExptVal'] == 6 and mat['Data'].Cell1.ExptID6 == 'IV':
        Data['Raw'] = mat['Data'].Cell1.Exp6
        Data['Stim'] = mat['Data'].Cell1.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell1.ExptID6 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell1.Exp6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell1.ExptID6 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell1.Exp6
        Data['Stim'] = mat['Data'].Cell1.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell1.ExptID6 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell1.Exp6
        Data['Stim'] = mat['Data'].Cell1.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell1.ExptID6 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell1.Exp6
        Data['Stim'] = mat['Data'].Cell1.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell1.ExptID6 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell1.Exp6
        Data['Stim'] = mat['Data'].Cell1.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell1.ExptID6 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell1.Exp6
        Data['Stim'] = mat['Data'].Cell1.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell1.ExptID6 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell1.Exp6
        Data['Stim'] = mat['Data'].Cell1.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell1.ExptID6 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell1.Exp6
        Data['Stim'] = mat['Data'].Cell1.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]        
        
    if User_choices['ExptVal'] == 7 and mat['Data'].Cell1.ExptID7 == 'IV':
        Data['Raw'] = mat['Data'].Cell1.Exp7
        Data['Stim'] = mat['Data'].Cell1.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell1.ExptID7 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell1.Exp7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell1.ExptID7 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell1.Exp7
        Data['Stim'] = mat['Data'].Cell1.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell1.ExptID7 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell1.Exp7
        Data['Stim'] = mat['Data'].Cell1.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell1.ExptID7 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell1.Exp7
        Data['Stim'] = mat['Data'].Cell1.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell1.ExptID7 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell1.Exp7
        Data['Stim'] = mat['Data'].Cell1.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell1.ExptID7 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell1.Exp7
        Data['Stim'] = mat['Data'].Cell1.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell1.ExptID7 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell1.Exp7
        Data['Stim'] = mat['Data'].Cell1.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell1.ExptID7 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell1.Exp7
        Data['Stim'] = mat['Data'].Cell1.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 8 and mat['Data'].Cell1.ExptID8 == 'IV':
        Data['Raw'] = mat['Data'].Cell1.Exp8
        Data['Stim'] = mat['Data'].Cell1.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell1.ExptID8 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell1.Exp8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell1.ExptID8 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell1.Exp8
        Data['Stim'] = mat['Data'].Cell1.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell1.ExptID8 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell1.Exp8
        Data['Stim'] = mat['Data'].Cell1.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell1.ExptID8 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell1.Exp8
        Data['Stim'] = mat['Data'].Cell1.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell1.ExptID8 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell1.Exp8
        Data['Stim'] = mat['Data'].Cell1.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell1.ExptID8 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell1.Exp8
        Data['Stim'] = mat['Data'].Cell1.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell1.ExptID8 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell1.Exp8
        Data['Stim'] = mat['Data'].Cell1.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell1.ExptID8 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell1.Exp8
        Data['Stim'] = mat['Data'].Cell1.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
    
    if User_choices['ExptVal'] == 9 and mat['Data'].Cell1.ExptID9 == 'IV':
        Data['Raw'] = mat['Data'].Cell1.Exp9
        Data['Stim'] = mat['Data'].Cell1.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell1.ExptID9 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell1.Exp9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell1.ExptID9 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell1.Exp9
        Data['Stim'] = mat['Data'].Cell1.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell1.ExptID9 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell1.Exp9
        Data['Stim'] = mat['Data'].Cell1.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell1.ExptID9 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell1.Exp9
        Data['Stim'] = mat['Data'].Cell1.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell1.ExptID9 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell1.Exp9
        Data['Stim'] = mat['Data'].Cell1.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell1.ExptID9 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell1.Exp9
        Data['Stim'] = mat['Data'].Cell1.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell1.ExptID9 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell1.Exp9
        Data['Stim'] = mat['Data'].Cell1.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell1.ExptID9 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell1.Exp9
        Data['Stim'] = mat['Data'].Cell1.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 10 and mat['Data'].Cell1.ExptID10 == 'IV':
        Data['Raw'] = mat['Data'].Cell1.Exp10
        Data['Stim'] = mat['Data'].Cell1.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell1.ExptID10 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell1.Exp10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell1.ExptID10 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell1.Exp10
        Data['Stim'] = mat['Data'].Cell1.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell1.ExptID10 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell1.Exp10
        Data['Stim'] = mat['Data'].Cell1.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell1.ExptID10 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell1.Exp10
        Data['Stim'] = mat['Data'].Cell1.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell1.ExptID10 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell1.Exp10
        Data['Stim'] = mat['Data'].Cell1.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell1.ExptID10 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell1.Exp10
        Data['Stim'] = mat['Data'].Cell1.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell1.ExptID10 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell1.Exp10
        Data['Stim'] = mat['Data'].Cell1.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell1.ExptID10 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell1.Exp10
        Data['Stim'] = mat['Data'].Cell1.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 11 and mat['Data'].Cell1.ExptID11 == 'IV':
        Data['Raw'] = mat['Data'].Cell1.Exp11
        Data['Stim'] = mat['Data'].Cell1.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell1.ExptID11 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell1.Exp11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell1.ExptID11 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell1.Exp11
        Data['Stim'] = mat['Data'].Cell1.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell1.ExptID11 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell1.Exp11
        Data['Stim'] = mat['Data'].Cell1.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell1.ExptID11 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell1.Exp11
        Data['Stim'] = mat['Data'].Cell1.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell1.ExptID11 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell1.Exp11
        Data['Stim'] = mat['Data'].Cell1.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell1.ExptID11 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell1.Exp11
        Data['Stim'] = mat['Data'].Cell1.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell1.ExptID11 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell1.Exp11
        Data['Stim'] = mat['Data'].Cell1.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell1.ExptID11 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell1.Exp11
        Data['Stim'] = mat['Data'].Cell1.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 12 and mat['Data'].Cell1.ExptID12 == 'IV':
        Data['Raw'] = mat['Data'].Cell1.Exp12
        Data['Stim'] = mat['Data'].Cell1.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell1.ExptID12 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell1.Exp12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell1.ExptID12 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell1.Exp12
        Data['Stim'] = mat['Data'].Cell1.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell1.ExptID12 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell1.Exp12
        Data['Stim'] = mat['Data'].Cell1.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell1.ExptID12 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell1.Exp12
        Data['Stim'] = mat['Data'].Cell1.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell1.ExptID12 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell1.Exp12
        Data['Stim'] = mat['Data'].Cell1.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell1.ExptID12 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell1.Exp12
        Data['Stim'] = mat['Data'].Cell1.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell1.ExptID12 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell1.Exp12
        Data['Stim'] = mat['Data'].Cell1.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell1.ExptID12 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell1.Exp12
        Data['Stim'] = mat['Data'].Cell1.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 13 and mat['Data'].Cell1.ExptID13 == 'IV':
        Data['Raw'] = mat['Data'].Cell1.Exp13
        Data['Stim'] = mat['Data'].Cell1.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell1.ExptID13 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell1.Exp13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell1.ExptID13 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell1.Exp13
        Data['Stim'] = mat['Data'].Cell1.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell1.ExptID13 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell1.Exp13
        Data['Stim'] = mat['Data'].Cell1.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell1.ExptID13 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell1.Exp13
        Data['Stim'] = mat['Data'].Cell1.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell1.ExptID13 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell1.Exp13
        Data['Stim'] = mat['Data'].Cell1.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell1.ExptID13 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell1.Exp13
        Data['Stim'] = mat['Data'].Cell1.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell1.ExptID13 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell1.Exp13
        Data['Stim'] = mat['Data'].Cell1.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell1.ExptID13 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell1.Exp13
        Data['Stim'] = mat['Data'].Cell1.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 14 and mat['Data'].Cell1.ExptID14 == 'IV':
        Data['Raw'] = mat['Data'].Cell1.Exp14
        Data['Stim'] = mat['Data'].Cell1.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell1.ExptID14 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell1.Exp14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell1.ExptI4 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell1.Exp14
        Data['Stim'] = mat['Data'].Cell1.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell1.ExptID14 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell1.Exp14
        Data['Stim'] = mat['Data'].Cell1.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell1.ExptID14 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell1.Exp14
        Data['Stim'] = mat['Data'].Cell1.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell1.ExptID14 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell1.Exp14
        Data['Stim'] = mat['Data'].Cell1.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell1.ExptID14 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell1.Exp14
        Data['Stim'] = mat['Data'].Cell1.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell1.ExptID14 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell1.Exp14
        Data['Stim'] = mat['Data'].Cell1.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell1.ExptID14 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell1.Exp14
        Data['Stim'] = mat['Data'].Cell1.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 15 and mat['Data'].Cell1.ExptID15== 'IV':
        Data['Raw'] = mat['Data'].Cell1.Exp15
        Data['Stim'] = mat['Data'].Cell1.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell1.ExptID15 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell1.Exp15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell1.ExptID15 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell1.Exp15
        Data['Stim'] = mat['Data'].Cell1.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell1.ExptID15 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell1.Exp15
        Data['Stim'] = mat['Data'].Cell1.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell1.ExptID15== 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell1.Exp15
        Data['Stim'] = mat['Data'].Cell1.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell1.ExptID15 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell1.Exp15
        Data['Stim'] = mat['Data'].Cell1.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell1.ExptID15 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell1.Exp15
        Data['Stim'] = mat['Data'].Cell1.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell1.ExptID15 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell1.Exp15
        Data['Stim'] = mat['Data'].Cell1.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell1.ExptID15 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell1.Exp15
        Data['Stim'] = mat['Data'].Cell1.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
if User_choices['CellVal'] == 2:
    if User_choices['ExptVal'] == 1 and mat['Data'].Cell2.ExptID1 == 'IV':
        Data['Raw'] = mat['Data'].Cell2.Exp1
        Data['Stim'] = mat['Data'].Cell2.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell2.ExptID1 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell2.Exp1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell2.ExptID1 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell2.Exp1
        Data['Stim'] = mat['Data'].Cell2.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell2.ExptID1 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell2.Exp1
        Data['Stim'] = mat['Data'].Cell2.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell2.ExptID1 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell2.Exp1
        Data['Stim'] = mat['Data'].Cell2.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell.ExptID1 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell2.Exp1
        Data['Stim'] = mat['Data'].Cell2.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell2.ExptID1 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell2.Exp1
        Data['Stim'] = mat['Data'].Cell2.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell2.ExptID1 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell2.Exp1
        Data['Stim'] = mat['Data'].Cell2.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell2.ExptID1 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell2.Exp1
        Data['Stim'] = mat['Data'].Cell2.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 2 and mat['Data'].Cell2.ExptID2 == 'IV':
        Data['Raw'] = mat['Data'].Cell2.Exp2
        Data['Stim'] = mat['Data'].Cell2.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell2.ExptID2 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell2.Exp2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell2.ExptID2 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell2.Exp2
        Data['Stim'] = mat['Data'].Cell2.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell2.ExptID2 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell2.Exp2
        Data['Stim'] = mat['Data'].Cell2.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell2.ExptID2 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell2.Exp2
        Data['Stim'] = mat['Data'].Cell2.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell2.ExptID2 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell2.Exp2
        Data['Stim'] = mat['Data'].Cell2.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell2.ExptID2 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell2.Exp2
        Data['Stim'] = mat['Data'].Cell2.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell2.ExptID2 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell2.Exp2
        Data['Stim'] = mat['Data'].Cell2.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell2.ExptID2 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell2.Exp2
        Data['Stim'] = mat['Data'].Cell2.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 3 and mat['Data'].Cell2.ExptID3 == 'IV':
        Data['Raw'] = mat['Data'].Cell2.Exp3
        Data['Stim'] = mat['Data'].Cell2.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell2.ExptID3 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell2.Exp3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell2.ExptID3 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell2.Exp3
        Data['Stim'] = mat['Data'].Cell2.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell2.ExptID3 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell2.Exp3
        Data['Stim'] = mat['Data'].Cell2.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell2.ExptID3 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell2.Exp3
        Data['Stim'] = mat['Data'].Cell2.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell2.ExptID3 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell2.Exp3
        Data['Stim'] = mat['Data'].Cell2.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell2.ExptID3 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell2.Exp3
        Data['Stim'] = mat['Data'].Cell2.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell2.ExptID3 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell2.Exp3
        Data['Stim'] = mat['Data'].Cell2.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell2.ExptID3 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell2.Exp3
        Data['Stim'] = mat['Data'].Cell2.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
    
    if User_choices['ExptVal'] == 4 and mat['Data'].Cell2.ExptID4 == 'IV':
        Data['Raw'] = mat['Data'].Cell2.Exp4
        Data['Stim'] = mat['Data'].Cell2.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell2.ExptID4 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell2.Exp4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell2.ExptID4 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell2.Exp4
        Data['Stim'] = mat['Data'].Cell2.Stim4
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell2.ExptID4 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell2.Exp4
        Data['Stim'] = mat['Data'].Cell2.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell2.ExptID4 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell2.Exp4
        Data['Stim'] = mat['Data'].Cell2.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell2.ExptID4 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell2.Exp4
        Data['Stim'] = mat['Data'].Cell2.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell2.ExptID4 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell2.Exp4
        Data['Stim'] = mat['Data'].Cell2.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell2.ExptID4 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell2.Exp4
        Data['Stim'] = mat['Data'].Cell2.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell2.ExptID4 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell2.Exp4
        Data['Stim'] = mat['Data'].Cell2.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 5 and mat['Data'].Cell2.ExptID5 == 'IV':
        Data['Raw'] = mat['Data'].Cell2.Exp5
        Data['Stim'] = mat['Data'].Cell2.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell2.ExptID5 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell2.Exp5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell2.ExptID5 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell2.Exp5
        Data['Stim'] = mat['Data'].Cell2.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell2.ExptID5 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell2.Exp5
        Data['Stim'] = mat['Data'].Cell2.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell2.ExptID5 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell2.Exp5
        Data['Stim'] = mat['Data'].Cell2.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell2.ExptID5 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell2.Exp5
        Data['Stim'] = mat['Data'].Cell2.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell2.ExptID5 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell2.Exp5
        Data['Stim'] = mat['Data'].Cell2.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell2.ExptID5 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell2.Exp5
        Data['Stim'] = mat['Data'].Cell2.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell2.ExptID5 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell2.Exp5
        Data['Stim'] = mat['Data'].Cell2.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]        
        
    if User_choices['ExptVal'] == 6 and mat['Data'].Cell2.ExptID6 == 'IV':
        Data['Raw'] = mat['Data'].Cell2.Exp6
        Data['Stim'] = mat['Data'].Cell2.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell2.ExptID6 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell2.Exp6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell2.ExptID6 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell2.Exp6
        Data['Stim'] = mat['Data'].Cell2.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell2.ExptID6 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell2.Exp6
        Data['Stim'] = mat['Data'].Cell2.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell2.ExptID6 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell2.Exp6
        Data['Stim'] = mat['Data'].Cell2.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell2.ExptID6 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell2.Exp6
        Data['Stim'] = mat['Data'].Cell2.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell2.ExptID6 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell2.Exp6
        Data['Stim'] = mat['Data'].Cell2.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell2.ExptID6 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell2.Exp6
        Data['Stim'] = mat['Data'].Cell2.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell2.ExptID6 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell2.Exp6
        Data['Stim'] = mat['Data'].Cell2.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]        
        
    if User_choices['ExptVal'] == 7 and mat['Data'].Cell2.ExptID7 == 'IV':
        Data['Raw'] = mat['Data'].Cell2.Exp7
        Data['Stim'] = mat['Data'].Cell2.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell2.ExptID7 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell2.Exp7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell2.ExptID7 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell2.Exp7
        Data['Stim'] = mat['Data'].Cell2.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell2.ExptID7 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell2.Exp7
        Data['Stim'] = mat['Data'].Cell2.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell2.ExptID7 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell2.Exp7
        Data['Stim'] = mat['Data'].Cell2.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell2.ExptID7 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell2.Exp7
        Data['Stim'] = mat['Data'].Cell2.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell2.ExptID7 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell2.Exp7
        Data['Stim'] = mat['Data'].Cell2.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell2.ExptID7 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell2.Exp7
        Data['Stim'] = mat['Data'].Cell2.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell2.ExptID7 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell2.Exp7
        Data['Stim'] = mat['Data'].Cell2.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 8 and mat['Data'].Cell2.ExptID8 == 'IV':
        Data['Raw'] = mat['Data'].Cell2.Exp8
        Data['Stim'] = mat['Data'].Cell2.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell2.ExptID8 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell2.Exp8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell2.ExptID8 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell2.Exp8
        Data['Stim'] = mat['Data'].Cell2.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell2.ExptID8 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell2.Exp8
        Data['Stim'] = mat['Data'].Cell2.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell2.ExptID8 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell2.Exp8
        Data['Stim'] = mat['Data'].Cell2.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell2.ExptID8 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell2.Exp8
        Data['Stim'] = mat['Data'].Cell2.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell2.ExptID8 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell2.Exp8
        Data['Stim'] = mat['Data'].Cell2.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell2.ExptID8 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell2.Exp8
        Data['Stim'] = mat['Data'].Cell2.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell2.ExptID8 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell2.Exp8
        Data['Stim'] = mat['Data'].Cell2.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
    
    if User_choices['ExptVal'] == 9 and mat['Data'].Cell2.ExptID9 == 'IV':
        Data['Raw'] = mat['Data'].Cell2.Exp9
        Data['Stim'] = mat['Data'].Cell2.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell2.ExptID9 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell2.Exp9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell2.ExptID9 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell2.Exp9
        Data['Stim'] = mat['Data'].Cell2.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell2.ExptID9 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell2.Exp9
        Data['Stim'] = mat['Data'].Cell2.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell2.ExptID9 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell2.Exp9
        Data['Stim'] = mat['Data'].Cell2.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell2.ExptID9 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell2.Exp9
        Data['Stim'] = mat['Data'].Cell2.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell2.ExptID9 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell2.Exp9
        Data['Stim'] = mat['Data'].Cell2.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell2.ExptID9 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell2.Exp9
        Data['Stim'] = mat['Data'].Cell2.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell2.ExptID9 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell2.Exp9
        Data['Stim'] = mat['Data'].Cell2.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 10 and mat['Data'].Cell2.ExptID10 == 'IV':
        Data['Raw'] = mat['Data'].Cell2.Exp10
        Data['Stim'] = mat['Data'].Cell2.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell2.ExptID10 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell2.Exp10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell2.ExptID10 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell2.Exp10
        Data['Stim'] = mat['Data'].Cell2.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell2.ExptID10 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell2.Exp10
        Data['Stim'] = mat['Data'].Cell2.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell2.ExptID10 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell2.Exp10
        Data['Stim'] = mat['Data'].Cell2.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell2.ExptID10 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell2.Exp10
        Data['Stim'] = mat['Data'].Cell2.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell2.ExptID10 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell2.Exp10
        Data['Stim'] = mat['Data'].Cell2.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell2.ExptID10 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell2.Exp10
        Data['Stim'] = mat['Data'].Cell2.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell2.ExptID10 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell2.Exp10
        Data['Stim'] = mat['Data'].Cell2.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 11 and mat['Data'].Cell2.ExptID11 == 'IV':
        Data['Raw'] = mat['Data'].Cell2.Exp11
        Data['Stim'] = mat['Data'].Cell2.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell2.ExptID11 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell2.Exp11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell2.ExptID11 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell2.Exp11
        Data['Stim'] = mat['Data'].Cell2.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell2.ExptID11 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell2.Exp11
        Data['Stim'] = mat['Data'].Cell2.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell2.ExptID11 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell2.Exp11
        Data['Stim'] = mat['Data'].Cell2.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell2.ExptID11 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell2.Exp11
        Data['Stim'] = mat['Data'].Cell2.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell2.ExptID11 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell2.Exp11
        Data['Stim'] = mat['Data'].Cell2.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell2.ExptID11 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell2.Exp11
        Data['Stim'] = mat['Data'].Cell2.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell2.ExptID11 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell2.Exp11
        Data['Stim'] = mat['Data'].Cell2.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 12 and mat['Data'].Cell2.ExptID12 == 'IV':
        Data['Raw'] = mat['Data'].Cell2.Exp12
        Data['Stim'] = mat['Data'].Cell2.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell2.ExptID12 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell2.Exp12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell2.ExptID12 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell2.Exp12
        Data['Stim'] = mat['Data'].Cell2.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell2.ExptID12 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell2.Exp12
        Data['Stim'] = mat['Data'].Cell2.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell2.ExptID12 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell2.Exp12
        Data['Stim'] = mat['Data'].Cell2.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell2.ExptID12 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell2.Exp12
        Data['Stim'] = mat['Data'].Cell2.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell2.ExptID12 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell2.Exp12
        Data['Stim'] = mat['Data'].Cell2.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell2.ExptID12 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell2.Exp12
        Data['Stim'] = mat['Data'].Cell2.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell2.ExptID12 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell2.Exp12
        Data['Stim'] = mat['Data'].Cell2.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 13 and mat['Data'].Cell2.ExptID13 == 'IV':
        Data['Raw'] = mat['Data'].Cell2.Exp13
        Data['Stim'] = mat['Data'].Cell2.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell2.ExptID13 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell2.Exp13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell2.ExptID13 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell2.Exp13
        Data['Stim'] = mat['Data'].Cell2.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell2.ExptID13 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell2.Exp13
        Data['Stim'] = mat['Data'].Cell2.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell2.ExptID13 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell2.Exp13
        Data['Stim'] = mat['Data'].Cell2.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell2.ExptID13 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell2.Exp13
        Data['Stim'] = mat['Data'].Cell2.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell2.ExptID13 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell2.Exp13
        Data['Stim'] = mat['Data'].Cell2.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell2.ExptID13 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell2.Exp13
        Data['Stim'] = mat['Data'].Cell2.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell2.ExptID13 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell2.Exp13
        Data['Stim'] = mat['Data'].Cell2.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 14 and mat['Data'].Cell2.ExptID14 == 'IV':
        Data['Raw'] = mat['Data'].Cell2.Exp14
        Data['Stim'] = mat['Data'].Cell2.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell2.ExptID14 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell2.Exp14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell2.ExptI4 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell2.Exp14
        Data['Stim'] = mat['Data'].Cell2.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell2.ExptID14 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell2.Exp14
        Data['Stim'] = mat['Data'].Cell2.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell2.ExptID14 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell2.Exp14
        Data['Stim'] = mat['Data'].Cell2.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell2.ExptID14 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell2.Exp14
        Data['Stim'] = mat['Data'].Cell2.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell2.ExptID14 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell2.Exp14
        Data['Stim'] = mat['Data'].Cell2.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell2.ExptID14 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell2.Exp14
        Data['Stim'] = mat['Data'].Cell2.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell2.ExptID14 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell2.Exp14
        Data['Stim'] = mat['Data'].Cell2.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 15 and mat['Data'].Cell2.ExptID15== 'IV':
        Data['Raw'] = mat['Data'].Cell2.Exp15
        Data['Stim'] = mat['Data'].Cell2.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell2.ExptID15 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell2.Exp15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell2.ExptID15 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell2.Exp15
        Data['Stim'] = mat['Data'].Cell2.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell2.ExptID15 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell2.Exp15
        Data['Stim'] = mat['Data'].Cell2.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell2.ExptID15== 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell2.Exp15
        Data['Stim'] = mat['Data'].Cell2.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell2.ExptID15 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell2.Exp15
        Data['Stim'] = mat['Data'].Cell2.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell2.ExptID15 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell2.Exp15
        Data['Stim'] = mat['Data'].Cell2.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell2.ExptID15 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell2.Exp15
        Data['Stim'] = mat['Data'].Cell2.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell2.ExptID15 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell2.Exp15
        Data['Stim'] = mat['Data'].Cell2.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
   
if User_choices['CellVal'] == 3:
    if User_choices['ExptVal'] == 1 and mat['Data'].Cell3.ExptID1 == 'IV':
        Data['Raw'] = mat['Data'].Cell3.Exp1
        Data['Stim'] = mat['Data'].Cell3.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell3.ExptID1 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell3.Exp1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell3.ExptID1 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell3.Exp1
        Data['Stim'] = mat['Data'].Cell3.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell3.ExptID1 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell3.Exp1
        Data['Stim'] = mat['Data'].Cell3.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell3.ExptID1 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell3.Exp1
        Data['Stim'] = mat['Data'].Cell3.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell.ExptID1 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell3.Exp1
        Data['Stim'] = mat['Data'].Cell3.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell3.ExptID1 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell3.Exp1
        Data['Stim'] = mat['Data'].Cell3.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell3.ExptID1 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell3.Exp1
        Data['Stim'] = mat['Data'].Cell3.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell3.ExptID1 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell3.Exp1
        Data['Stim'] = mat['Data'].Cell3.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 2 and mat['Data'].Cell3.ExptID2 == 'IV':
        Data['Raw'] = mat['Data'].Cell3.Exp2
        Data['Stim'] = mat['Data'].Cell3.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell3.ExptID2 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell3.Exp2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell3.ExptID2 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell3.Exp2
        Data['Stim'] = mat['Data'].Cell3.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell3.ExptID2 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell3.Exp2
        Data['Stim'] = mat['Data'].Cell3.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell3.ExptID2 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell3.Exp2
        Data['Stim'] = mat['Data'].Cell3.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell3.ExptID2 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell3.Exp2
        Data['Stim'] = mat['Data'].Cell3.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell3.ExptID2 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell3.Exp2
        Data['Stim'] = mat['Data'].Cell3.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell3.ExptID2 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell3.Exp2
        Data['Stim'] = mat['Data'].Cell3.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell3.ExptID2 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell3.Exp2
        Data['Stim'] = mat['Data'].Cell3.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 3 and mat['Data'].Cell3.ExptID3 == 'IV':
        Data['Raw'] = mat['Data'].Cell3.Exp3
        Data['Stim'] = mat['Data'].Cell3.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell3.ExptID3 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell3.Exp3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell3.ExptID3 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell3.Exp3
        Data['Stim'] = mat['Data'].Cell3.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell3.ExptID3 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell3.Exp3
        Data['Stim'] = mat['Data'].Cell3.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell3.ExptID3 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell3.Exp3
        Data['Stim'] = mat['Data'].Cell3.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell3.ExptID3 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell3.Exp3
        Data['Stim'] = mat['Data'].Cell3.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell3.ExptID3 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell3.Exp3
        Data['Stim'] = mat['Data'].Cell3.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell3.ExptID3 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell3.Exp3
        Data['Stim'] = mat['Data'].Cell3.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell3.ExptID3 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell3.Exp3
        Data['Stim'] = mat['Data'].Cell3.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
    
    if User_choices['ExptVal'] == 4 and mat['Data'].Cell3.ExptID4 == 'IV':
        Data['Raw'] = mat['Data'].Cell3.Exp4
        Data['Stim'] = mat['Data'].Cell3.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell3.ExptID4 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell3.Exp4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell3.ExptID4 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell3.Exp4
        Data['Stim'] = mat['Data'].Cell3.Stim4
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell3.ExptID4 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell3.Exp4
        Data['Stim'] = mat['Data'].Cell3.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell3.ExptID4 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell3.Exp4
        Data['Stim'] = mat['Data'].Cell3.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell3.ExptID4 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell3.Exp4
        Data['Stim'] = mat['Data'].Cell3.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell3.ExptID4 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell3.Exp4
        Data['Stim'] = mat['Data'].Cell3.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell3.ExptID4 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell3.Exp4
        Data['Stim'] = mat['Data'].Cell3.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell3.ExptID4 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell3.Exp4
        Data['Stim'] = mat['Data'].Cell3.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 5 and mat['Data'].Cell3.ExptID5 == 'IV':
        Data['Raw'] = mat['Data'].Cell3.Exp5
        Data['Stim'] = mat['Data'].Cell3.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell3.ExptID5 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell3.Exp5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell3.ExptID5 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell3.Exp5
        Data['Stim'] = mat['Data'].Cell3.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell3.ExptID5 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell3.Exp5
        Data['Stim'] = mat['Data'].Cell3.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell3.ExptID5 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell3.Exp5
        Data['Stim'] = mat['Data'].Cell3.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell3.ExptID5 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell3.Exp5
        Data['Stim'] = mat['Data'].Cell3.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell3.ExptID5 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell3.Exp5
        Data['Stim'] = mat['Data'].Cell3.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell3.ExptID5 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell3.Exp5
        Data['Stim'] = mat['Data'].Cell3.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell3.ExptID5 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell3.Exp5
        Data['Stim'] = mat['Data'].Cell3.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]        
        
    if User_choices['ExptVal'] == 6 and mat['Data'].Cell3.ExptID6 == 'IV':
        Data['Raw'] = mat['Data'].Cell3.Exp6
        Data['Stim'] = mat['Data'].Cell3.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell3.ExptID6 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell3.Exp6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell3.ExptID6 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell3.Exp6
        Data['Stim'] = mat['Data'].Cell3.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell3.ExptID6 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell3.Exp6
        Data['Stim'] = mat['Data'].Cell3.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell3.ExptID6 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell3.Exp6
        Data['Stim'] = mat['Data'].Cell3.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell3.ExptID6 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell3.Exp6
        Data['Stim'] = mat['Data'].Cell3.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell3.ExptID6 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell3.Exp6
        Data['Stim'] = mat['Data'].Cell3.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell3.ExptID6 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell3.Exp6
        Data['Stim'] = mat['Data'].Cell3.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell3.ExptID6 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell3.Exp6
        Data['Stim'] = mat['Data'].Cell3.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]        
        
    if User_choices['ExptVal'] == 7 and mat['Data'].Cell3.ExptID7 == 'IV':
        Data['Raw'] = mat['Data'].Cell3.Exp7
        Data['Stim'] = mat['Data'].Cell3.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell3.ExptID7 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell3.Exp7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell3.ExptID7 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell3.Exp7
        Data['Stim'] = mat['Data'].Cell3.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell3.ExptID7 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell3.Exp7
        Data['Stim'] = mat['Data'].Cell3.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell3.ExptID7 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell3.Exp7
        Data['Stim'] = mat['Data'].Cell3.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell3.ExptID7 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell3.Exp7
        Data['Stim'] = mat['Data'].Cell3.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell3.ExptID7 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell3.Exp7
        Data['Stim'] = mat['Data'].Cell3.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell3.ExptID7 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell3.Exp7
        Data['Stim'] = mat['Data'].Cell3.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell3.ExptID7 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell3.Exp7
        Data['Stim'] = mat['Data'].Cell3.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 8 and mat['Data'].Cell3.ExptID8 == 'IV':
        Data['Raw'] = mat['Data'].Cell3.Exp8
        Data['Stim'] = mat['Data'].Cell3.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell3.ExptID8 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell3.Exp8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell3.ExptID8 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell3.Exp8
        Data['Stim'] = mat['Data'].Cell3.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell3.ExptID8 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell3.Exp8
        Data['Stim'] = mat['Data'].Cell3.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell3.ExptID8 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell3.Exp8
        Data['Stim'] = mat['Data'].Cell3.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell3.ExptID8 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell3.Exp8
        Data['Stim'] = mat['Data'].Cell3.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell3.ExptID8 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell3.Exp8
        Data['Stim'] = mat['Data'].Cell3.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell3.ExptID8 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell3.Exp8
        Data['Stim'] = mat['Data'].Cell3.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell3.ExptID8 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell3.Exp8
        Data['Stim'] = mat['Data'].Cell3.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
    
    if User_choices['ExptVal'] == 9 and mat['Data'].Cell3.ExptID9 == 'IV':
        Data['Raw'] = mat['Data'].Cell3.Exp9
        Data['Stim'] = mat['Data'].Cell3.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell3.ExptID9 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell3.Exp9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell3.ExptID9 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell3.Exp9
        Data['Stim'] = mat['Data'].Cell3.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell3.ExptID9 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell3.Exp9
        Data['Stim'] = mat['Data'].Cell3.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell3.ExptID9 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell3.Exp9
        Data['Stim'] = mat['Data'].Cell3.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell3.ExptID9 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell3.Exp9
        Data['Stim'] = mat['Data'].Cell3.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell3.ExptID9 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell3.Exp9
        Data['Stim'] = mat['Data'].Cell3.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell3.ExptID9 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell3.Exp9
        Data['Stim'] = mat['Data'].Cell3.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell3.ExptID9 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell3.Exp9
        Data['Stim'] = mat['Data'].Cell3.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 10 and mat['Data'].Cell3.ExptID10 == 'IV':
        Data['Raw'] = mat['Data'].Cell3.Exp10
        Data['Stim'] = mat['Data'].Cell3.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell3.ExptID10 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell3.Exp10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell3.ExptID10 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell3.Exp10
        Data['Stim'] = mat['Data'].Cell3.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell3.ExptID10 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell3.Exp10
        Data['Stim'] = mat['Data'].Cell3.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell3.ExptID10 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell3.Exp10
        Data['Stim'] = mat['Data'].Cell3.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell3.ExptID10 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell3.Exp10
        Data['Stim'] = mat['Data'].Cell3.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell3.ExptID10 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell3.Exp10
        Data['Stim'] = mat['Data'].Cell3.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell3.ExptID10 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell3.Exp10
        Data['Stim'] = mat['Data'].Cell3.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell3.ExptID10 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell3.Exp10
        Data['Stim'] = mat['Data'].Cell3.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 11 and mat['Data'].Cell3.ExptID11 == 'IV':
        Data['Raw'] = mat['Data'].Cell3.Exp11
        Data['Stim'] = mat['Data'].Cell3.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell3.ExptID11 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell3.Exp11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell3.ExptID11 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell3.Exp11
        Data['Stim'] = mat['Data'].Cell3.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell3.ExptID11 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell3.Exp11
        Data['Stim'] = mat['Data'].Cell3.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell3.ExptID11 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell3.Exp11
        Data['Stim'] = mat['Data'].Cell3.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell3.ExptID11 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell3.Exp11
        Data['Stim'] = mat['Data'].Cell3.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell3.ExptID11 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell3.Exp11
        Data['Stim'] = mat['Data'].Cell3.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell3.ExptID11 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell3.Exp11
        Data['Stim'] = mat['Data'].Cell3.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell3.ExptID11 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell3.Exp11
        Data['Stim'] = mat['Data'].Cell3.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 12 and mat['Data'].Cell3.ExptID12 == 'IV':
        Data['Raw'] = mat['Data'].Cell3.Exp12
        Data['Stim'] = mat['Data'].Cell3.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell3.ExptID12 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell3.Exp12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell3.ExptID12 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell3.Exp12
        Data['Stim'] = mat['Data'].Cell3.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell3.ExptID12 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell3.Exp12
        Data['Stim'] = mat['Data'].Cell3.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell3.ExptID12 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell3.Exp12
        Data['Stim'] = mat['Data'].Cell3.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell3.ExptID12 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell3.Exp12
        Data['Stim'] = mat['Data'].Cell3.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell3.ExptID12 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell3.Exp12
        Data['Stim'] = mat['Data'].Cell3.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell3.ExptID12 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell3.Exp12
        Data['Stim'] = mat['Data'].Cell3.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell3.ExptID12 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell3.Exp12
        Data['Stim'] = mat['Data'].Cell3.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 13 and mat['Data'].Cell3.ExptID13 == 'IV':
        Data['Raw'] = mat['Data'].Cell3.Exp13
        Data['Stim'] = mat['Data'].Cell3.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell3.ExptID13 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell3.Exp13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell3.ExptID13 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell3.Exp13
        Data['Stim'] = mat['Data'].Cell3.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell3.ExptID13 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell3.Exp13
        Data['Stim'] = mat['Data'].Cell3.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell3.ExptID13 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell3.Exp13
        Data['Stim'] = mat['Data'].Cell3.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell3.ExptID13 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell3.Exp13
        Data['Stim'] = mat['Data'].Cell3.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell3.ExptID13 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell3.Exp13
        Data['Stim'] = mat['Data'].Cell3.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell3.ExptID13 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell3.Exp13
        Data['Stim'] = mat['Data'].Cell3.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell3.ExptID13 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell3.Exp13
        Data['Stim'] = mat['Data'].Cell3.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 14 and mat['Data'].Cell3.ExptID14 == 'IV':
        Data['Raw'] = mat['Data'].Cell3.Exp14
        Data['Stim'] = mat['Data'].Cell3.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell3.ExptID14 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell3.Exp14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell3.ExptI4 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell3.Exp14
        Data['Stim'] = mat['Data'].Cell3.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell3.ExptID14 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell3.Exp14
        Data['Stim'] = mat['Data'].Cell3.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell3.ExptID14 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell3.Exp14
        Data['Stim'] = mat['Data'].Cell3.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell3.ExptID14 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell3.Exp14
        Data['Stim'] = mat['Data'].Cell3.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell3.ExptID14 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell3.Exp14
        Data['Stim'] = mat['Data'].Cell3.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell3.ExptID14 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell3.Exp14
        Data['Stim'] = mat['Data'].Cell3.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell3.ExptID14 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell3.Exp14
        Data['Stim'] = mat['Data'].Cell3.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 15 and mat['Data'].Cell3.ExptID15== 'IV':
        Data['Raw'] = mat['Data'].Cell3.Exp15
        Data['Stim'] = mat['Data'].Cell3.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell3.ExptID15 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell3.Exp15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell3.ExptID15 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell3.Exp15
        Data['Stim'] = mat['Data'].Cell3.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell3.ExptID15 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell3.Exp15
        Data['Stim'] = mat['Data'].Cell3.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell3.ExptID15== 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell3.Exp15
        Data['Stim'] = mat['Data'].Cell3.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell3.ExptID15 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell3.Exp15
        Data['Stim'] = mat['Data'].Cell3.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell3.ExptID15 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell3.Exp15
        Data['Stim'] = mat['Data'].Cell3.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell3.ExptID15 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell3.Exp15
        Data['Stim'] = mat['Data'].Cell3.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell3.ExptID15 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell3.Exp15
        Data['Stim'] = mat['Data'].Cell3.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        

if User_choices['CellVal'] == 4:
    if User_choices['ExptVal'] == 1 and mat['Data'].Cell4.ExptID1 == 'IV':
        Data['Raw'] = mat['Data'].Cell4.Exp1
        Data['Stim'] = mat['Data'].Cell4.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell4.ExptID1 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell4.Exp1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell4.ExptID1 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell4.Exp1
        Data['Stim'] = mat['Data'].Cell4.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell4.ExptID1 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell4.Exp1
        Data['Stim'] = mat['Data'].Cell4.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell4.ExptID1 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell4.Exp1
        Data['Stim'] = mat['Data'].Cell4.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell.ExptID1 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell4.Exp1
        Data['Stim'] = mat['Data'].Cell4.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell4.ExptID1 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell4.Exp1
        Data['Stim'] = mat['Data'].Cell4.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell4.ExptID1 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell4.Exp1
        Data['Stim'] = mat['Data'].Cell4.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell4.ExptID1 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell4.Exp1
        Data['Stim'] = mat['Data'].Cell4.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 2 and mat['Data'].Cell4.ExptID2 == 'IV':
        Data['Raw'] = mat['Data'].Cell4.Exp2
        Data['Stim'] = mat['Data'].Cell4.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell4.ExptID2 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell4.Exp2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell4.ExptID2 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell4.Exp2
        Data['Stim'] = mat['Data'].Cell4.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell4.ExptID2 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell4.Exp2
        Data['Stim'] = mat['Data'].Cell4.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell4.ExptID2 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell4.Exp2
        Data['Stim'] = mat['Data'].Cell4.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell4.ExptID2 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell4.Exp2
        Data['Stim'] = mat['Data'].Cell4.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell4.ExptID2 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell4.Exp2
        Data['Stim'] = mat['Data'].Cell4.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell4.ExptID2 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell4.Exp2
        Data['Stim'] = mat['Data'].Cell4.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell4.ExptID2 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell4.Exp2
        Data['Stim'] = mat['Data'].Cell4.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 3 and mat['Data'].Cell4.ExptID3 == 'IV':
        Data['Raw'] = mat['Data'].Cell4.Exp3
        Data['Stim'] = mat['Data'].Cell4.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell4.ExptID3 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell4.Exp3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell4.ExptID3 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell4.Exp3
        Data['Stim'] = mat['Data'].Cell4.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell4.ExptID3 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell4.Exp3
        Data['Stim'] = mat['Data'].Cell4.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell4.ExptID3 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell4.Exp3
        Data['Stim'] = mat['Data'].Cell4.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell4.ExptID3 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell4.Exp3
        Data['Stim'] = mat['Data'].Cell4.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell4.ExptID3 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell4.Exp3
        Data['Stim'] = mat['Data'].Cell4.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell4.ExptID3 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell4.Exp3
        Data['Stim'] = mat['Data'].Cell4.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell4.ExptID3 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell4.Exp3
        Data['Stim'] = mat['Data'].Cell4.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
    
    if User_choices['ExptVal'] == 4 and mat['Data'].Cell4.ExptID4 == 'IV':
        Data['Raw'] = mat['Data'].Cell4.Exp4
        Data['Stim'] = mat['Data'].Cell4.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell4.ExptID4 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell4.Exp4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell4.ExptID4 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell4.Exp4
        Data['Stim'] = mat['Data'].Cell4.Stim4
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell4.ExptID4 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell4.Exp4
        Data['Stim'] = mat['Data'].Cell4.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell4.ExptID4 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell4.Exp4
        Data['Stim'] = mat['Data'].Cell4.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell4.ExptID4 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell4.Exp4
        Data['Stim'] = mat['Data'].Cell4.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell4.ExptID4 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell4.Exp4
        Data['Stim'] = mat['Data'].Cell4.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell4.ExptID4 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell4.Exp4
        Data['Stim'] = mat['Data'].Cell4.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell4.ExptID4 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell4.Exp4
        Data['Stim'] = mat['Data'].Cell4.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 5 and mat['Data'].Cell4.ExptID5 == 'IV':
        Data['Raw'] = mat['Data'].Cell4.Exp5
        Data['Stim'] = mat['Data'].Cell4.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell4.ExptID5 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell4.Exp5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell4.ExptID5 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell4.Exp5
        Data['Stim'] = mat['Data'].Cell4.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell4.ExptID5 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell4.Exp5
        Data['Stim'] = mat['Data'].Cell4.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell4.ExptID5 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell4.Exp5
        Data['Stim'] = mat['Data'].Cell4.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell4.ExptID5 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell4.Exp5
        Data['Stim'] = mat['Data'].Cell4.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell4.ExptID5 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell4.Exp5
        Data['Stim'] = mat['Data'].Cell4.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell4.ExptID5 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell4.Exp5
        Data['Stim'] = mat['Data'].Cell4.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell4.ExptID5 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell4.Exp5
        Data['Stim'] = mat['Data'].Cell4.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]        
        
    if User_choices['ExptVal'] == 6 and mat['Data'].Cell4.ExptID6 == 'IV':
        Data['Raw'] = mat['Data'].Cell4.Exp6
        Data['Stim'] = mat['Data'].Cell4.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell4.ExptID6 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell4.Exp6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell4.ExptID6 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell4.Exp6
        Data['Stim'] = mat['Data'].Cell4.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell4.ExptID6 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell4.Exp6
        Data['Stim'] = mat['Data'].Cell4.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell4.ExptID6 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell4.Exp6
        Data['Stim'] = mat['Data'].Cell4.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell4.ExptID6 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell4.Exp6
        Data['Stim'] = mat['Data'].Cell4.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell4.ExptID6 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell4.Exp6
        Data['Stim'] = mat['Data'].Cell4.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell4.ExptID6 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell4.Exp6
        Data['Stim'] = mat['Data'].Cell4.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell4.ExptID6 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell4.Exp6
        Data['Stim'] = mat['Data'].Cell4.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]        
        
    if User_choices['ExptVal'] == 7 and mat['Data'].Cell4.ExptID7 == 'IV':
        Data['Raw'] = mat['Data'].Cell4.Exp7
        Data['Stim'] = mat['Data'].Cell4.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell4.ExptID7 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell4.Exp7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell4.ExptID7 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell4.Exp7
        Data['Stim'] = mat['Data'].Cell4.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell4.ExptID7 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell4.Exp7
        Data['Stim'] = mat['Data'].Cell4.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell4.ExptID7 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell4.Exp7
        Data['Stim'] = mat['Data'].Cell4.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell4.ExptID7 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell4.Exp7
        Data['Stim'] = mat['Data'].Cell4.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell4.ExptID7 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell4.Exp7
        Data['Stim'] = mat['Data'].Cell4.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell4.ExptID7 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell4.Exp7
        Data['Stim'] = mat['Data'].Cell4.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell4.ExptID7 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell4.Exp7
        Data['Stim'] = mat['Data'].Cell4.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 8 and mat['Data'].Cell4.ExptID8 == 'IV':
        Data['Raw'] = mat['Data'].Cell4.Exp8
        Data['Stim'] = mat['Data'].Cell4.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell4.ExptID8 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell4.Exp8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell4.ExptID8 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell4.Exp8
        Data['Stim'] = mat['Data'].Cell4.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell4.ExptID8 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell4.Exp8
        Data['Stim'] = mat['Data'].Cell4.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell4.ExptID8 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell4.Exp8
        Data['Stim'] = mat['Data'].Cell4.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell4.ExptID8 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell4.Exp8
        Data['Stim'] = mat['Data'].Cell4.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell4.ExptID8 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell4.Exp8
        Data['Stim'] = mat['Data'].Cell4.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell4.ExptID8 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell4.Exp8
        Data['Stim'] = mat['Data'].Cell4.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell4.ExptID8 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell4.Exp8
        Data['Stim'] = mat['Data'].Cell4.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
    
    if User_choices['ExptVal'] == 9 and mat['Data'].Cell4.ExptID9 == 'IV':
        Data['Raw'] = mat['Data'].Cell4.Exp9
        Data['Stim'] = mat['Data'].Cell4.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell4.ExptID9 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell4.Exp9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell4.ExptID9 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell4.Exp9
        Data['Stim'] = mat['Data'].Cell4.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell4.ExptID9 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell4.Exp9
        Data['Stim'] = mat['Data'].Cell4.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell4.ExptID9 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell4.Exp9
        Data['Stim'] = mat['Data'].Cell4.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell4.ExptID9 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell4.Exp9
        Data['Stim'] = mat['Data'].Cell4.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell4.ExptID9 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell4.Exp9
        Data['Stim'] = mat['Data'].Cell4.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell4.ExptID9 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell4.Exp9
        Data['Stim'] = mat['Data'].Cell4.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell4.ExptID9 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell4.Exp9
        Data['Stim'] = mat['Data'].Cell4.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 10 and mat['Data'].Cell4.ExptID10 == 'IV':
        Data['Raw'] = mat['Data'].Cell4.Exp10
        Data['Stim'] = mat['Data'].Cell4.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell4.ExptID10 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell4.Exp10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell4.ExptID10 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell4.Exp10
        Data['Stim'] = mat['Data'].Cell4.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell4.ExptID10 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell4.Exp10
        Data['Stim'] = mat['Data'].Cell4.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell4.ExptID10 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell4.Exp10
        Data['Stim'] = mat['Data'].Cell4.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell4.ExptID10 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell4.Exp10
        Data['Stim'] = mat['Data'].Cell4.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell4.ExptID10 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell4.Exp10
        Data['Stim'] = mat['Data'].Cell4.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell4.ExptID10 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell4.Exp10
        Data['Stim'] = mat['Data'].Cell4.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell4.ExptID10 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell4.Exp10
        Data['Stim'] = mat['Data'].Cell4.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 11 and mat['Data'].Cell4.ExptID11 == 'IV':
        Data['Raw'] = mat['Data'].Cell4.Exp11
        Data['Stim'] = mat['Data'].Cell4.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell4.ExptID11 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell4.Exp11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell4.ExptID11 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell4.Exp11
        Data['Stim'] = mat['Data'].Cell4.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell4.ExptID11 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell4.Exp11
        Data['Stim'] = mat['Data'].Cell4.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell4.ExptID11 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell4.Exp11
        Data['Stim'] = mat['Data'].Cell4.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell4.ExptID11 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell4.Exp11
        Data['Stim'] = mat['Data'].Cell4.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell4.ExptID11 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell4.Exp11
        Data['Stim'] = mat['Data'].Cell4.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell4.ExptID11 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell4.Exp11
        Data['Stim'] = mat['Data'].Cell4.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell4.ExptID11 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell4.Exp11
        Data['Stim'] = mat['Data'].Cell4.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 12 and mat['Data'].Cell4.ExptID12 == 'IV':
        Data['Raw'] = mat['Data'].Cell4.Exp12
        Data['Stim'] = mat['Data'].Cell4.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell4.ExptID12 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell4.Exp12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell4.ExptID12 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell4.Exp12
        Data['Stim'] = mat['Data'].Cell4.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell4.ExptID12 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell4.Exp12
        Data['Stim'] = mat['Data'].Cell4.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell4.ExptID12 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell4.Exp12
        Data['Stim'] = mat['Data'].Cell4.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell4.ExptID12 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell4.Exp12
        Data['Stim'] = mat['Data'].Cell4.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell4.ExptID12 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell4.Exp12
        Data['Stim'] = mat['Data'].Cell4.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell4.ExptID12 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell4.Exp12
        Data['Stim'] = mat['Data'].Cell4.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell4.ExptID12 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell4.Exp12
        Data['Stim'] = mat['Data'].Cell4.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 13 and mat['Data'].Cell4.ExptID13 == 'IV':
        Data['Raw'] = mat['Data'].Cell4.Exp13
        Data['Stim'] = mat['Data'].Cell4.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell4.ExptID13 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell4.Exp13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell4.ExptID13 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell4.Exp13
        Data['Stim'] = mat['Data'].Cell4.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell4.ExptID13 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell4.Exp13
        Data['Stim'] = mat['Data'].Cell4.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell4.ExptID13 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell4.Exp13
        Data['Stim'] = mat['Data'].Cell4.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell4.ExptID13 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell4.Exp13
        Data['Stim'] = mat['Data'].Cell4.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell4.ExptID13 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell4.Exp13
        Data['Stim'] = mat['Data'].Cell4.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell4.ExptID13 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell4.Exp13
        Data['Stim'] = mat['Data'].Cell4.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell4.ExptID13 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell4.Exp13
        Data['Stim'] = mat['Data'].Cell4.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 14 and mat['Data'].Cell4.ExptID14 == 'IV':
        Data['Raw'] = mat['Data'].Cell4.Exp14
        Data['Stim'] = mat['Data'].Cell4.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell4.ExptID14 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell4.Exp14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell4.ExptI4 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell4.Exp14
        Data['Stim'] = mat['Data'].Cell4.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell4.ExptID14 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell4.Exp14
        Data['Stim'] = mat['Data'].Cell4.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell4.ExptID14 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell4.Exp14
        Data['Stim'] = mat['Data'].Cell4.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell4.ExptID14 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell4.Exp14
        Data['Stim'] = mat['Data'].Cell4.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell4.ExptID14 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell4.Exp14
        Data['Stim'] = mat['Data'].Cell4.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell4.ExptID14 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell4.Exp14
        Data['Stim'] = mat['Data'].Cell4.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell4.ExptID14 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell4.Exp14
        Data['Stim'] = mat['Data'].Cell4.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 15 and mat['Data'].Cell4.ExptID15== 'IV':
        Data['Raw'] = mat['Data'].Cell4.Exp15
        Data['Stim'] = mat['Data'].Cell4.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell4.ExptID15 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell4.Exp15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell4.ExptID15 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell4.Exp15
        Data['Stim'] = mat['Data'].Cell4.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell4.ExptID15 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell4.Exp15
        Data['Stim'] = mat['Data'].Cell4.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell4.ExptID15== 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell4.Exp15
        Data['Stim'] = mat['Data'].Cell4.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell4.ExptID15 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell4.Exp15
        Data['Stim'] = mat['Data'].Cell4.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell4.ExptID15 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell4.Exp15
        Data['Stim'] = mat['Data'].Cell4.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell4.ExptID15 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell4.Exp15
        Data['Stim'] = mat['Data'].Cell4.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell4.ExptID15 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell4.Exp15
        Data['Stim'] = mat['Data'].Cell4.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
             
if User_choices['CellVal'] == 5:
    if User_choices['ExptVal'] == 1 and mat['Data'].Cell5.ExptID1 == 'IV':
        Data['Raw'] = mat['Data'].Cell5.Exp1
        Data['Stim'] = mat['Data'].Cell5.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell5.ExptID1 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell5.Exp1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell5.ExptID1 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell5.Exp1
        Data['Stim'] = mat['Data'].Cell5.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell5.ExptID1 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell5.Exp1
        Data['Stim'] = mat['Data'].Cell5.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell5.ExptID1 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell5.Exp1
        Data['Stim'] = mat['Data'].Cell5.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell.ExptID1 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell5.Exp1
        Data['Stim'] = mat['Data'].Cell5.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell5.ExptID1 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell5.Exp1
        Data['Stim'] = mat['Data'].Cell5.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell5.ExptID1 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell5.Exp1
        Data['Stim'] = mat['Data'].Cell5.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell5.ExptID1 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell5.Exp1
        Data['Stim'] = mat['Data'].Cell5.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 2 and mat['Data'].Cell5.ExptID2 == 'IV':
        Data['Raw'] = mat['Data'].Cell5.Exp2
        Data['Stim'] = mat['Data'].Cell5.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell5.ExptID2 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell5.Exp2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell5.ExptID2 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell5.Exp2
        Data['Stim'] = mat['Data'].Cell5.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell5.ExptID2 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell5.Exp2
        Data['Stim'] = mat['Data'].Cell5.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell5.ExptID2 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell5.Exp2
        Data['Stim'] = mat['Data'].Cell5.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell5.ExptID2 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell5.Exp2
        Data['Stim'] = mat['Data'].Cell5.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell5.ExptID2 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell5.Exp2
        Data['Stim'] = mat['Data'].Cell5.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell5.ExptID2 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell5.Exp2
        Data['Stim'] = mat['Data'].Cell5.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell5.ExptID2 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell5.Exp2
        Data['Stim'] = mat['Data'].Cell5.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 3 and mat['Data'].Cell5.ExptID3 == 'IV':
        Data['Raw'] = mat['Data'].Cell5.Exp3
        Data['Stim'] = mat['Data'].Cell5.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell5.ExptID3 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell5.Exp3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell5.ExptID3 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell5.Exp3
        Data['Stim'] = mat['Data'].Cell5.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell5.ExptID3 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell5.Exp3
        Data['Stim'] = mat['Data'].Cell5.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell5.ExptID3 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell5.Exp3
        Data['Stim'] = mat['Data'].Cell5.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell5.ExptID3 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell5.Exp3
        Data['Stim'] = mat['Data'].Cell5.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell5.ExptID3 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell5.Exp3
        Data['Stim'] = mat['Data'].Cell5.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell5.ExptID3 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell5.Exp3
        Data['Stim'] = mat['Data'].Cell5.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell5.ExptID3 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell5.Exp3
        Data['Stim'] = mat['Data'].Cell5.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
    
    if User_choices['ExptVal'] == 4 and mat['Data'].Cell5.ExptID4 == 'IV':
        Data['Raw'] = mat['Data'].Cell5.Exp4
        Data['Stim'] = mat['Data'].Cell5.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell5.ExptID4 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell5.Exp4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell5.ExptID4 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell5.Exp4
        Data['Stim'] = mat['Data'].Cell5.Stim4
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell5.ExptID4 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell5.Exp4
        Data['Stim'] = mat['Data'].Cell5.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell5.ExptID4 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell5.Exp4
        Data['Stim'] = mat['Data'].Cell5.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell5.ExptID4 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell5.Exp4
        Data['Stim'] = mat['Data'].Cell5.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell5.ExptID4 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell5.Exp4
        Data['Stim'] = mat['Data'].Cell5.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell5.ExptID4 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell5.Exp4
        Data['Stim'] = mat['Data'].Cell5.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell5.ExptID4 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell5.Exp4
        Data['Stim'] = mat['Data'].Cell5.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 5 and mat['Data'].Cell5.ExptID5 == 'IV':
        Data['Raw'] = mat['Data'].Cell5.Exp5
        Data['Stim'] = mat['Data'].Cell5.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell5.ExptID5 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell5.Exp5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell5.ExptID5 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell5.Exp5
        Data['Stim'] = mat['Data'].Cell5.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell5.ExptID5 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell5.Exp5
        Data['Stim'] = mat['Data'].Cell5.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell5.ExptID5 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell5.Exp5
        Data['Stim'] = mat['Data'].Cell5.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell5.ExptID5 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell5.Exp5
        Data['Stim'] = mat['Data'].Cell5.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell5.ExptID5 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell5.Exp5
        Data['Stim'] = mat['Data'].Cell5.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell5.ExptID5 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell5.Exp5
        Data['Stim'] = mat['Data'].Cell5.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell5.ExptID5 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell5.Exp5
        Data['Stim'] = mat['Data'].Cell5.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]        
        
    if User_choices['ExptVal'] == 6 and mat['Data'].Cell5.ExptID6 == 'IV':
        Data['Raw'] = mat['Data'].Cell5.Exp6
        Data['Stim'] = mat['Data'].Cell5.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell5.ExptID6 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell5.Exp6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell5.ExptID6 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell5.Exp6
        Data['Stim'] = mat['Data'].Cell5.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell5.ExptID6 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell5.Exp6
        Data['Stim'] = mat['Data'].Cell5.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell5.ExptID6 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell5.Exp6
        Data['Stim'] = mat['Data'].Cell5.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell5.ExptID6 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell5.Exp6
        Data['Stim'] = mat['Data'].Cell5.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell5.ExptID6 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell5.Exp6
        Data['Stim'] = mat['Data'].Cell5.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell5.ExptID6 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell5.Exp6
        Data['Stim'] = mat['Data'].Cell5.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell5.ExptID6 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell5.Exp6
        Data['Stim'] = mat['Data'].Cell5.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]        
        
    if User_choices['ExptVal'] == 7 and mat['Data'].Cell5.ExptID7 == 'IV':
        Data['Raw'] = mat['Data'].Cell5.Exp7
        Data['Stim'] = mat['Data'].Cell5.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell5.ExptID7 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell5.Exp7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell5.ExptID7 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell5.Exp7
        Data['Stim'] = mat['Data'].Cell5.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell5.ExptID7 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell5.Exp7
        Data['Stim'] = mat['Data'].Cell5.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell5.ExptID7 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell5.Exp7
        Data['Stim'] = mat['Data'].Cell5.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell5.ExptID7 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell5.Exp7
        Data['Stim'] = mat['Data'].Cell5.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell5.ExptID7 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell5.Exp7
        Data['Stim'] = mat['Data'].Cell5.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell5.ExptID7 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell5.Exp7
        Data['Stim'] = mat['Data'].Cell5.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell5.ExptID7 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell5.Exp7
        Data['Stim'] = mat['Data'].Cell5.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 8 and mat['Data'].Cell5.ExptID8 == 'IV':
        Data['Raw'] = mat['Data'].Cell5.Exp8
        Data['Stim'] = mat['Data'].Cell5.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell5.ExptID8 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell5.Exp8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell5.ExptID8 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell5.Exp8
        Data['Stim'] = mat['Data'].Cell5.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell5.ExptID8 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell5.Exp8
        Data['Stim'] = mat['Data'].Cell5.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell5.ExptID8 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell5.Exp8
        Data['Stim'] = mat['Data'].Cell5.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell5.ExptID8 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell5.Exp8
        Data['Stim'] = mat['Data'].Cell5.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell5.ExptID8 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell5.Exp8
        Data['Stim'] = mat['Data'].Cell5.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell5.ExptID8 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell5.Exp8
        Data['Stim'] = mat['Data'].Cell5.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell5.ExptID8 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell5.Exp8
        Data['Stim'] = mat['Data'].Cell5.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
    
    if User_choices['ExptVal'] == 9 and mat['Data'].Cell5.ExptID9 == 'IV':
        Data['Raw'] = mat['Data'].Cell5.Exp9
        Data['Stim'] = mat['Data'].Cell5.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell5.ExptID9 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell5.Exp9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell5.ExptID9 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell5.Exp9
        Data['Stim'] = mat['Data'].Cell5.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell5.ExptID9 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell5.Exp9
        Data['Stim'] = mat['Data'].Cell5.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell5.ExptID9 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell5.Exp9
        Data['Stim'] = mat['Data'].Cell5.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell5.ExptID9 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell5.Exp9
        Data['Stim'] = mat['Data'].Cell5.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell5.ExptID9 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell5.Exp9
        Data['Stim'] = mat['Data'].Cell5.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell5.ExptID9 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell5.Exp9
        Data['Stim'] = mat['Data'].Cell5.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell5.ExptID9 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell5.Exp9
        Data['Stim'] = mat['Data'].Cell5.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 10 and mat['Data'].Cell5.ExptID10 == 'IV':
        Data['Raw'] = mat['Data'].Cell5.Exp10
        Data['Stim'] = mat['Data'].Cell5.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell5.ExptID10 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell5.Exp10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell5.ExptID10 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell5.Exp10
        Data['Stim'] = mat['Data'].Cell5.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell5.ExptID10 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell5.Exp10
        Data['Stim'] = mat['Data'].Cell5.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell5.ExptID10 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell5.Exp10
        Data['Stim'] = mat['Data'].Cell5.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell5.ExptID10 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell5.Exp10
        Data['Stim'] = mat['Data'].Cell5.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell5.ExptID10 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell5.Exp10
        Data['Stim'] = mat['Data'].Cell5.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell5.ExptID10 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell5.Exp10
        Data['Stim'] = mat['Data'].Cell5.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell5.ExptID10 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell5.Exp10
        Data['Stim'] = mat['Data'].Cell5.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 11 and mat['Data'].Cell5.ExptID11 == 'IV':
        Data['Raw'] = mat['Data'].Cell5.Exp11
        Data['Stim'] = mat['Data'].Cell5.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell5.ExptID11 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell5.Exp11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell5.ExptID11 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell5.Exp11
        Data['Stim'] = mat['Data'].Cell5.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell5.ExptID11 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell5.Exp11
        Data['Stim'] = mat['Data'].Cell5.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell5.ExptID11 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell5.Exp11
        Data['Stim'] = mat['Data'].Cell5.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell5.ExptID11 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell5.Exp11
        Data['Stim'] = mat['Data'].Cell5.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell5.ExptID11 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell5.Exp11
        Data['Stim'] = mat['Data'].Cell5.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell5.ExptID11 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell5.Exp11
        Data['Stim'] = mat['Data'].Cell5.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell5.ExptID11 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell5.Exp11
        Data['Stim'] = mat['Data'].Cell5.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 12 and mat['Data'].Cell5.ExptID12 == 'IV':
        Data['Raw'] = mat['Data'].Cell5.Exp12
        Data['Stim'] = mat['Data'].Cell5.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell5.ExptID12 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell5.Exp12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell5.ExptID12 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell5.Exp12
        Data['Stim'] = mat['Data'].Cell5.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell5.ExptID12 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell5.Exp12
        Data['Stim'] = mat['Data'].Cell5.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell5.ExptID12 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell5.Exp12
        Data['Stim'] = mat['Data'].Cell5.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell5.ExptID12 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell5.Exp12
        Data['Stim'] = mat['Data'].Cell5.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell5.ExptID12 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell5.Exp12
        Data['Stim'] = mat['Data'].Cell5.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell5.ExptID12 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell5.Exp12
        Data['Stim'] = mat['Data'].Cell5.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell5.ExptID12 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell5.Exp12
        Data['Stim'] = mat['Data'].Cell5.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 13 and mat['Data'].Cell5.ExptID13 == 'IV':
        Data['Raw'] = mat['Data'].Cell5.Exp13
        Data['Stim'] = mat['Data'].Cell5.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell5.ExptID13 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell5.Exp13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell5.ExptID13 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell5.Exp13
        Data['Stim'] = mat['Data'].Cell5.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell5.ExptID13 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell5.Exp13
        Data['Stim'] = mat['Data'].Cell5.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell5.ExptID13 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell5.Exp13
        Data['Stim'] = mat['Data'].Cell5.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell5.ExptID13 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell5.Exp13
        Data['Stim'] = mat['Data'].Cell5.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell5.ExptID13 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell5.Exp13
        Data['Stim'] = mat['Data'].Cell5.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell5.ExptID13 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell5.Exp13
        Data['Stim'] = mat['Data'].Cell5.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell5.ExptID13 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell5.Exp13
        Data['Stim'] = mat['Data'].Cell5.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 14 and mat['Data'].Cell5.ExptID14 == 'IV':
        Data['Raw'] = mat['Data'].Cell5.Exp14
        Data['Stim'] = mat['Data'].Cell5.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell5.ExptID14 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell5.Exp14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell5.ExptI4 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell5.Exp14
        Data['Stim'] = mat['Data'].Cell5.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell5.ExptID14 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell5.Exp14
        Data['Stim'] = mat['Data'].Cell5.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell5.ExptID14 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell5.Exp14
        Data['Stim'] = mat['Data'].Cell5.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell5.ExptID14 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell5.Exp14
        Data['Stim'] = mat['Data'].Cell5.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell5.ExptID14 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell5.Exp14
        Data['Stim'] = mat['Data'].Cell5.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell5.ExptID14 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell5.Exp14
        Data['Stim'] = mat['Data'].Cell5.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell5.ExptID14 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell5.Exp14
        Data['Stim'] = mat['Data'].Cell5.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 15 and mat['Data'].Cell5.ExptID15== 'IV':
        Data['Raw'] = mat['Data'].Cell5.Exp15
        Data['Stim'] = mat['Data'].Cell5.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell5.ExptID15 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell5.Exp15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell5.ExptID15 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell5.Exp15
        Data['Stim'] = mat['Data'].Cell5.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell5.ExptID15 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell5.Exp15
        Data['Stim'] = mat['Data'].Cell5.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell5.ExptID15== 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell5.Exp15
        Data['Stim'] = mat['Data'].Cell5.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell5.ExptID15 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell5.Exp15
        Data['Stim'] = mat['Data'].Cell5.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell5.ExptID15 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell5.Exp15
        Data['Stim'] = mat['Data'].Cell5.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell5.ExptID15 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell5.Exp15
        Data['Stim'] = mat['Data'].Cell5.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell5.ExptID15 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell5.Exp15
        Data['Stim'] = mat['Data'].Cell5.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

if User_choices['CellVal'] == 6:
    if User_choices['ExptVal'] == 1 and mat['Data'].Cell6.ExptID1 == 'IV':
        Data['Raw'] = mat['Data'].Cell6.Exp1
        Data['Stim'] = mat['Data'].Cell6.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell6.ExptID1 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell6.Exp1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell6.ExptID1 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell6.Exp1
        Data['Stim'] = mat['Data'].Cell6.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell6.ExptID1 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell6.Exp1
        Data['Stim'] = mat['Data'].Cell6.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell6.ExptID1 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell6.Exp1
        Data['Stim'] = mat['Data'].Cell6.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell.ExptID1 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell6.Exp1
        Data['Stim'] = mat['Data'].Cell6.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell6.ExptID1 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell6.Exp1
        Data['Stim'] = mat['Data'].Cell6.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell6.ExptID1 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell6.Exp1
        Data['Stim'] = mat['Data'].Cell6.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell6.ExptID1 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell6.Exp1
        Data['Stim'] = mat['Data'].Cell6.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 2 and mat['Data'].Cell6.ExptID2 == 'IV':
        Data['Raw'] = mat['Data'].Cell6.Exp2
        Data['Stim'] = mat['Data'].Cell6.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell6.ExptID2 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell6.Exp2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell6.ExptID2 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell6.Exp2
        Data['Stim'] = mat['Data'].Cell6.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell6.ExptID2 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell6.Exp2
        Data['Stim'] = mat['Data'].Cell6.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell6.ExptID2 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell6.Exp2
        Data['Stim'] = mat['Data'].Cell6.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell6.ExptID2 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell6.Exp2
        Data['Stim'] = mat['Data'].Cell6.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell6.ExptID2 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell6.Exp2
        Data['Stim'] = mat['Data'].Cell6.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell6.ExptID2 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell6.Exp2
        Data['Stim'] = mat['Data'].Cell6.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell6.ExptID2 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell6.Exp2
        Data['Stim'] = mat['Data'].Cell6.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 3 and mat['Data'].Cell6.ExptID3 == 'IV':
        Data['Raw'] = mat['Data'].Cell6.Exp3
        Data['Stim'] = mat['Data'].Cell6.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell6.ExptID3 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell6.Exp3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell6.ExptID3 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell6.Exp3
        Data['Stim'] = mat['Data'].Cell6.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell6.ExptID3 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell6.Exp3
        Data['Stim'] = mat['Data'].Cell6.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell6.ExptID3 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell6.Exp3
        Data['Stim'] = mat['Data'].Cell6.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell6.ExptID3 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell6.Exp3
        Data['Stim'] = mat['Data'].Cell6.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell6.ExptID3 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell6.Exp3
        Data['Stim'] = mat['Data'].Cell6.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell6.ExptID3 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell6.Exp3
        Data['Stim'] = mat['Data'].Cell6.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell6.ExptID3 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell6.Exp3
        Data['Stim'] = mat['Data'].Cell6.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
    
    if User_choices['ExptVal'] == 4 and mat['Data'].Cell6.ExptID4 == 'IV':
        Data['Raw'] = mat['Data'].Cell6.Exp4
        Data['Stim'] = mat['Data'].Cell6.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell6.ExptID4 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell6.Exp4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell6.ExptID4 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell6.Exp4
        Data['Stim'] = mat['Data'].Cell6.Stim4
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell6.ExptID4 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell6.Exp4
        Data['Stim'] = mat['Data'].Cell6.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell6.ExptID4 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell6.Exp4
        Data['Stim'] = mat['Data'].Cell6.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell6.ExptID4 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell6.Exp4
        Data['Stim'] = mat['Data'].Cell6.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell6.ExptID4 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell6.Exp4
        Data['Stim'] = mat['Data'].Cell6.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell6.ExptID4 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell6.Exp4
        Data['Stim'] = mat['Data'].Cell6.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell6.ExptID4 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell6.Exp4
        Data['Stim'] = mat['Data'].Cell6.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 5 and mat['Data'].Cell6.ExptID5 == 'IV':
        Data['Raw'] = mat['Data'].Cell6.Exp5
        Data['Stim'] = mat['Data'].Cell6.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell6.ExptID5 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell6.Exp5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell6.ExptID5 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell6.Exp5
        Data['Stim'] = mat['Data'].Cell6.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell6.ExptID5 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell6.Exp5
        Data['Stim'] = mat['Data'].Cell6.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell6.ExptID5 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell6.Exp5
        Data['Stim'] = mat['Data'].Cell6.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell6.ExptID5 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell6.Exp5
        Data['Stim'] = mat['Data'].Cell6.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell6.ExptID5 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell6.Exp5
        Data['Stim'] = mat['Data'].Cell6.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell6.ExptID5 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell6.Exp5
        Data['Stim'] = mat['Data'].Cell6.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell6.ExptID5 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell6.Exp5
        Data['Stim'] = mat['Data'].Cell6.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]        
        
    if User_choices['ExptVal'] == 6 and mat['Data'].Cell6.ExptID6 == 'IV':
        Data['Raw'] = mat['Data'].Cell6.Exp6
        Data['Stim'] = mat['Data'].Cell6.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell6.ExptID6 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell6.Exp6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell6.ExptID6 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell6.Exp6
        Data['Stim'] = mat['Data'].Cell6.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell6.ExptID6 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell6.Exp6
        Data['Stim'] = mat['Data'].Cell6.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell6.ExptID6 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell6.Exp6
        Data['Stim'] = mat['Data'].Cell6.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell6.ExptID6 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell6.Exp6
        Data['Stim'] = mat['Data'].Cell6.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell6.ExptID6 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell6.Exp6
        Data['Stim'] = mat['Data'].Cell6.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell6.ExptID6 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell6.Exp6
        Data['Stim'] = mat['Data'].Cell6.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell6.ExptID6 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell6.Exp6
        Data['Stim'] = mat['Data'].Cell6.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]        
        
    if User_choices['ExptVal'] == 7 and mat['Data'].Cell6.ExptID7 == 'IV':
        Data['Raw'] = mat['Data'].Cell6.Exp7
        Data['Stim'] = mat['Data'].Cell6.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell6.ExptID7 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell6.Exp7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell6.ExptID7 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell6.Exp7
        Data['Stim'] = mat['Data'].Cell6.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell6.ExptID7 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell6.Exp7
        Data['Stim'] = mat['Data'].Cell6.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell6.ExptID7 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell6.Exp7
        Data['Stim'] = mat['Data'].Cell6.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell6.ExptID7 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell6.Exp7
        Data['Stim'] = mat['Data'].Cell6.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell6.ExptID7 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell6.Exp7
        Data['Stim'] = mat['Data'].Cell6.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell6.ExptID7 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell6.Exp7
        Data['Stim'] = mat['Data'].Cell6.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell6.ExptID7 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell6.Exp7
        Data['Stim'] = mat['Data'].Cell6.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 8 and mat['Data'].Cell6.ExptID8 == 'IV':
        Data['Raw'] = mat['Data'].Cell6.Exp8
        Data['Stim'] = mat['Data'].Cell6.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell6.ExptID8 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell6.Exp8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell6.ExptID8 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell6.Exp8
        Data['Stim'] = mat['Data'].Cell6.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell6.ExptID8 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell6.Exp8
        Data['Stim'] = mat['Data'].Cell6.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell6.ExptID8 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell6.Exp8
        Data['Stim'] = mat['Data'].Cell6.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell6.ExptID8 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell6.Exp8
        Data['Stim'] = mat['Data'].Cell6.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell6.ExptID8 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell6.Exp8
        Data['Stim'] = mat['Data'].Cell6.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell6.ExptID8 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell6.Exp8
        Data['Stim'] = mat['Data'].Cell6.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell6.ExptID8 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell6.Exp8
        Data['Stim'] = mat['Data'].Cell6.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
    
    if User_choices['ExptVal'] == 9 and mat['Data'].Cell6.ExptID9 == 'IV':
        Data['Raw'] = mat['Data'].Cell6.Exp9
        Data['Stim'] = mat['Data'].Cell6.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell6.ExptID9 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell6.Exp9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell6.ExptID9 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell6.Exp9
        Data['Stim'] = mat['Data'].Cell6.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell6.ExptID9 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell6.Exp9
        Data['Stim'] = mat['Data'].Cell6.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell6.ExptID9 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell6.Exp9
        Data['Stim'] = mat['Data'].Cell6.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell6.ExptID9 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell6.Exp9
        Data['Stim'] = mat['Data'].Cell6.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell6.ExptID9 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell6.Exp9
        Data['Stim'] = mat['Data'].Cell6.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell6.ExptID9 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell6.Exp9
        Data['Stim'] = mat['Data'].Cell6.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell6.ExptID9 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell6.Exp9
        Data['Stim'] = mat['Data'].Cell6.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 10 and mat['Data'].Cell6.ExptID10 == 'IV':
        Data['Raw'] = mat['Data'].Cell6.Exp10
        Data['Stim'] = mat['Data'].Cell6.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell6.ExptID10 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell6.Exp10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell6.ExptID10 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell6.Exp10
        Data['Stim'] = mat['Data'].Cell6.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell6.ExptID10 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell6.Exp10
        Data['Stim'] = mat['Data'].Cell6.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell6.ExptID10 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell6.Exp10
        Data['Stim'] = mat['Data'].Cell6.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell6.ExptID10 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell6.Exp10
        Data['Stim'] = mat['Data'].Cell6.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell6.ExptID10 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell6.Exp10
        Data['Stim'] = mat['Data'].Cell6.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell6.ExptID10 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell6.Exp10
        Data['Stim'] = mat['Data'].Cell6.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell6.ExptID10 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell6.Exp10
        Data['Stim'] = mat['Data'].Cell6.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 11 and mat['Data'].Cell6.ExptID11 == 'IV':
        Data['Raw'] = mat['Data'].Cell6.Exp11
        Data['Stim'] = mat['Data'].Cell6.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell6.ExptID11 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell6.Exp11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell6.ExptID11 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell6.Exp11
        Data['Stim'] = mat['Data'].Cell6.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell6.ExptID11 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell6.Exp11
        Data['Stim'] = mat['Data'].Cell6.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell6.ExptID11 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell6.Exp11
        Data['Stim'] = mat['Data'].Cell6.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell6.ExptID11 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell6.Exp11
        Data['Stim'] = mat['Data'].Cell6.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell6.ExptID11 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell6.Exp11
        Data['Stim'] = mat['Data'].Cell6.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell6.ExptID11 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell6.Exp11
        Data['Stim'] = mat['Data'].Cell6.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell6.ExptID11 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell6.Exp11
        Data['Stim'] = mat['Data'].Cell6.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 12 and mat['Data'].Cell6.ExptID12 == 'IV':
        Data['Raw'] = mat['Data'].Cell6.Exp12
        Data['Stim'] = mat['Data'].Cell6.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell6.ExptID12 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell6.Exp12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell6.ExptID12 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell6.Exp12
        Data['Stim'] = mat['Data'].Cell6.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell6.ExptID12 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell6.Exp12
        Data['Stim'] = mat['Data'].Cell6.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell6.ExptID12 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell6.Exp12
        Data['Stim'] = mat['Data'].Cell6.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell6.ExptID12 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell6.Exp12
        Data['Stim'] = mat['Data'].Cell6.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell6.ExptID12 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell6.Exp12
        Data['Stim'] = mat['Data'].Cell6.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell6.ExptID12 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell6.Exp12
        Data['Stim'] = mat['Data'].Cell6.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell6.ExptID12 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell6.Exp12
        Data['Stim'] = mat['Data'].Cell6.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 13 and mat['Data'].Cell6.ExptID13 == 'IV':
        Data['Raw'] = mat['Data'].Cell6.Exp13
        Data['Stim'] = mat['Data'].Cell6.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell6.ExptID13 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell6.Exp13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell6.ExptID13 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell6.Exp13
        Data['Stim'] = mat['Data'].Cell6.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell6.ExptID13 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell6.Exp13
        Data['Stim'] = mat['Data'].Cell6.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell6.ExptID13 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell6.Exp13
        Data['Stim'] = mat['Data'].Cell6.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell6.ExptID13 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell6.Exp13
        Data['Stim'] = mat['Data'].Cell6.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell6.ExptID13 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell6.Exp13
        Data['Stim'] = mat['Data'].Cell6.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell6.ExptID13 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell6.Exp13
        Data['Stim'] = mat['Data'].Cell6.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell6.ExptID13 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell6.Exp13
        Data['Stim'] = mat['Data'].Cell6.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 14 and mat['Data'].Cell6.ExptID14 == 'IV':
        Data['Raw'] = mat['Data'].Cell6.Exp14
        Data['Stim'] = mat['Data'].Cell6.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell6.ExptID14 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell6.Exp14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell6.ExptI4 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell6.Exp14
        Data['Stim'] = mat['Data'].Cell6.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell6.ExptID14 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell6.Exp14
        Data['Stim'] = mat['Data'].Cell6.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell6.ExptID14 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell6.Exp14
        Data['Stim'] = mat['Data'].Cell6.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell6.ExptID14 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell6.Exp14
        Data['Stim'] = mat['Data'].Cell6.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell6.ExptID14 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell6.Exp14
        Data['Stim'] = mat['Data'].Cell6.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell6.ExptID14 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell6.Exp14
        Data['Stim'] = mat['Data'].Cell6.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell6.ExptID14 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell6.Exp14
        Data['Stim'] = mat['Data'].Cell6.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 15 and mat['Data'].Cell6.ExptID15== 'IV':
        Data['Raw'] = mat['Data'].Cell6.Exp15
        Data['Stim'] = mat['Data'].Cell6.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell6.ExptID15 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell6.Exp15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell6.ExptID15 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell6.Exp15
        Data['Stim'] = mat['Data'].Cell6.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell6.ExptID15 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell6.Exp15
        Data['Stim'] = mat['Data'].Cell6.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell6.ExptID15== 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell6.Exp15
        Data['Stim'] = mat['Data'].Cell6.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell6.ExptID15 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell6.Exp15
        Data['Stim'] = mat['Data'].Cell6.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell6.ExptID15 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell6.Exp15
        Data['Stim'] = mat['Data'].Cell6.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell6.ExptID15 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell6.Exp15
        Data['Stim'] = mat['Data'].Cell6.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell6.ExptID15 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell6.Exp15
        Data['Stim'] = mat['Data'].Cell6.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

if User_choices['CellVal'] == 7:
    if User_choices['ExptVal'] == 1 and mat['Data'].Cell7.ExptID1 == 'IV':
        Data['Raw'] = mat['Data'].Cell7.Exp1
        Data['Stim'] = mat['Data'].Cell7.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell7.ExptID1 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell7.Exp1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell7.ExptID1 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell7.Exp1
        Data['Stim'] = mat['Data'].Cell7.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell7.ExptID1 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell7.Exp1
        Data['Stim'] = mat['Data'].Cell7.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell7.ExptID1 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell7.Exp1
        Data['Stim'] = mat['Data'].Cell7.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell.ExptID1 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell7.Exp1
        Data['Stim'] = mat['Data'].Cell7.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell7.ExptID1 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell7.Exp1
        Data['Stim'] = mat['Data'].Cell7.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell7.ExptID1 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell7.Exp1
        Data['Stim'] = mat['Data'].Cell7.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell7.ExptID1 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell7.Exp1
        Data['Stim'] = mat['Data'].Cell7.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 2 and mat['Data'].Cell7.ExptID2 == 'IV':
        Data['Raw'] = mat['Data'].Cell7.Exp2
        Data['Stim'] = mat['Data'].Cell7.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell7.ExptID2 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell7.Exp2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell7.ExptID2 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell7.Exp2
        Data['Stim'] = mat['Data'].Cell7.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell7.ExptID2 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell7.Exp2
        Data['Stim'] = mat['Data'].Cell7.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell7.ExptID2 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell7.Exp2
        Data['Stim'] = mat['Data'].Cell7.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell7.ExptID2 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell7.Exp2
        Data['Stim'] = mat['Data'].Cell7.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell7.ExptID2 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell7.Exp2
        Data['Stim'] = mat['Data'].Cell7.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell7.ExptID2 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell7.Exp2
        Data['Stim'] = mat['Data'].Cell7.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell7.ExptID2 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell7.Exp2
        Data['Stim'] = mat['Data'].Cell7.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 3 and mat['Data'].Cell7.ExptID3 == 'IV':
        Data['Raw'] = mat['Data'].Cell7.Exp3
        Data['Stim'] = mat['Data'].Cell7.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell7.ExptID3 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell7.Exp3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell7.ExptID3 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell7.Exp3
        Data['Stim'] = mat['Data'].Cell7.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell7.ExptID3 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell7.Exp3
        Data['Stim'] = mat['Data'].Cell7.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell7.ExptID3 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell7.Exp3
        Data['Stim'] = mat['Data'].Cell7.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell7.ExptID3 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell7.Exp3
        Data['Stim'] = mat['Data'].Cell7.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell7.ExptID3 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell7.Exp3
        Data['Stim'] = mat['Data'].Cell7.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell7.ExptID3 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell7.Exp3
        Data['Stim'] = mat['Data'].Cell7.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell7.ExptID3 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell7.Exp3
        Data['Stim'] = mat['Data'].Cell7.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
    
    if User_choices['ExptVal'] == 4 and mat['Data'].Cell7.ExptID4 == 'IV':
        Data['Raw'] = mat['Data'].Cell7.Exp4
        Data['Stim'] = mat['Data'].Cell7.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell7.ExptID4 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell7.Exp4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell7.ExptID4 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell7.Exp4
        Data['Stim'] = mat['Data'].Cell7.Stim4
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell7.ExptID4 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell7.Exp4
        Data['Stim'] = mat['Data'].Cell7.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell7.ExptID4 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell7.Exp4
        Data['Stim'] = mat['Data'].Cell7.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell7.ExptID4 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell7.Exp4
        Data['Stim'] = mat['Data'].Cell7.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell7.ExptID4 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell7.Exp4
        Data['Stim'] = mat['Data'].Cell7.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell7.ExptID4 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell7.Exp4
        Data['Stim'] = mat['Data'].Cell7.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell7.ExptID4 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell7.Exp4
        Data['Stim'] = mat['Data'].Cell7.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 5 and mat['Data'].Cell7.ExptID5 == 'IV':
        Data['Raw'] = mat['Data'].Cell7.Exp5
        Data['Stim'] = mat['Data'].Cell7.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell7.ExptID5 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell7.Exp5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell7.ExptID5 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell7.Exp5
        Data['Stim'] = mat['Data'].Cell7.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell7.ExptID5 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell7.Exp5
        Data['Stim'] = mat['Data'].Cell7.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell7.ExptID5 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell7.Exp5
        Data['Stim'] = mat['Data'].Cell7.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell7.ExptID5 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell7.Exp5
        Data['Stim'] = mat['Data'].Cell7.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell7.ExptID5 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell7.Exp5
        Data['Stim'] = mat['Data'].Cell7.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell7.ExptID5 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell7.Exp5
        Data['Stim'] = mat['Data'].Cell7.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell7.ExptID5 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell7.Exp5
        Data['Stim'] = mat['Data'].Cell7.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]        
        
    if User_choices['ExptVal'] == 6 and mat['Data'].Cell7.ExptID6 == 'IV':
        Data['Raw'] = mat['Data'].Cell7.Exp6
        Data['Stim'] = mat['Data'].Cell7.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell7.ExptID6 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell7.Exp6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell7.ExptID6 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell7.Exp6
        Data['Stim'] = mat['Data'].Cell7.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell7.ExptID6 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell7.Exp6
        Data['Stim'] = mat['Data'].Cell7.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell7.ExptID6 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell7.Exp6
        Data['Stim'] = mat['Data'].Cell7.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell7.ExptID6 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell7.Exp6
        Data['Stim'] = mat['Data'].Cell7.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell7.ExptID6 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell7.Exp6
        Data['Stim'] = mat['Data'].Cell7.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell7.ExptID6 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell7.Exp6
        Data['Stim'] = mat['Data'].Cell7.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell7.ExptID6 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell7.Exp6
        Data['Stim'] = mat['Data'].Cell7.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]        
        
    if User_choices['ExptVal'] == 7 and mat['Data'].Cell7.ExptID7 == 'IV':
        Data['Raw'] = mat['Data'].Cell7.Exp7
        Data['Stim'] = mat['Data'].Cell7.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell7.ExptID7 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell7.Exp7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell7.ExptID7 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell7.Exp7
        Data['Stim'] = mat['Data'].Cell7.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell7.ExptID7 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell7.Exp7
        Data['Stim'] = mat['Data'].Cell7.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell7.ExptID7 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell7.Exp7
        Data['Stim'] = mat['Data'].Cell7.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell7.ExptID7 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell7.Exp7
        Data['Stim'] = mat['Data'].Cell7.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell7.ExptID7 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell7.Exp7
        Data['Stim'] = mat['Data'].Cell7.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell7.ExptID7 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell7.Exp7
        Data['Stim'] = mat['Data'].Cell7.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell7.ExptID7 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell7.Exp7
        Data['Stim'] = mat['Data'].Cell7.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 8 and mat['Data'].Cell7.ExptID8 == 'IV':
        Data['Raw'] = mat['Data'].Cell7.Exp8
        Data['Stim'] = mat['Data'].Cell7.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell7.ExptID8 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell7.Exp8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell7.ExptID8 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell7.Exp8
        Data['Stim'] = mat['Data'].Cell7.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell7.ExptID8 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell7.Exp8
        Data['Stim'] = mat['Data'].Cell7.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell7.ExptID8 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell7.Exp8
        Data['Stim'] = mat['Data'].Cell7.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell7.ExptID8 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell7.Exp8
        Data['Stim'] = mat['Data'].Cell7.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell7.ExptID8 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell7.Exp8
        Data['Stim'] = mat['Data'].Cell7.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell7.ExptID8 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell7.Exp8
        Data['Stim'] = mat['Data'].Cell7.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell7.ExptID8 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell7.Exp8
        Data['Stim'] = mat['Data'].Cell7.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
    
    if User_choices['ExptVal'] == 9 and mat['Data'].Cell7.ExptID9 == 'IV':
        Data['Raw'] = mat['Data'].Cell7.Exp9
        Data['Stim'] = mat['Data'].Cell7.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell7.ExptID9 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell7.Exp9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell7.ExptID9 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell7.Exp9
        Data['Stim'] = mat['Data'].Cell7.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell7.ExptID9 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell7.Exp9
        Data['Stim'] = mat['Data'].Cell7.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell7.ExptID9 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell7.Exp9
        Data['Stim'] = mat['Data'].Cell7.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell7.ExptID9 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell7.Exp9
        Data['Stim'] = mat['Data'].Cell7.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell7.ExptID9 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell7.Exp9
        Data['Stim'] = mat['Data'].Cell7.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell7.ExptID9 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell7.Exp9
        Data['Stim'] = mat['Data'].Cell7.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell7.ExptID9 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell7.Exp9
        Data['Stim'] = mat['Data'].Cell7.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 10 and mat['Data'].Cell7.ExptID10 == 'IV':
        Data['Raw'] = mat['Data'].Cell7.Exp10
        Data['Stim'] = mat['Data'].Cell7.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell7.ExptID10 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell7.Exp10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell7.ExptID10 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell7.Exp10
        Data['Stim'] = mat['Data'].Cell7.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell7.ExptID10 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell7.Exp10
        Data['Stim'] = mat['Data'].Cell7.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell7.ExptID10 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell7.Exp10
        Data['Stim'] = mat['Data'].Cell7.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell7.ExptID10 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell7.Exp10
        Data['Stim'] = mat['Data'].Cell7.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell7.ExptID10 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell7.Exp10
        Data['Stim'] = mat['Data'].Cell7.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell7.ExptID10 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell7.Exp10
        Data['Stim'] = mat['Data'].Cell7.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell7.ExptID10 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell7.Exp10
        Data['Stim'] = mat['Data'].Cell7.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 11 and mat['Data'].Cell7.ExptID11 == 'IV':
        Data['Raw'] = mat['Data'].Cell7.Exp11
        Data['Stim'] = mat['Data'].Cell7.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell7.ExptID11 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell7.Exp11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell7.ExptID11 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell7.Exp11
        Data['Stim'] = mat['Data'].Cell7.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell7.ExptID11 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell7.Exp11
        Data['Stim'] = mat['Data'].Cell7.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell7.ExptID11 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell7.Exp11
        Data['Stim'] = mat['Data'].Cell7.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell7.ExptID11 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell7.Exp11
        Data['Stim'] = mat['Data'].Cell7.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell7.ExptID11 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell7.Exp11
        Data['Stim'] = mat['Data'].Cell7.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell7.ExptID11 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell7.Exp11
        Data['Stim'] = mat['Data'].Cell7.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell7.ExptID11 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell7.Exp11
        Data['Stim'] = mat['Data'].Cell7.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 12 and mat['Data'].Cell7.ExptID12 == 'IV':
        Data['Raw'] = mat['Data'].Cell7.Exp12
        Data['Stim'] = mat['Data'].Cell7.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell7.ExptID12 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell7.Exp12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell7.ExptID12 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell7.Exp12
        Data['Stim'] = mat['Data'].Cell7.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell7.ExptID12 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell7.Exp12
        Data['Stim'] = mat['Data'].Cell7.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell7.ExptID12 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell7.Exp12
        Data['Stim'] = mat['Data'].Cell7.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell7.ExptID12 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell7.Exp12
        Data['Stim'] = mat['Data'].Cell7.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell7.ExptID12 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell7.Exp12
        Data['Stim'] = mat['Data'].Cell7.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell7.ExptID12 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell7.Exp12
        Data['Stim'] = mat['Data'].Cell7.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell7.ExptID12 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell7.Exp12
        Data['Stim'] = mat['Data'].Cell7.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 13 and mat['Data'].Cell7.ExptID13 == 'IV':
        Data['Raw'] = mat['Data'].Cell7.Exp13
        Data['Stim'] = mat['Data'].Cell7.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell7.ExptID13 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell7.Exp13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell7.ExptID13 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell7.Exp13
        Data['Stim'] = mat['Data'].Cell7.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell7.ExptID13 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell7.Exp13
        Data['Stim'] = mat['Data'].Cell7.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell7.ExptID13 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell7.Exp13
        Data['Stim'] = mat['Data'].Cell7.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell7.ExptID13 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell7.Exp13
        Data['Stim'] = mat['Data'].Cell7.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell7.ExptID13 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell7.Exp13
        Data['Stim'] = mat['Data'].Cell7.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell7.ExptID13 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell7.Exp13
        Data['Stim'] = mat['Data'].Cell7.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell7.ExptID13 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell7.Exp13
        Data['Stim'] = mat['Data'].Cell7.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 14 and mat['Data'].Cell7.ExptID14 == 'IV':
        Data['Raw'] = mat['Data'].Cell7.Exp14
        Data['Stim'] = mat['Data'].Cell7.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell7.ExptID14 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell7.Exp14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell7.ExptI4 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell7.Exp14
        Data['Stim'] = mat['Data'].Cell7.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell7.ExptID14 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell7.Exp14
        Data['Stim'] = mat['Data'].Cell7.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell7.ExptID14 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell7.Exp14
        Data['Stim'] = mat['Data'].Cell7.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell7.ExptID14 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell7.Exp14
        Data['Stim'] = mat['Data'].Cell7.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell7.ExptID14 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell7.Exp14
        Data['Stim'] = mat['Data'].Cell7.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell7.ExptID14 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell7.Exp14
        Data['Stim'] = mat['Data'].Cell7.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell7.ExptID14 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell7.Exp14
        Data['Stim'] = mat['Data'].Cell7.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 15 and mat['Data'].Cell7.ExptID15== 'IV':
        Data['Raw'] = mat['Data'].Cell7.Exp15
        Data['Stim'] = mat['Data'].Cell7.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell7.ExptID15 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell7.Exp15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell7.ExptID15 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell7.Exp15
        Data['Stim'] = mat['Data'].Cell7.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell7.ExptID15 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell7.Exp15
        Data['Stim'] = mat['Data'].Cell7.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell7.ExptID15== 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell7.Exp15
        Data['Stim'] = mat['Data'].Cell7.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell7.ExptID15 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell7.Exp15
        Data['Stim'] = mat['Data'].Cell7.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell7.ExptID15 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell7.Exp15
        Data['Stim'] = mat['Data'].Cell7.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell7.ExptID15 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell7.Exp15
        Data['Stim'] = mat['Data'].Cell7.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell7.ExptID15 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell7.Exp15
        Data['Stim'] = mat['Data'].Cell7.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

if User_choices['CellVal'] == 8:
    if User_choices['ExptVal'] == 1 and mat['Data'].Cell8.ExptID1 == 'IV':
        Data['Raw'] = mat['Data'].Cell8.Exp1
        Data['Stim'] = mat['Data'].Cell8.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell8.ExptID1 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell8.Exp1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell8.ExptID1 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell8.Exp1
        Data['Stim'] = mat['Data'].Cell8.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell8.ExptID1 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell8.Exp1
        Data['Stim'] = mat['Data'].Cell8.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell8.ExptID1 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell8.Exp1
        Data['Stim'] = mat['Data'].Cell8.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell.ExptID1 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell8.Exp1
        Data['Stim'] = mat['Data'].Cell8.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell8.ExptID1 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell8.Exp1
        Data['Stim'] = mat['Data'].Cell8.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell8.ExptID1 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell8.Exp1
        Data['Stim'] = mat['Data'].Cell8.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell8.ExptID1 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell8.Exp1
        Data['Stim'] = mat['Data'].Cell8.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 2 and mat['Data'].Cell8.ExptID2 == 'IV':
        Data['Raw'] = mat['Data'].Cell8.Exp2
        Data['Stim'] = mat['Data'].Cell8.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell8.ExptID2 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell8.Exp2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell8.ExptID2 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell8.Exp2
        Data['Stim'] = mat['Data'].Cell8.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell8.ExptID2 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell8.Exp2
        Data['Stim'] = mat['Data'].Cell8.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell8.ExptID2 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell8.Exp2
        Data['Stim'] = mat['Data'].Cell8.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell8.ExptID2 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell8.Exp2
        Data['Stim'] = mat['Data'].Cell8.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell8.ExptID2 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell8.Exp2
        Data['Stim'] = mat['Data'].Cell8.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell8.ExptID2 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell8.Exp2
        Data['Stim'] = mat['Data'].Cell8.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell8.ExptID2 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell8.Exp2
        Data['Stim'] = mat['Data'].Cell8.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 3 and mat['Data'].Cell8.ExptID3 == 'IV':
        Data['Raw'] = mat['Data'].Cell8.Exp3
        Data['Stim'] = mat['Data'].Cell8.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell8.ExptID3 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell8.Exp3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell8.ExptID3 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell8.Exp3
        Data['Stim'] = mat['Data'].Cell8.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell8.ExptID3 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell8.Exp3
        Data['Stim'] = mat['Data'].Cell8.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell8.ExptID3 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell8.Exp3
        Data['Stim'] = mat['Data'].Cell8.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell8.ExptID3 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell8.Exp3
        Data['Stim'] = mat['Data'].Cell8.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell8.ExptID3 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell8.Exp3
        Data['Stim'] = mat['Data'].Cell8.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell8.ExptID3 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell8.Exp3
        Data['Stim'] = mat['Data'].Cell8.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell8.ExptID3 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell8.Exp3
        Data['Stim'] = mat['Data'].Cell8.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
    
    if User_choices['ExptVal'] == 4 and mat['Data'].Cell8.ExptID4 == 'IV':
        Data['Raw'] = mat['Data'].Cell8.Exp4
        Data['Stim'] = mat['Data'].Cell8.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell8.ExptID4 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell8.Exp4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell8.ExptID4 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell8.Exp4
        Data['Stim'] = mat['Data'].Cell8.Stim4
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell8.ExptID4 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell8.Exp4
        Data['Stim'] = mat['Data'].Cell8.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell8.ExptID4 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell8.Exp4
        Data['Stim'] = mat['Data'].Cell8.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell8.ExptID4 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell8.Exp4
        Data['Stim'] = mat['Data'].Cell8.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell8.ExptID4 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell8.Exp4
        Data['Stim'] = mat['Data'].Cell8.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell8.ExptID4 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell8.Exp4
        Data['Stim'] = mat['Data'].Cell8.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell8.ExptID4 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell8.Exp4
        Data['Stim'] = mat['Data'].Cell8.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 5 and mat['Data'].Cell8.ExptID5 == 'IV':
        Data['Raw'] = mat['Data'].Cell8.Exp5
        Data['Stim'] = mat['Data'].Cell8.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell8.ExptID5 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell8.Exp5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell8.ExptID5 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell8.Exp5
        Data['Stim'] = mat['Data'].Cell8.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell8.ExptID5 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell8.Exp5
        Data['Stim'] = mat['Data'].Cell8.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell8.ExptID5 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell8.Exp5
        Data['Stim'] = mat['Data'].Cell8.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell8.ExptID5 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell8.Exp5
        Data['Stim'] = mat['Data'].Cell8.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell8.ExptID5 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell8.Exp5
        Data['Stim'] = mat['Data'].Cell8.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell8.ExptID5 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell8.Exp5
        Data['Stim'] = mat['Data'].Cell8.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell8.ExptID5 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell8.Exp5
        Data['Stim'] = mat['Data'].Cell8.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]        
        
    if User_choices['ExptVal'] == 6 and mat['Data'].Cell8.ExptID6 == 'IV':
        Data['Raw'] = mat['Data'].Cell8.Exp6
        Data['Stim'] = mat['Data'].Cell8.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell8.ExptID6 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell8.Exp6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell8.ExptID6 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell8.Exp6
        Data['Stim'] = mat['Data'].Cell8.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell8.ExptID6 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell8.Exp6
        Data['Stim'] = mat['Data'].Cell8.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell8.ExptID6 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell8.Exp6
        Data['Stim'] = mat['Data'].Cell8.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell8.ExptID6 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell8.Exp6
        Data['Stim'] = mat['Data'].Cell8.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell8.ExptID6 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell8.Exp6
        Data['Stim'] = mat['Data'].Cell8.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell8.ExptID6 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell8.Exp6
        Data['Stim'] = mat['Data'].Cell8.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell8.ExptID6 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell8.Exp6
        Data['Stim'] = mat['Data'].Cell8.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]        
        
    if User_choices['ExptVal'] == 7 and mat['Data'].Cell8.ExptID7 == 'IV':
        Data['Raw'] = mat['Data'].Cell8.Exp7
        Data['Stim'] = mat['Data'].Cell8.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell8.ExptID7 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell8.Exp7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell8.ExptID7 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell8.Exp7
        Data['Stim'] = mat['Data'].Cell8.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell8.ExptID7 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell8.Exp7
        Data['Stim'] = mat['Data'].Cell8.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell8.ExptID7 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell8.Exp7
        Data['Stim'] = mat['Data'].Cell8.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell8.ExptID7 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell8.Exp7
        Data['Stim'] = mat['Data'].Cell8.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell8.ExptID7 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell8.Exp7
        Data['Stim'] = mat['Data'].Cell8.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell8.ExptID7 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell8.Exp7
        Data['Stim'] = mat['Data'].Cell8.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell8.ExptID7 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell8.Exp7
        Data['Stim'] = mat['Data'].Cell8.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 8 and mat['Data'].Cell8.ExptID8 == 'IV':
        Data['Raw'] = mat['Data'].Cell8.Exp8
        Data['Stim'] = mat['Data'].Cell8.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell8.ExptID8 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell8.Exp8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell8.ExptID8 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell8.Exp8
        Data['Stim'] = mat['Data'].Cell8.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell8.ExptID8 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell8.Exp8
        Data['Stim'] = mat['Data'].Cell8.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell8.ExptID8 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell8.Exp8
        Data['Stim'] = mat['Data'].Cell8.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell8.ExptID8 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell8.Exp8
        Data['Stim'] = mat['Data'].Cell8.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell8.ExptID8 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell8.Exp8
        Data['Stim'] = mat['Data'].Cell8.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell8.ExptID8 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell8.Exp8
        Data['Stim'] = mat['Data'].Cell8.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell8.ExptID8 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell8.Exp8
        Data['Stim'] = mat['Data'].Cell8.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
    
    if User_choices['ExptVal'] == 9 and mat['Data'].Cell8.ExptID9 == 'IV':
        Data['Raw'] = mat['Data'].Cell8.Exp9
        Data['Stim'] = mat['Data'].Cell8.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell8.ExptID9 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell8.Exp9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell8.ExptID9 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell8.Exp9
        Data['Stim'] = mat['Data'].Cell8.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell8.ExptID9 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell8.Exp9
        Data['Stim'] = mat['Data'].Cell8.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell8.ExptID9 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell8.Exp9
        Data['Stim'] = mat['Data'].Cell8.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell8.ExptID9 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell8.Exp9
        Data['Stim'] = mat['Data'].Cell8.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell8.ExptID9 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell8.Exp9
        Data['Stim'] = mat['Data'].Cell8.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell8.ExptID9 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell8.Exp9
        Data['Stim'] = mat['Data'].Cell8.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell8.ExptID9 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell8.Exp9
        Data['Stim'] = mat['Data'].Cell8.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 10 and mat['Data'].Cell8.ExptID10 == 'IV':
        Data['Raw'] = mat['Data'].Cell8.Exp10
        Data['Stim'] = mat['Data'].Cell8.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell8.ExptID10 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell8.Exp10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell8.ExptID10 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell8.Exp10
        Data['Stim'] = mat['Data'].Cell8.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell8.ExptID10 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell8.Exp10
        Data['Stim'] = mat['Data'].Cell8.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell8.ExptID10 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell8.Exp10
        Data['Stim'] = mat['Data'].Cell8.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell8.ExptID10 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell8.Exp10
        Data['Stim'] = mat['Data'].Cell8.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell8.ExptID10 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell8.Exp10
        Data['Stim'] = mat['Data'].Cell8.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell8.ExptID10 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell8.Exp10
        Data['Stim'] = mat['Data'].Cell8.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell8.ExptID10 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell8.Exp10
        Data['Stim'] = mat['Data'].Cell8.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 11 and mat['Data'].Cell8.ExptID11 == 'IV':
        Data['Raw'] = mat['Data'].Cell8.Exp11
        Data['Stim'] = mat['Data'].Cell8.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell8.ExptID11 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell8.Exp11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell8.ExptID11 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell8.Exp11
        Data['Stim'] = mat['Data'].Cell8.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell8.ExptID11 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell8.Exp11
        Data['Stim'] = mat['Data'].Cell8.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell8.ExptID11 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell8.Exp11
        Data['Stim'] = mat['Data'].Cell8.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell8.ExptID11 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell8.Exp11
        Data['Stim'] = mat['Data'].Cell8.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell8.ExptID11 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell8.Exp11
        Data['Stim'] = mat['Data'].Cell8.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell8.ExptID11 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell8.Exp11
        Data['Stim'] = mat['Data'].Cell8.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell8.ExptID11 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell8.Exp11
        Data['Stim'] = mat['Data'].Cell8.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 12 and mat['Data'].Cell8.ExptID12 == 'IV':
        Data['Raw'] = mat['Data'].Cell8.Exp12
        Data['Stim'] = mat['Data'].Cell8.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell8.ExptID12 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell8.Exp12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell8.ExptID12 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell8.Exp12
        Data['Stim'] = mat['Data'].Cell8.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell8.ExptID12 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell8.Exp12
        Data['Stim'] = mat['Data'].Cell8.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell8.ExptID12 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell8.Exp12
        Data['Stim'] = mat['Data'].Cell8.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell8.ExptID12 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell8.Exp12
        Data['Stim'] = mat['Data'].Cell8.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell8.ExptID12 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell8.Exp12
        Data['Stim'] = mat['Data'].Cell8.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell8.ExptID12 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell8.Exp12
        Data['Stim'] = mat['Data'].Cell8.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell8.ExptID12 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell8.Exp12
        Data['Stim'] = mat['Data'].Cell8.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 13 and mat['Data'].Cell8.ExptID13 == 'IV':
        Data['Raw'] = mat['Data'].Cell8.Exp13
        Data['Stim'] = mat['Data'].Cell8.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell8.ExptID13 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell8.Exp13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell8.ExptID13 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell8.Exp13
        Data['Stim'] = mat['Data'].Cell8.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell8.ExptID13 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell8.Exp13
        Data['Stim'] = mat['Data'].Cell8.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell8.ExptID13 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell8.Exp13
        Data['Stim'] = mat['Data'].Cell8.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell8.ExptID13 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell8.Exp13
        Data['Stim'] = mat['Data'].Cell8.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell8.ExptID13 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell8.Exp13
        Data['Stim'] = mat['Data'].Cell8.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell8.ExptID13 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell8.Exp13
        Data['Stim'] = mat['Data'].Cell8.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell8.ExptID13 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell8.Exp13
        Data['Stim'] = mat['Data'].Cell8.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 14 and mat['Data'].Cell8.ExptID14 == 'IV':
        Data['Raw'] = mat['Data'].Cell8.Exp14
        Data['Stim'] = mat['Data'].Cell8.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell8.ExptID14 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell8.Exp14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell8.ExptI4 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell8.Exp14
        Data['Stim'] = mat['Data'].Cell8.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell8.ExptID14 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell8.Exp14
        Data['Stim'] = mat['Data'].Cell8.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell8.ExptID14 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell8.Exp14
        Data['Stim'] = mat['Data'].Cell8.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell8.ExptID14 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell8.Exp14
        Data['Stim'] = mat['Data'].Cell8.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell8.ExptID14 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell8.Exp14
        Data['Stim'] = mat['Data'].Cell8.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell8.ExptID14 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell8.Exp14
        Data['Stim'] = mat['Data'].Cell8.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell8.ExptID14 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell8.Exp14
        Data['Stim'] = mat['Data'].Cell8.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 15 and mat['Data'].Cell8.ExptID15== 'IV':
        Data['Raw'] = mat['Data'].Cell8.Exp15
        Data['Stim'] = mat['Data'].Cell8.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell8.ExptID15 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell8.Exp15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell8.ExptID15 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell8.Exp15
        Data['Stim'] = mat['Data'].Cell8.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell8.ExptID15 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell8.Exp15
        Data['Stim'] = mat['Data'].Cell8.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell8.ExptID15== 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell8.Exp15
        Data['Stim'] = mat['Data'].Cell8.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell8.ExptID15 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell8.Exp15
        Data['Stim'] = mat['Data'].Cell8.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell8.ExptID15 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell8.Exp15
        Data['Stim'] = mat['Data'].Cell8.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell8.ExptID15 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell8.Exp15
        Data['Stim'] = mat['Data'].Cell8.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell8.ExptID15 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell8.Exp15
        Data['Stim'] = mat['Data'].Cell8.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

if User_choices['CellVal'] == 9:
    if User_choices['ExptVal'] == 1 and mat['Data'].Cell9.ExptID1 == 'IV':
        Data['Raw'] = mat['Data'].Cell9.Exp1
        Data['Stim'] = mat['Data'].Cell9.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell9.ExptID1 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell9.Exp1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell9.ExptID1 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell9.Exp1
        Data['Stim'] = mat['Data'].Cell9.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell9.ExptID1 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell9.Exp1
        Data['Stim'] = mat['Data'].Cell9.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell9.ExptID1 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell9.Exp1
        Data['Stim'] = mat['Data'].Cell9.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell.ExptID1 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell9.Exp1
        Data['Stim'] = mat['Data'].Cell9.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell9.ExptID1 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell9.Exp1
        Data['Stim'] = mat['Data'].Cell9.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell9.ExptID1 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell9.Exp1
        Data['Stim'] = mat['Data'].Cell9.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell9.ExptID1 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell9.Exp1
        Data['Stim'] = mat['Data'].Cell9.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 2 and mat['Data'].Cell9.ExptID2 == 'IV':
        Data['Raw'] = mat['Data'].Cell9.Exp2
        Data['Stim'] = mat['Data'].Cell9.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell9.ExptID2 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell9.Exp2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell9.ExptID2 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell9.Exp2
        Data['Stim'] = mat['Data'].Cell9.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell9.ExptID2 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell9.Exp2
        Data['Stim'] = mat['Data'].Cell9.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell9.ExptID2 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell9.Exp2
        Data['Stim'] = mat['Data'].Cell9.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell9.ExptID2 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell9.Exp2
        Data['Stim'] = mat['Data'].Cell9.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell9.ExptID2 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell9.Exp2
        Data['Stim'] = mat['Data'].Cell9.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell9.ExptID2 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell9.Exp2
        Data['Stim'] = mat['Data'].Cell9.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell9.ExptID2 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell9.Exp2
        Data['Stim'] = mat['Data'].Cell9.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 3 and mat['Data'].Cell9.ExptID3 == 'IV':
        Data['Raw'] = mat['Data'].Cell9.Exp3
        Data['Stim'] = mat['Data'].Cell9.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell9.ExptID3 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell9.Exp3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell9.ExptID3 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell9.Exp3
        Data['Stim'] = mat['Data'].Cell9.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell9.ExptID3 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell9.Exp3
        Data['Stim'] = mat['Data'].Cell9.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell9.ExptID3 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell9.Exp3
        Data['Stim'] = mat['Data'].Cell9.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell9.ExptID3 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell9.Exp3
        Data['Stim'] = mat['Data'].Cell9.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell9.ExptID3 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell9.Exp3
        Data['Stim'] = mat['Data'].Cell9.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell9.ExptID3 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell9.Exp3
        Data['Stim'] = mat['Data'].Cell9.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell9.ExptID3 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell9.Exp3
        Data['Stim'] = mat['Data'].Cell9.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
    
    if User_choices['ExptVal'] == 4 and mat['Data'].Cell9.ExptID4 == 'IV':
        Data['Raw'] = mat['Data'].Cell9.Exp4
        Data['Stim'] = mat['Data'].Cell9.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell9.ExptID4 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell9.Exp4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell9.ExptID4 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell9.Exp4
        Data['Stim'] = mat['Data'].Cell9.Stim4
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell9.ExptID4 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell9.Exp4
        Data['Stim'] = mat['Data'].Cell9.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell9.ExptID4 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell9.Exp4
        Data['Stim'] = mat['Data'].Cell9.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell9.ExptID4 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell9.Exp4
        Data['Stim'] = mat['Data'].Cell9.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell9.ExptID4 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell9.Exp4
        Data['Stim'] = mat['Data'].Cell9.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell9.ExptID4 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell9.Exp4
        Data['Stim'] = mat['Data'].Cell9.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell9.ExptID4 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell9.Exp4
        Data['Stim'] = mat['Data'].Cell9.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 5 and mat['Data'].Cell9.ExptID5 == 'IV':
        Data['Raw'] = mat['Data'].Cell9.Exp5
        Data['Stim'] = mat['Data'].Cell9.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell9.ExptID5 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell9.Exp5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell9.ExptID5 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell9.Exp5
        Data['Stim'] = mat['Data'].Cell9.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell9.ExptID5 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell9.Exp5
        Data['Stim'] = mat['Data'].Cell9.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell9.ExptID5 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell9.Exp5
        Data['Stim'] = mat['Data'].Cell9.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell9.ExptID5 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell9.Exp5
        Data['Stim'] = mat['Data'].Cell9.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell9.ExptID5 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell9.Exp5
        Data['Stim'] = mat['Data'].Cell9.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell9.ExptID5 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell9.Exp5
        Data['Stim'] = mat['Data'].Cell9.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell9.ExptID5 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell9.Exp5
        Data['Stim'] = mat['Data'].Cell9.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]        
        
    if User_choices['ExptVal'] == 6 and mat['Data'].Cell9.ExptID6 == 'IV':
        Data['Raw'] = mat['Data'].Cell9.Exp6
        Data['Stim'] = mat['Data'].Cell9.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell9.ExptID6 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell9.Exp6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell9.ExptID6 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell9.Exp6
        Data['Stim'] = mat['Data'].Cell9.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell9.ExptID6 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell9.Exp6
        Data['Stim'] = mat['Data'].Cell9.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell9.ExptID6 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell9.Exp6
        Data['Stim'] = mat['Data'].Cell9.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell9.ExptID6 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell9.Exp6
        Data['Stim'] = mat['Data'].Cell9.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell9.ExptID6 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell9.Exp6
        Data['Stim'] = mat['Data'].Cell9.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell9.ExptID6 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell9.Exp6
        Data['Stim'] = mat['Data'].Cell9.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell9.ExptID6 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell9.Exp6
        Data['Stim'] = mat['Data'].Cell9.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]        
        
    if User_choices['ExptVal'] == 7 and mat['Data'].Cell9.ExptID7 == 'IV':
        Data['Raw'] = mat['Data'].Cell9.Exp7
        Data['Stim'] = mat['Data'].Cell9.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell9.ExptID7 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell9.Exp7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell9.ExptID7 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell9.Exp7
        Data['Stim'] = mat['Data'].Cell9.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell9.ExptID7 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell9.Exp7
        Data['Stim'] = mat['Data'].Cell9.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell9.ExptID7 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell9.Exp7
        Data['Stim'] = mat['Data'].Cell9.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell9.ExptID7 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell9.Exp7
        Data['Stim'] = mat['Data'].Cell9.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell9.ExptID7 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell9.Exp7
        Data['Stim'] = mat['Data'].Cell9.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell9.ExptID7 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell9.Exp7
        Data['Stim'] = mat['Data'].Cell9.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell9.ExptID7 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell9.Exp7
        Data['Stim'] = mat['Data'].Cell9.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 8 and mat['Data'].Cell9.ExptID8 == 'IV':
        Data['Raw'] = mat['Data'].Cell9.Exp8
        Data['Stim'] = mat['Data'].Cell9.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell9.ExptID8 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell9.Exp8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell9.ExptID8 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell9.Exp8
        Data['Stim'] = mat['Data'].Cell9.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell9.ExptID8 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell9.Exp8
        Data['Stim'] = mat['Data'].Cell9.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell9.ExptID8 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell9.Exp8
        Data['Stim'] = mat['Data'].Cell9.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell9.ExptID8 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell9.Exp8
        Data['Stim'] = mat['Data'].Cell9.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell9.ExptID8 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell9.Exp8
        Data['Stim'] = mat['Data'].Cell9.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell9.ExptID8 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell9.Exp8
        Data['Stim'] = mat['Data'].Cell9.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell9.ExptID8 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell9.Exp8
        Data['Stim'] = mat['Data'].Cell9.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
    
    if User_choices['ExptVal'] == 9 and mat['Data'].Cell9.ExptID9 == 'IV':
        Data['Raw'] = mat['Data'].Cell9.Exp9
        Data['Stim'] = mat['Data'].Cell9.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell9.ExptID9 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell9.Exp9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell9.ExptID9 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell9.Exp9
        Data['Stim'] = mat['Data'].Cell9.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell9.ExptID9 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell9.Exp9
        Data['Stim'] = mat['Data'].Cell9.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell9.ExptID9 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell9.Exp9
        Data['Stim'] = mat['Data'].Cell9.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell9.ExptID9 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell9.Exp9
        Data['Stim'] = mat['Data'].Cell9.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell9.ExptID9 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell9.Exp9
        Data['Stim'] = mat['Data'].Cell9.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell9.ExptID9 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell9.Exp9
        Data['Stim'] = mat['Data'].Cell9.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell9.ExptID9 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell9.Exp9
        Data['Stim'] = mat['Data'].Cell9.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 10 and mat['Data'].Cell9.ExptID10 == 'IV':
        Data['Raw'] = mat['Data'].Cell9.Exp10
        Data['Stim'] = mat['Data'].Cell9.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell9.ExptID10 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell9.Exp10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell9.ExptID10 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell9.Exp10
        Data['Stim'] = mat['Data'].Cell9.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell9.ExptID10 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell9.Exp10
        Data['Stim'] = mat['Data'].Cell9.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell9.ExptID10 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell9.Exp10
        Data['Stim'] = mat['Data'].Cell9.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell9.ExptID10 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell9.Exp10
        Data['Stim'] = mat['Data'].Cell9.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell9.ExptID10 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell9.Exp10
        Data['Stim'] = mat['Data'].Cell9.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell9.ExptID10 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell9.Exp10
        Data['Stim'] = mat['Data'].Cell9.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell9.ExptID10 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell9.Exp10
        Data['Stim'] = mat['Data'].Cell9.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 11 and mat['Data'].Cell9.ExptID11 == 'IV':
        Data['Raw'] = mat['Data'].Cell9.Exp11
        Data['Stim'] = mat['Data'].Cell9.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell9.ExptID11 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell9.Exp11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell9.ExptID11 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell9.Exp11
        Data['Stim'] = mat['Data'].Cell9.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell9.ExptID11 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell9.Exp11
        Data['Stim'] = mat['Data'].Cell9.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell9.ExptID11 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell9.Exp11
        Data['Stim'] = mat['Data'].Cell9.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell9.ExptID11 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell9.Exp11
        Data['Stim'] = mat['Data'].Cell9.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell9.ExptID11 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell9.Exp11
        Data['Stim'] = mat['Data'].Cell9.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell9.ExptID11 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell9.Exp11
        Data['Stim'] = mat['Data'].Cell9.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell9.ExptID11 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell9.Exp11
        Data['Stim'] = mat['Data'].Cell9.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 12 and mat['Data'].Cell9.ExptID12 == 'IV':
        Data['Raw'] = mat['Data'].Cell9.Exp12
        Data['Stim'] = mat['Data'].Cell9.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell9.ExptID12 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell9.Exp12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell9.ExptID12 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell9.Exp12
        Data['Stim'] = mat['Data'].Cell9.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell9.ExptID12 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell9.Exp12
        Data['Stim'] = mat['Data'].Cell9.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell9.ExptID12 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell9.Exp12
        Data['Stim'] = mat['Data'].Cell9.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell9.ExptID12 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell9.Exp12
        Data['Stim'] = mat['Data'].Cell9.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell9.ExptID12 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell9.Exp12
        Data['Stim'] = mat['Data'].Cell9.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell9.ExptID12 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell9.Exp12
        Data['Stim'] = mat['Data'].Cell9.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell9.ExptID12 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell9.Exp12
        Data['Stim'] = mat['Data'].Cell9.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 13 and mat['Data'].Cell9.ExptID13 == 'IV':
        Data['Raw'] = mat['Data'].Cell9.Exp13
        Data['Stim'] = mat['Data'].Cell9.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell9.ExptID13 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell9.Exp13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell9.ExptID13 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell9.Exp13
        Data['Stim'] = mat['Data'].Cell9.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell9.ExptID13 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell9.Exp13
        Data['Stim'] = mat['Data'].Cell9.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell9.ExptID13 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell9.Exp13
        Data['Stim'] = mat['Data'].Cell9.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell9.ExptID13 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell9.Exp13
        Data['Stim'] = mat['Data'].Cell9.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell9.ExptID13 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell9.Exp13
        Data['Stim'] = mat['Data'].Cell9.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell9.ExptID13 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell9.Exp13
        Data['Stim'] = mat['Data'].Cell9.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell9.ExptID13 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell9.Exp13
        Data['Stim'] = mat['Data'].Cell9.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 14 and mat['Data'].Cell9.ExptID14 == 'IV':
        Data['Raw'] = mat['Data'].Cell9.Exp14
        Data['Stim'] = mat['Data'].Cell9.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell9.ExptID14 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell9.Exp14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell9.ExptI4 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell9.Exp14
        Data['Stim'] = mat['Data'].Cell9.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell9.ExptID14 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell9.Exp14
        Data['Stim'] = mat['Data'].Cell9.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell9.ExptID14 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell9.Exp14
        Data['Stim'] = mat['Data'].Cell9.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell9.ExptID14 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell9.Exp14
        Data['Stim'] = mat['Data'].Cell9.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell9.ExptID14 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell9.Exp14
        Data['Stim'] = mat['Data'].Cell9.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell9.ExptID14 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell9.Exp14
        Data['Stim'] = mat['Data'].Cell9.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell9.ExptID14 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell9.Exp14
        Data['Stim'] = mat['Data'].Cell9.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 15 and mat['Data'].Cell9.ExptID15== 'IV':
        Data['Raw'] = mat['Data'].Cell9.Exp15
        Data['Stim'] = mat['Data'].Cell9.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell9.ExptID15 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell9.Exp15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell9.ExptID15 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell9.Exp15
        Data['Stim'] = mat['Data'].Cell9.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell9.ExptID15 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell9.Exp15
        Data['Stim'] = mat['Data'].Cell9.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell9.ExptID15== 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell9.Exp15
        Data['Stim'] = mat['Data'].Cell9.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell9.ExptID15 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell9.Exp15
        Data['Stim'] = mat['Data'].Cell9.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell9.ExptID15 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell9.Exp15
        Data['Stim'] = mat['Data'].Cell9.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell9.ExptID15 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell9.Exp15
        Data['Stim'] = mat['Data'].Cell9.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell9.ExptID15 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell9.Exp15
        Data['Stim'] = mat['Data'].Cell9.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

if User_choices['CellVal'] == 10:
    if User_choices['ExptVal'] == 1 and mat['Data'].Cell10.ExptID1 == 'IV':
        Data['Raw'] = mat['Data'].Cell10.Exp1
        Data['Stim'] = mat['Data'].Cell10.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell10.ExptID1 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell10.Exp1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell10.ExptID1 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell10.Exp1
        Data['Stim'] = mat['Data'].Cell10.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell10.ExptID1 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell10.Exp1
        Data['Stim'] = mat['Data'].Cell10.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell10.ExptID1 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell10.Exp1
        Data['Stim'] = mat['Data'].Cell10.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell.ExptID1 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell10.Exp1
        Data['Stim'] = mat['Data'].Cell10.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell10.ExptID1 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell10.Exp1
        Data['Stim'] = mat['Data'].Cell10.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell10.ExptID1 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell10.Exp1
        Data['Stim'] = mat['Data'].Cell10.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 1 and mat['Data'].Cell10.ExptID1 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell10.Exp1
        Data['Stim'] = mat['Data'].Cell10.Stim1
        Data['TraceMax'] = cols1
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 2 and mat['Data'].Cell10.ExptID2 == 'IV':
        Data['Raw'] = mat['Data'].Cell10.Exp2
        Data['Stim'] = mat['Data'].Cell10.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell10.ExptID2 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell10.Exp2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell10.ExptID2 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell10.Exp2
        Data['Stim'] = mat['Data'].Cell10.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell10.ExptID2 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell10.Exp2
        Data['Stim'] = mat['Data'].Cell10.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell10.ExptID2 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell10.Exp2
        Data['Stim'] = mat['Data'].Cell10.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell10.ExptID2 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell10.Exp2
        Data['Stim'] = mat['Data'].Cell10.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell10.ExptID2 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell10.Exp2
        Data['Stim'] = mat['Data'].Cell10.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell10.ExptID2 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell10.Exp2
        Data['Stim'] = mat['Data'].Cell10.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 2 and mat['Data'].Cell10.ExptID2 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell10.Exp2
        Data['Stim'] = mat['Data'].Cell10.Stim2
        Data['TraceMax'] = cols2
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 3 and mat['Data'].Cell10.ExptID3 == 'IV':
        Data['Raw'] = mat['Data'].Cell10.Exp3
        Data['Stim'] = mat['Data'].Cell10.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell10.ExptID3 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell10.Exp3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell10.ExptID3 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell10.Exp3
        Data['Stim'] = mat['Data'].Cell10.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell10.ExptID3 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell10.Exp3
        Data['Stim'] = mat['Data'].Cell10.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell10.ExptID3 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell10.Exp3
        Data['Stim'] = mat['Data'].Cell10.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell10.ExptID3 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell10.Exp3
        Data['Stim'] = mat['Data'].Cell10.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell10.ExptID3 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell10.Exp3
        Data['Stim'] = mat['Data'].Cell10.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell10.ExptID3 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell10.Exp3
        Data['Stim'] = mat['Data'].Cell10.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 3 and mat['Data'].Cell10.ExptID3 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell10.Exp3
        Data['Stim'] = mat['Data'].Cell10.Stim3
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
    
    if User_choices['ExptVal'] == 4 and mat['Data'].Cell10.ExptID4 == 'IV':
        Data['Raw'] = mat['Data'].Cell10.Exp4
        Data['Stim'] = mat['Data'].Cell10.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell10.ExptID4 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell10.Exp4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell10.ExptID4 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell10.Exp4
        Data['Stim'] = mat['Data'].Cell10.Stim4
        Data['TraceMax'] = cols3
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell10.ExptID4 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell10.Exp4
        Data['Stim'] = mat['Data'].Cell10.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell10.ExptID4 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell10.Exp4
        Data['Stim'] = mat['Data'].Cell10.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell10.ExptID4 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell10.Exp4
        Data['Stim'] = mat['Data'].Cell10.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell10.ExptID4 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell10.Exp4
        Data['Stim'] = mat['Data'].Cell10.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell10.ExptID4 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell10.Exp4
        Data['Stim'] = mat['Data'].Cell10.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 4 and mat['Data'].Cell10.ExptID4 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell10.Exp4
        Data['Stim'] = mat['Data'].Cell10.Stim4
        Data['TraceMax'] = cols4
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 5 and mat['Data'].Cell10.ExptID5 == 'IV':
        Data['Raw'] = mat['Data'].Cell10.Exp5
        Data['Stim'] = mat['Data'].Cell10.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell10.ExptID5 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell10.Exp5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell10.ExptID5 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell10.Exp5
        Data['Stim'] = mat['Data'].Cell10.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell10.ExptID5 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell10.Exp5
        Data['Stim'] = mat['Data'].Cell10.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell10.ExptID5 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell10.Exp5
        Data['Stim'] = mat['Data'].Cell10.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell10.ExptID5 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell10.Exp5
        Data['Stim'] = mat['Data'].Cell10.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell10.ExptID5 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell10.Exp5
        Data['Stim'] = mat['Data'].Cell10.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell10.ExptID5 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell10.Exp5
        Data['Stim'] = mat['Data'].Cell10.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 5 and mat['Data'].Cell10.ExptID5 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell10.Exp5
        Data['Stim'] = mat['Data'].Cell10.Stim5
        Data['TraceMax'] = cols5
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]        
        
    if User_choices['ExptVal'] == 6 and mat['Data'].Cell10.ExptID6 == 'IV':
        Data['Raw'] = mat['Data'].Cell10.Exp6
        Data['Stim'] = mat['Data'].Cell10.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell10.ExptID6 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell10.Exp6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell10.ExptID6 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell10.Exp6
        Data['Stim'] = mat['Data'].Cell10.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell10.ExptID6 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell10.Exp6
        Data['Stim'] = mat['Data'].Cell10.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell10.ExptID6 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell10.Exp6
        Data['Stim'] = mat['Data'].Cell10.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell10.ExptID6 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell10.Exp6
        Data['Stim'] = mat['Data'].Cell10.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell10.ExptID6 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell10.Exp6
        Data['Stim'] = mat['Data'].Cell10.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell10.ExptID6 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell10.Exp6
        Data['Stim'] = mat['Data'].Cell10.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 6 and mat['Data'].Cell10.ExptID6 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell10.Exp6
        Data['Stim'] = mat['Data'].Cell10.Stim6
        Data['TraceMax'] = cols6
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]        
        
    if User_choices['ExptVal'] == 7 and mat['Data'].Cell10.ExptID7 == 'IV':
        Data['Raw'] = mat['Data'].Cell10.Exp7
        Data['Stim'] = mat['Data'].Cell10.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell10.ExptID7 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell10.Exp7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell10.ExptID7 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell10.Exp7
        Data['Stim'] = mat['Data'].Cell10.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell10.ExptID7 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell10.Exp7
        Data['Stim'] = mat['Data'].Cell10.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell10.ExptID7 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell10.Exp7
        Data['Stim'] = mat['Data'].Cell10.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell10.ExptID7 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell10.Exp7
        Data['Stim'] = mat['Data'].Cell10.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell10.ExptID7 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell10.Exp7
        Data['Stim'] = mat['Data'].Cell10.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell10.ExptID7 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell10.Exp7
        Data['Stim'] = mat['Data'].Cell10.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 7 and mat['Data'].Cell10.ExptID7 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell10.Exp7
        Data['Stim'] = mat['Data'].Cell10.Stim7
        Data['TraceMax'] = cols7
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 8 and mat['Data'].Cell10.ExptID8 == 'IV':
        Data['Raw'] = mat['Data'].Cell10.Exp8
        Data['Stim'] = mat['Data'].Cell10.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell10.ExptID8 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell10.Exp8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell10.ExptID8 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell10.Exp8
        Data['Stim'] = mat['Data'].Cell10.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell10.ExptID8 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell10.Exp8
        Data['Stim'] = mat['Data'].Cell10.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell10.ExptID8 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell10.Exp8
        Data['Stim'] = mat['Data'].Cell10.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell10.ExptID8 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell10.Exp8
        Data['Stim'] = mat['Data'].Cell10.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell10.ExptID8 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell10.Exp8
        Data['Stim'] = mat['Data'].Cell10.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell10.ExptID8 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell10.Exp8
        Data['Stim'] = mat['Data'].Cell10.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 8 and mat['Data'].Cell10.ExptID8 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell10.Exp8
        Data['Stim'] = mat['Data'].Cell10.Stim8
        Data['TraceMax'] = cols8
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
    
    if User_choices['ExptVal'] == 9 and mat['Data'].Cell10.ExptID9 == 'IV':
        Data['Raw'] = mat['Data'].Cell10.Exp9
        Data['Stim'] = mat['Data'].Cell10.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell10.ExptID9 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell10.Exp9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell10.ExptID9 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell10.Exp9
        Data['Stim'] = mat['Data'].Cell10.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell10.ExptID9 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell10.Exp9
        Data['Stim'] = mat['Data'].Cell10.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell10.ExptID9 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell10.Exp9
        Data['Stim'] = mat['Data'].Cell10.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell10.ExptID9 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell10.Exp9
        Data['Stim'] = mat['Data'].Cell10.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell10.ExptID9 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell10.Exp9
        Data['Stim'] = mat['Data'].Cell10.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell10.ExptID9 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell10.Exp9
        Data['Stim'] = mat['Data'].Cell10.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 9 and mat['Data'].Cell10.ExptID9 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell10.Exp9
        Data['Stim'] = mat['Data'].Cell10.Stim9
        Data['TraceMax'] = cols9
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 10 and mat['Data'].Cell10.ExptID10 == 'IV':
        Data['Raw'] = mat['Data'].Cell10.Exp10
        Data['Stim'] = mat['Data'].Cell10.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell10.ExptID10 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell10.Exp10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell10.ExptID10 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell10.Exp10
        Data['Stim'] = mat['Data'].Cell10.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell10.ExptID10 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell10.Exp10
        Data['Stim'] = mat['Data'].Cell10.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell10.ExptID10 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell10.Exp10
        Data['Stim'] = mat['Data'].Cell10.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell10.ExptID10 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell10.Exp10
        Data['Stim'] = mat['Data'].Cell10.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell10.ExptID10 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell10.Exp10
        Data['Stim'] = mat['Data'].Cell10.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell10.ExptID10 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell10.Exp10
        Data['Stim'] = mat['Data'].Cell10.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 10 and mat['Data'].Cell10.ExptID10 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell10.Exp10
        Data['Stim'] = mat['Data'].Cell10.Stim10
        Data['TraceMax'] = cols10
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 11 and mat['Data'].Cell10.ExptID11 == 'IV':
        Data['Raw'] = mat['Data'].Cell10.Exp11
        Data['Stim'] = mat['Data'].Cell10.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell10.ExptID11 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell10.Exp11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell10.ExptID11 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell10.Exp11
        Data['Stim'] = mat['Data'].Cell10.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell10.ExptID11 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell10.Exp11
        Data['Stim'] = mat['Data'].Cell10.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell10.ExptID11 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell10.Exp11
        Data['Stim'] = mat['Data'].Cell10.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell10.ExptID11 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell10.Exp11
        Data['Stim'] = mat['Data'].Cell10.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell10.ExptID11 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell10.Exp11
        Data['Stim'] = mat['Data'].Cell10.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell10.ExptID11 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell10.Exp11
        Data['Stim'] = mat['Data'].Cell10.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 11 and mat['Data'].Cell10.ExptID11 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell10.Exp11
        Data['Stim'] = mat['Data'].Cell10.Stim11
        Data['TraceMax'] = cols11
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 12 and mat['Data'].Cell10.ExptID12 == 'IV':
        Data['Raw'] = mat['Data'].Cell10.Exp12
        Data['Stim'] = mat['Data'].Cell10.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell10.ExptID12 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell10.Exp12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell10.ExptID12 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell10.Exp12
        Data['Stim'] = mat['Data'].Cell10.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell10.ExptID12 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell10.Exp12
        Data['Stim'] = mat['Data'].Cell10.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell10.ExptID12 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell10.Exp12
        Data['Stim'] = mat['Data'].Cell10.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell10.ExptID12 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell10.Exp12
        Data['Stim'] = mat['Data'].Cell10.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell10.ExptID12 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell10.Exp12
        Data['Stim'] = mat['Data'].Cell10.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell10.ExptID12 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell10.Exp12
        Data['Stim'] = mat['Data'].Cell10.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 12 and mat['Data'].Cell10.ExptID12 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell10.Exp12
        Data['Stim'] = mat['Data'].Cell10.Stim12
        Data['TraceMax'] = cols12
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 13 and mat['Data'].Cell10.ExptID13 == 'IV':
        Data['Raw'] = mat['Data'].Cell10.Exp13
        Data['Stim'] = mat['Data'].Cell10.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell10.ExptID13 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell10.Exp13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell10.ExptID13 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell10.Exp13
        Data['Stim'] = mat['Data'].Cell10.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell10.ExptID13 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell10.Exp13
        Data['Stim'] = mat['Data'].Cell10.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell10.ExptID13 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell10.Exp13
        Data['Stim'] = mat['Data'].Cell10.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell10.ExptID13 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell10.Exp13
        Data['Stim'] = mat['Data'].Cell10.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell10.ExptID13 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell10.Exp13
        Data['Stim'] = mat['Data'].Cell10.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell10.ExptID13 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell10.Exp13
        Data['Stim'] = mat['Data'].Cell10.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 13 and mat['Data'].Cell10.ExptID13 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell10.Exp13
        Data['Stim'] = mat['Data'].Cell10.Stim13
        Data['TraceMax'] = cols13
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]
        
    if User_choices['ExptVal'] == 14 and mat['Data'].Cell10.ExptID14 == 'IV':
        Data['Raw'] = mat['Data'].Cell10.Exp14
        Data['Stim'] = mat['Data'].Cell10.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell10.ExptID14 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell10.Exp14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell10.ExptI4 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell10.Exp14
        Data['Stim'] = mat['Data'].Cell10.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell10.ExptID14 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell10.Exp14
        Data['Stim'] = mat['Data'].Cell10.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell10.ExptID14 == 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell10.Exp14
        Data['Stim'] = mat['Data'].Cell10.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell10.ExptID14 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell10.Exp14
        Data['Stim'] = mat['Data'].Cell10.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell10.ExptID14 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell10.Exp14
        Data['Stim'] = mat['Data'].Cell10.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell10.ExptID14 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell10.Exp14
        Data['Stim'] = mat['Data'].Cell10.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 14 and mat['Data'].Cell10.ExptID14 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell10.Exp14
        Data['Stim'] = mat['Data'].Cell10.Stim14
        Data['TraceMax'] = cols14
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]

    if User_choices['ExptVal'] == 15 and mat['Data'].Cell10.ExptID15== 'IV':
        Data['Raw'] = mat['Data'].Cell10.Exp15
        Data['Stim'] = mat['Data'].Cell10.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['Raw'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell10.ExptID15 == 'TBS induction':
        Data['RawTBS'] = mat['Data'].Cell10.Exp15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawTBS'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell10.ExptID15 == 'PPR CC':
        Data['RawPPRCC'] = mat['Data'].Cell10.Exp15
        Data['Stim'] = mat['Data'].Cell10.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell10.ExptID15 == 'SP CC':
        Data['SPCC'] = mat['Data'].Cell10.Exp15
        Data['Stim'] = mat['Data'].Cell10.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['SPCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell10.ExptID15== 'PPR VC':
        Data['RawPPRVC'] = mat['Data'].Cell10.Exp15
        Data['Stim'] = mat['Data'].Cell10.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['RawPPRVC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell10.ExptID15 == 'NMDA VC':
        Data['NMDA'] = mat['Data'].Cell10.Exp15
        Data['Stim'] = mat['Data'].Cell10.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['NMDA'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell10.ExptID15 == 'AMPA VC':
        Data['AMPA'] = mat['Data'].Cell10.Exp15
        Data['Stim'] = mat['Data'].Cell10.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['AMPA'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell10.ExptID15 == 'Train CC':
        Data['TrainCC'] = mat['Data'].Cell10.Exp15
        Data['Stim'] = mat['Data'].Cell10.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['TrainCC'].shape[0]]
    elif User_choices['ExptVal'] == 15 and mat['Data'].Cell10.ExptID15 == 'Train VC':
        Data['TrainVC'] = mat['Data'].Cell10.Exp15
        Data['Stim'] = mat['Data'].Cell10.Stim15
        Data['TraceMax'] = cols15
        Data['Time'] = mat['Data'].Time[0:Data['TrainVC'].shape[0]]    
    
#Calculates IV curve parameters including spikecount, RMP, Rin, Freq, etc.
if 'Raw' in Data:
    x = 0
    for i in Data['Raw'][x:Data['TraceMax']:1]:
        trace1 = {}
        trace1['T'] = Data['Time'][:]
        trace1['V'] = Data['Raw'][:,x]
        trace1['stim_start'] = [201]
        trace1['stim_end'] = [700]
        traces = [trace1]
        traces_results = efel.getFeatureValues(traces,['Spikecount','voltage_base'])
    
        #If a Spikecount of 0 is detected, continue for loop
        #Cannot append "N/A" as the DictWriter won't work
        if traces_results[0]['Spikecount'] == 0:
            x += 1
            continue
        
        #If a Spikecount of 1 is detected, plot graph and continue
        #Potential to be modified if Threshold_AP is needed for each trace
        if traces_results[0]['Spikecount'] == 1:
            Trace_Results = {'AP #': int(traces_results[0]['Spikecount']), 'RMP': float(traces_results[0]['voltage_base'])}
            Results.append(Trace_Results)
            
            plt.plot(Data['Time'],Data['Raw'][:,x])
            plt.title('Cell ' + str(User_choices['CellVal']) + ', Trace ' + str(x))
            plt.xlabel('Time (in ms)')
            plt.ylabel('Voltage (in mV)')
            plt.show()
            x+= 1
            continue
        
        #If Spikecount is greater than 1, the code continues as normal
        if traces_results[0]['Spikecount'] >= 2:
            traces_results = efel.getFeatureValues(traces,[
                'AP_begin_voltage','voltage_base','AP_amplitude','AP_rise_time',
                'Spikecount','min_AHP_values','AP_begin_indices','peak_time','spike_width2'
                ,'peak_voltage'])

            #Error if operands of AP_begin_voltage and min_AHP_values are not equal
            #This code automatically removes the erroneous values (usually the last value(s)) and makes the number of values equal for further calculations
            if len(traces_results[0]['min_AHP_values']) != len(traces_results[0]['AP_begin_voltage']):
                if len(traces_results[0]['min_AHP_values']) > len(traces_results[0]['AP_begin_voltage']):
                    traces_results[0]['min_AHP_values'] = np.delete(traces_results[0]['min_AHP_values'],-1)
                elif len(traces_results[0]['AP_begin_voltage']) > len(traces_results[0]['min_AHP_values']):
                    traces_results[0]['AP_begin_voltage'] = np.delete(traces_results[0]['AP_begin_voltage'],-1)
                    traces_results[0]['AP_begin_indices'] = np.delete(traces_results[0]['AP_begin_indices'],-1)
    
            #Calculate ISI values based on AP_begin_indices and multiply each value by the sampling point (0.05ms)
            if traces_results[0]['Spikecount'] == 2:
                traces_results[0]['ISI_values'] = float(traces_results[0]['AP_begin_indices'][-1] - traces_results[0]['AP_begin_indices'][0]) * 0.05
            elif traces_results[0]['Spikecount'] > 2:    
                traces_results[0]['ISI_values'] = np.diff(traces_results[0]['AP_begin_indices']) * 0.05
    
            #Calculate initial ISI value and insert this value into the 0 position of ISI values
            FirstISI = traces_results[0]['peak_time'][1] - traces_results[0]['peak_time'][0]
            traces_results[0]['ISI_values'] = np.insert(traces_results[0]['ISI_values'],0,FirstISI)    
        
            #Calculate AHP parameters
            trace_calc['AHP'] = traces_results[0]['min_AHP_values'] - traces_results[0]['AP_begin_voltage']
            
            #Calculate Duration of Spiking
            trace_calc['SpikeDur'] = Data['Time'][[traces_results[0]['AP_begin_indices'][-1]]] - Data['Time'][[traces_results[0]['AP_begin_indices'][0]]]

            #Calculate input resistance based on lowest hyperpolarizing step (Hard coded hyperpolarizing step)
            trace_calc['Vin'] = (((Data['Raw'][6000,4]) - (Data['Raw'][2000,4])) / 1000) #Voltage is calculated in mV, but converted to V
            trace_calc['Iin'] = (((Data['Stim'][6000,4]) - (Data['Stim'][2000,4])) / 1000000) #Current is calculated in microA, but converted to A
            trace_calc['Rin'] = ((trace_calc['Vin']/trace_calc['Iin']) / 1000) #Resistance is provided in MOhms
            
            #Calculate frequency and adaptation parameters
            Frequency = 1/traces_results[0]['ISI_values']
            trace_calc['MeanInstFreq'] = np.mean(Frequency)*1000
            trace_calc['MaxFreq'] = max(Frequency)*1000
            trace_calc['FreqAdapt'] = traces_results[0]['ISI_values'][-1] / traces_results[0]['ISI_values'][0]
            trace_calc['PeakAdapt'] = traces_results[0]['AP_amplitude'][-1] / traces_results[0]['AP_amplitude'][0]
            
            #Plot graphs in the output window
            peak_time = traces_results[0]['peak_time'][0:len(traces_results[0]['peak_voltage'])]
            plt.plot(Data['Time'],Data['Raw'][:,x])
            plt.title('Cell ' + str(User_choices['CellVal']) + ', Trace ' + str(x))
            plt.xlabel('Time (in ms)')
            plt.ylabel('Voltage (in mV)')
            plt.scatter(peak_time,traces_results[0]['peak_voltage'] + 20,c='r',marker = '+')
            plt.show()
            
            #Save results in a dictionary
            Trace_Results = {'AP #': int(traces_results[0]['Spikecount']), 'RMP': float(traces_results[0]['voltage_base']),
                             'Rin': trace_calc['Rin'], 'Duration_of_Spiking': float(trace_calc['SpikeDur']),
                             'Mean_AP_Half-Height_Width': np.mean(traces_results[0]['spike_width2']), 'Mean_AP_Amplitude': np.mean(traces_results[0]['AP_amplitude']),
                             'Mean_Inst_Freq': trace_calc['MeanInstFreq'], 'Max_Freq': trace_calc['MaxFreq'], 
                             'Freq_Adapt': trace_calc['FreqAdapt'], 'Peak_Adapt': trace_calc['PeakAdapt'],
                             'Mean_ISI': np.mean(traces_results[0]['ISI_values']), 'Mean_AHP_Amplitude': np.mean(trace_calc['AHP'])}
            
            #Append each dictionary into a list
            Results.append(Trace_Results)
            
            #Variable to iterate through the traces
            x += 1
    
    plt.plot(Data['Time'],Data['Raw'])
    #plt.title('All Traces for Cell' + str(User_choices['CellVal']))
    plt.xlabel('Time (in ms)')
    plt.ylabel('Voltage (in mV)')
    plt.show()
    
    #Outputs IV parameters into a CSV
    with open(str(file) + '_IV_Results' + '.csv','w') as IV:
        writer1 = DictWriter(IV,('AP #','RMP','Rin','Duration_of_Spiking',
                                 'Mean_AP_Half-Height_Width','Mean_AP_Amplitude',
                                 'Mean_Inst_Freq','Max_Freq','Freq_Adapt','Peak_Adapt',
                                 'Mean_ISI','Mean_AHP_Amplitude'))
        writer1.writeheader()
        writer1.writerows(Results)
        IV.close()            

    if not Results:
        print('\n' + 'No spikes detected in Experiment ' + str(User_choices['ExptVal']) + ' for Cell ' + str(User_choices['CellVal']))