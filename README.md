Custom scripts utilizing other github-related scripts (BlueBrain/EFEL, HEKA_Importer, and ABF_Importer) code to import, organize, analyze and plot ex vivo whole-cell patch clamp electrophysiology data.

# HEKA_Importer Script (MATLAB)
This script is used in conjunction with the "Multi-Ephys-HEKA-Analysis.py" script.
Import file is a .dat file from Patchmaster Next.
Output file is a .mat file with a nested structure containing trace data, stim data, and experiment information.
Example .dat file has been provided.

***Note: For this file to work, you must have the HEKA_Importer folder (https://github.com/ChristianKeine/HEKA_Patchmaster_Importer) in the same folder as the .dat file.

# Multi_Ephys_HEKA_Analysis Script (PYTHON)
This script imports, organizes, analyzes, plots, and saves data from a .mat file
Import file is a .mat file from the previous script.
Output file is a .csv file containing either IV parameters (EFEL) or PSP amplitude parameter (Custom).
Example .mat file has been provided.

# ABF_EFELv1 Script (PYTHON)
This script imports, organizes, analyzes, plots, and saves data from a .abf file
Import file is a .abf file
Output file are two .csv files containing threshold AP parameters (EFEL) and IV averaged parameters (EFEL)
Example .abf file has been provided.

***Note: ABF importer code can be found here (https://pypi.org/project/pyabf/).
