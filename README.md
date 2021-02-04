Custom scripts utilizing the numerous github scripts (BlueBrain/EFEL, HEKA_Importer, and ABF_Importer) code to import, organize, analyze and plot ex vivo whole-cell patch clamp electrophysiology data.



# HEKAv2.mat File
The HEKAv2.mat file is used in conjunction with the HEKA_to_Pyv2.py file.
The import file is the .dat file output from the HEKA Patchmaster Next software.

***NOTE: For the HEKAv2.mat file to work, you must have the HEKA_Importer folder in the same folder as the HEKA Patchmaster .dat file***
The HEKA_Importer script can be found here: https://github.com/ChristianKeine/HEKA_Patchmaster_Importer

1. Run the HEKAv2 MATLAB script on the appropriate .dat file (ensuring that the HEKA_Importer file is present in the same folder as the .dat file)

2. The script will calculate time constant (based on a sampling frequency of 20kHz), number of cells (up to 3), and the number of experiments for each cell. Additionally, it will segregate experiments/traces into a single array.

3. Finally, the script will save the Data Array, Time Constant, Number of Cells, and Number of Experiments in a mat file labeled as the filename minus the .dat extension.
**NOTE: I use Spyder for running my code**

4. Within Python, ensure that the proper libraries are installed (e.g. scipy.io, efel, numpy, matplotlib, etc.)

5. Run the "Heka_to_Pyv2.py" script and select the MATLAB file via the tkinter dialog box

6. The script will print the number of cells (up to 3) and the number of experiments within each cell

7. Next input the cell number you would like to analyze (from 1-3), the experiment you would like to analyze, and the trace (or all traces) you would like to analyze

8a. If you input a single value (0-10) and the code ran successfully, a graph of the trace should appear along with an accompanying "Trace # of Cell # analyzed successfully!" The data will be stored in the appropriate cell variable (SingleC#Trace)

8b. If you input all traces value (12) and the code ran successfully, the data will be stored in the appropriate variable (AllC#Traces) with an accompanying "All traces analyzed successfully!" for each trace analyzed.





# ABF_to_Py_efel.py File
The ABF_to_Py_efel.py file utilizes an ABF import code along with the EFEL code to import, analyze, and export analytical parameters as CSVs.
The ABF Importer can be found here: https://pypi.org/project/pyabf/

1. Run the ABF_to_Py_efel.py script by selecting the appropriate .abf file

2. The script will import, organize, analyze, and output two CSV files (Threshold_AP and AllAverages
