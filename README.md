Custom scripts utilizing other github-related scripts (BlueBrain/EFEL, HEKA_Importer, and ABF_Importer) code to import, organize, analyze and plot ex vivo whole-cell patch clamp electrophysiology data.

# HEKA_Importer Script (MATLAB)
This script is used in conjunction with the "Multi-Ephys-HEKA-Analysis.py" script.

Import file is a .dat file from Patchmaster Next.

Output file is a .mat file with a nested structure containing trace data, stim data, and experiment information.

Example .dat file has been provided.

***Note: For this file to work, you must have the HEKA_Importer folder (https://github.com/ChristianKeine/HEKA_Patchmaster_Importer) in the same folder as the .dat file.

# Multi_Ephys_Analysis Script (PYTHON)
This script imports, organizes, analyzes, plots, and saves data from a .mat file

UPDATED = 3/2/2022 --> Script now contains a defined function that saved ~7000 lines by loading the matlab file into a dictionary instead of using explicit dot notation to load in each parameter.

Import file is a .mat file from the previous script (HEKA_Importer)

Output file now varies and it is dependent on the user's needs. Users can input whether they want to save graphs as SVGs, while output files are automatically saved as *.txt files in the working directoy. There is an exception as the IV data is saved as a *.csv that contains numerous parameters for each sweep.

Example .mat file has been provided.

***Note: The basic IV parameters are calculated through a python-wrapped C++ code known as Electrophysiology Feature Library Extraction (EFEL) that has been developed through the BlueBrain Project at EPFL (https://github.com/BlueBrain/eFEL).

# Multi Parameter Scripts (PYTHON)
Updated = 3/2/22 --> Added three scripts (Multi_SP, Multi_PPR, and Multi_Train) that can perform grand averaging across multiple files.

# E/I Balance (PYTHON)
Updated = 3/2/22 --> Added another script (EI_Balance_Analysis) that takes the *.txt output files from the Multi_Ephys_Analysis script and calculates the E/I balance leves.

***Note = The SP text file needs to be selected before the EI file

# ABF_EFELv2 Script (PYTHON)
This script imports, organizes, analyzes, plots, and saves data from a .abf file

Import file is a .abf file

Output file are two .csv files containing threshold AP parameters (EFEL) and IV averaged parameters (EFEL)

Example .abf file has been provided.

v2 includes while loops to recognize/correct errors created by the EFEL script

***Note: ABF importer code can be found here (https://pypi.org/project/pyabf/).
