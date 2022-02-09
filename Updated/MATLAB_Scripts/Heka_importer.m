clear;
clc;
[path] = uigetdir;
cd(path);

%Load in file and save imported data into new variable ('data')
file = uigetfile;
filename = file(1:end-4);
HEKA_Importer(file)
all = ans;
clear ans;

%Create data structure to save all pertinent information
Data = struct();

%Determine number of cells
Data.CellNum = max(all.RecTable{:,1});
if strcmp(all.RecTable{1,2}, 'Exp-2')
    Data.CellNum = Data.CellNum + 1;
end

%Determine sampling frequency for each experiment type
timerow = 2;
Time(1,1) = 0;

SF = (1/all.RecTable{1,19})*1000; %This value must be set as the sampling frequency (20kHz)
for i = 1:99999
    Time(timerow,1) = 0 + SF;
    SF = SF + 0.05;
    timerow = timerow + 1;
end

Data.Time = Time;

%Preallocate nested cell data structures based on number of cells
if Data.CellNum == 1
    Data.Cell1 = [];
    Data.Cell1.Expts = 0;
elseif Data.CellNum == 2
    Data.Cell1 = [];
    Data.Cell2 = [];
    Data.Cell1.Expts = 0;
    Data.Cell2.Expts = 0;
elseif Data.CellNum == 3
    Data.Cell1 = [];
    Data.Cell2 = [];
    Data.Cell3 = [];
    Data.Cell1.Expts = 0;
    Data.Cell2.Expts = 0;
    Data.Cell3.Expts = 0;
elseif Data.CellNum == 4
    Data.Cell1 = [];
    Data.Cell2 = [];
    Data.Cell3 = [];
    Data.Cell4 = [];
    Data.Cell1.Expts = 0;
    Data.Cell2.Expts = 0;
    Data.Cell3.Expts = 0;
    Data.Cell4.Expts = 0;
elseif Data.CellNum == 5
    Data.Cell1 = [];
    Data.Cell2 = [];
    Data.Cell3 = [];
    Data.Cell4 = [];
    Data.Cell5 = [];
    Data.Cell1.Expts = 0;
    Data.Cell2.Expts = 0;
    Data.Cell3.Expts = 0;
    Data.Cell4.Expts = 0;
    Data.Cell5.Expts = 0;
elseif Data.CellNum == 6
    Data.Cell1 = [];
    Data.Cell2 = [];
    Data.Cell3 = [];
    Data.Cell4 = [];
    Data.Cell5 = [];
    Data.Cell6 = [];
    Data.Cell1.Expts = 0;
    Data.Cell2.Expts = 0;
    Data.Cell3.Expts = 0;
    Data.Cell4.Expts = 0;
    Data.Cell5.Expts = 0;
    Data.Cell6.Expts = 0;
elseif Data.CellNum == 7
    Data.Cell1 = [];
    Data.Cell2 = [];
    Data.Cell3 = [];
    Data.Cell4 = [];
    Data.Cell5 = [];
    Data.Cell6 = [];
    Data.Cell7 = [];
    Data.Cell1.Expts = 0;
    Data.Cell2.Expts = 0;
    Data.Cell3.Expts = 0;
    Data.Cell4.Expts = 0;
    Data.Cell5.Expts = 0;
    Data.Cell6.Expts = 0;
    Data.Cell7.Expts = 0;
elseif Data.CellNum == 8
    Data.Cell1 = [];
    Data.Cell2 = [];
    Data.Cell3 = [];
    Data.Cell4 = [];
    Data.Cell5 = [];
    Data.Cell6 = [];
    Data.Cell7 = [];
    Data.Cell8 = [];
    Data.Cell1.Expts = 0;
    Data.Cell2.Expts = 0;
    Data.Cell3.Expts = 0;
    Data.Cell4.Expts = 0;
    Data.Cell5.Expts = 0;
    Data.Cell6.Expts = 0;
    Data.Cell7.Expts = 0;
    Data.Cell8.Expts = 0;
elseif Data.CellNum == 9
    Data.Cell1 = [];
    Data.Cell2 = [];
    Data.Cell3 = [];
    Data.Cell4 = [];
    Data.Cell5 = [];
    Data.Cell6 = [];
    Data.Cell7 = [];
    Data.Cell8 = [];
    Data.Cell9 = [];
    Data.Cell1.Expts = 0;
    Data.Cell2.Expts = 0;
    Data.Cell3.Expts = 0;
    Data.Cell4.Expts = 0;
    Data.Cell5.Expts = 0;
    Data.Cell6.Expts = 0;
    Data.Cell7.Expts = 0;
    Data.Cell8.Expts = 0;
    Data.Cell9.Expts = 0;
elseif Data.CellNum == 10
    Data.Cell1 = [];
    Data.Cell2 = [];
    Data.Cell3 = [];
    Data.Cell4 = [];
    Data.Cell5 = [];
    Data.Cell6 = [];
    Data.Cell7 = [];
    Data.Cell8 = [];
    Data.Cell9 = [];
    Data.Cell10 = [];
    Data.Cell1.Expts = 0;
    Data.Cell2.Expts = 0;
    Data.Cell3.Expts = 0;
    Data.Cell4.Expts = 0;
    Data.Cell5.Expts = 0;
    Data.Cell6.Expts = 0;
    Data.Cell7.Expts = 0;
    Data.Cell8.Expts = 0;
    Data.Cell9.Expts = 0;
    Data.Cell10.Expts = 0;
end

%Determine the number of experiments for each and save information inside
%nested structure for each cell
for i = 1:height(all.RecTable{:,2})
    if strcmp(all.RecTable{i,2}, 'Exp-1')
        Data.Cell1.Expts = Data.Cell1.Expts + 1;
    elseif strcmp(all.RecTable{i,2}, 'Exp-2')
        Data.Cell2.Expts = Data.Cell2.Expts + 1;
    elseif strcmp(all.RecTable{i,2}, 'Exp-3')
        Data.Cell3.Expts = Data.Cell3.Expts + 1;
    elseif strcmp(all.RecTable{i,2}, 'Exp-4')
        Data.Cell4.Expts = Data.Cell4.Expts + 1;
    elseif strcmp(all.RecTable{i,2}, 'Exp-5')
        Data.Cell5.Expts = Data.Cell5.Expts + 1;
    elseif strcmp(all.RecTable{i,2}, 'Exp-6')
        Data.Cell6.Expts = Data.Cell6.Expts + 1;
    elseif strcmp(all.RecTable{i,2}, 'Exp-7')
        Data.Cell7.Expts = Data.Cell7.Expts + 1;
    elseif strcmp(all.RecTable{i,2}, 'Exp-8')
        Data.Cell8.Expts = Data.Cell8.Expts + 1;
    elseif strcmp(all.RecTable{i,2}, 'Exp-9')
        Data.Cell9.Expts = Data.Cell9.Expts + 1;
    elseif strcmp(all.RecTable{i,2}, 'Exp-10')
        Data.Cell10.Expts = Data.Cell10.Expts + 1;
    end
end

%Move data related to each experiment within a cell into its own nested
%structure along with stimWave data to calculate input resistance and
%Experiment Identification
%Voltage response is also converted to mV (multiplied by 1000)
if Data.CellNum == 1
    for i = 1:Data.Cell1.Expts
        if i == 1
            Data.Cell1.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID1 = char(all.RecTable{i,10});
            Data.Cell1.Exp1 = Data.Cell1.Exp1 * 1000;
        elseif i == 2
            Data.Cell1.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID2 = char(all.RecTable{i,10});
            Data.Cell1.Exp2 = Data.Cell1.Exp2 * 1000;
        elseif i == 3
            Data.Cell1.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID3 = char(all.RecTable{i,10});
            Data.Cell1.Exp3 = Data.Cell1.Exp3 * 1000;
        elseif i == 4
            Data.Cell1.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID4 = char(all.RecTable{i,10});
            Data.Cell1.Exp4 = Data.Cell1.Exp4 * 1000;
        elseif i == 5
            Data.Cell1.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID5 = char(all.RecTable{i,10});
            Data.Cell1.Exp5 = Data.Cell1.Exp5 * 1000;
        elseif i == 6
            Data.Cell1.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID6 = char(all.RecTable{i,10});
            Data.Cell1.Exp6 = Data.Cell1.Exp6 * 1000;
        elseif i == 7
            Data.Cell1.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID7 = char(all.RecTable{i,10});
            Data.Cell1.Exp7 = Data.Cell1.Exp7 * 1000;
        elseif i == 8
            Data.Cell1.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID8 = char(all.RecTable{i,10});
            Data.Cell1.Exp8 = Data.Cell1.Exp8 * 1000;
        elseif i == 9
            Data.Cell1.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID9 = char(all.RecTable{i,10});
            Data.Cell1.Exp9 = Data.Cell1.Exp9 * 1000;
        elseif i == 10
            Data.Cell1.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID10 = char(all.RecTable{i,10});
            Data.Cell1.Exp10 = Data.Cell1.Exp10 * 1000;
        elseif i == 11
            Data.Cell1.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID11 = char(all.RecTable{i,10});
            Data.Cell1.Exp11 = Data.Cell1.Exp11 * 1000;
        elseif i == 12
            Data.Cell1.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID12 = char(all.RecTable{i,10});
            Data.Cell1.Exp12 = Data.Cell1.Exp12 * 1000;
        elseif i == 13
            Data.Cell1.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID13 = char(all.RecTable{i,10});
            Data.Cell1.Exp13 = Data.Cell1.Exp13 * 1000;
        elseif i == 14
            Data.Cell1.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID14 = char(all.RecTable{i,10});
            Data.Cell1.Exp14 = Data.Cell1.Exp14 * 1000;
        elseif i == 15
            Data.Cell1.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID15 = char(all.RecTable{i,10});
            Data.Cell1.Exp15 = Data.Cell1.Exp15 * 1000;
        end
    end
elseif Data.CellNum == 2
    for i = 1:Data.Cell1.Expts
        if i == 1
            Data.Cell1.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID1 = char(all.RecTable{i,10});
            Data.Cell1.Exp1 = Data.Cell1.Exp1 * 1000;
        elseif i == 2
            Data.Cell1.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID2 = char(all.RecTable{i,10});
            Data.Cell1.Exp2 = Data.Cell1.Exp2 * 1000;
        elseif i == 3
            Data.Cell1.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID3 = char(all.RecTable{i,10});
            Data.Cell1.Exp3 = Data.Cell1.Exp3 * 1000;
        elseif i == 4
            Data.Cell1.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID4 = char(all.RecTable{i,10});
            Data.Cell1.Exp4 = Data.Cell1.Exp4 * 1000;
        elseif i == 5
            Data.Cell1.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID5 = char(all.RecTable{i,10});
            Data.Cell1.Exp5 = Data.Cell1.Exp5 * 1000;
        elseif i == 6
            Data.Cell1.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID6 = char(all.RecTable{i,10});
            Data.Cell1.Exp6 = Data.Cell1.Exp6 * 1000;
        elseif i == 7
            Data.Cell1.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID7 = char(all.RecTable{i,10});
            Data.Cell1.Exp7 = Data.Cell1.Exp7 * 1000;
        elseif i == 8
            Data.Cell1.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID8 = char(all.RecTable{i,10});
            Data.Cell1.Exp8 = Data.Cell1.Exp8 * 1000;
        elseif i == 9
            Data.Cell1.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID9 = char(all.RecTable{i,10});
            Data.Cell1.Exp9 = Data.Cell1.Exp9 * 1000;
        elseif i == 10
            Data.Cell1.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID10 = char(all.RecTable{i,10});
            Data.Cell1.Exp10 = Data.Cell1.Exp10 * 1000;
        elseif i == 11
            Data.Cell1.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID11 = char(all.RecTable{i,10});
            Data.Cell1.Exp11 = Data.Cell1.Exp11 * 1000;
        elseif i == 12
            Data.Cell1.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID12 = char(all.RecTable{i,10});
            Data.Cell1.Exp12 = Data.Cell1.Exp12 * 1000;
        elseif i == 13
            Data.Cell1.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID13 = char(all.RecTable{i,10});
            Data.Cell1.Exp13 = Data.Cell1.Exp13 * 1000;
        elseif i == 14
            Data.Cell1.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID14 = char(all.RecTable{i,10});
            Data.Cell1.Exp14 = Data.Cell1.Exp14 * 1000;
        elseif i == 15
            Data.Cell1.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID15 = char(all.RecTable{i,10});
            Data.Cell1.Exp15 = Data.Cell1.Exp15 * 1000;
        end
    end
    for i = Data.Cell1.Expts:(Data.Cell1.Expts+ Data.Cell2.Expts)
        if i == Data.Cell1.Expts + 1
            Data.Cell2.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID1 = char(all.RecTable{i,10});
            Data.Cell2.Exp1 = Data.Cell2.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + 2
            Data.Cell2.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID2 = char(all.RecTable{i,10});
            Data.Cell2.Exp2 = Data.Cell2.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + 3
            Data.Cell2.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID3 = char(all.RecTable{i,10});
            Data.Cell2.Exp3 = Data.Cell2.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + 4
            Data.Cell2.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID4 = char(all.RecTable{i,10});
            Data.Cell2.Exp4 = Data.Cell2.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + 5
            Data.Cell2.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID5 = char(all.RecTable{i,10});
            Data.Cell2.Exp5 = Data.Cell2.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + 6
            Data.Cell2.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID6 = char(all.RecTable{i,10});
            Data.Cell2.Exp6 = Data.Cell2.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + 7
            Data.Cell2.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID7 = char(all.RecTable{i,10});
            Data.Cell2.Exp7 = Data.Cell2.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + 8
            Data.Cell2.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID8 = char(all.RecTable{i,10});
            Data.Cell2.Exp8 = Data.Cell2.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + 9
            Data.Cell2.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID9 = char(all.RecTable{i,10});
            Data.Cell2.Exp9 = Data.Cell2.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + 10
            Data.Cell2.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID10 = char(all.RecTable{i,10});
            Data.Cell2.Exp10 = Data.Cell2.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + 11
            Data.Cell2.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID11 = char(all.RecTable{i,10});
            Data.Cell2.Exp11 = Data.Cell2.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + 12
            Data.Cell2.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID12 = char(all.RecTable{i,10});
            Data.Cell2.Exp12 = Data.Cell2.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + 13
            Data.Cell2.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID13 = char(all.RecTable{i,10});
            Data.Cell2.Exp13 = Data.Cell2.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + 14
            Data.Cell2.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID14 = char(all.RecTable{i,10});
            Data.Cell2.Exp14 = Data.Cell2.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + 15
            Data.Cell2.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID15 = char(all.RecTable{i,10});
            Data.Cell2.Exp15 = Data.Cell2.Exp15 * 1000;
        end
    end
elseif Data.CellNum == 3
    for i = 1:Data.Cell1.Expts
        if i == 1
            Data.Cell1.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID1 = char(all.RecTable{i,10});
            Data.Cell1.Exp1 = Data.Cell1.Exp1 * 1000;
        elseif i == 2
            Data.Cell1.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID2 = char(all.RecTable{i,10});
            Data.Cell1.Exp2 = Data.Cell1.Exp2 * 1000;
        elseif i == 3
            Data.Cell1.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID3 = char(all.RecTable{i,10});
            Data.Cell1.Exp3 = Data.Cell1.Exp3 * 1000;
        elseif i == 4
            Data.Cell1.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID4 = char(all.RecTable{i,10});
            Data.Cell1.Exp4 = Data.Cell1.Exp4 * 1000;
        elseif i == 5
            Data.Cell1.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID5 = char(all.RecTable{i,10});
            Data.Cell1.Exp5 = Data.Cell1.Exp5 * 1000;
        elseif i == 6
            Data.Cell1.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID6 = char(all.RecTable{i,10});
            Data.Cell1.Exp6 = Data.Cell1.Exp6 * 1000;
        elseif i == 7
            Data.Cell1.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID7 = char(all.RecTable{i,10});
            Data.Cell1.Exp7 = Data.Cell1.Exp7 * 1000;
        elseif i == 8
            Data.Cell1.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID8 = char(all.RecTable{i,10});
            Data.Cell1.Exp8 = Data.Cell1.Exp8 * 1000;
        elseif i == 9
            Data.Cell1.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID9 = char(all.RecTable{i,10});
            Data.Cell1.Exp9 = Data.Cell1.Exp9 * 1000;
        elseif i == 10
            Data.Cell1.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID10 = char(all.RecTable{i,10});
            Data.Cell1.Exp10 = Data.Cell1.Exp10 * 1000;
        elseif i == 11
            Data.Cell1.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID11 = char(all.RecTable{i,10});
            Data.Cell1.Exp11 = Data.Cell1.Exp11 * 1000;
        elseif i == 12
            Data.Cell1.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID12 = char(all.RecTable{i,10});
            Data.Cell1.Exp12 = Data.Cell1.Exp12 * 1000;
        elseif i == 13
            Data.Cell1.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID13 = char(all.RecTable{i,10});
            Data.Cell1.Exp13 = Data.Cell1.Exp13 * 1000;
        elseif i == 14
            Data.Cell1.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID14 = char(all.RecTable{i,10});
            Data.Cell1.Exp14 = Data.Cell1.Exp14 * 1000;
        elseif i == 15
            Data.Cell1.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID15 = char(all.RecTable{i,10});
            Data.Cell1.Exp15 = Data.Cell1.Exp15 * 1000;
        end
    end
    for i = Data.Cell1.Expts:(Data.Cell1.Expts + Data.Cell2.Expts)
        if i == Data.Cell1.Expts + 1
            Data.Cell2.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID1 = char(all.RecTable{i,10});
            Data.Cell2.Exp1 = Data.Cell2.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + 2
            Data.Cell2.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID2 = char(all.RecTable{i,10});
            Data.Cell2.Exp2 = Data.Cell2.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + 3
            Data.Cell2.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID3 = char(all.RecTable{i,10});
            Data.Cell2.Exp3 = Data.Cell2.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + 4
            Data.Cell2.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID4 = char(all.RecTable{i,10});
            Data.Cell2.Exp4 = Data.Cell2.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + 5
            Data.Cell2.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID5 = char(all.RecTable{i,10});
            Data.Cell2.Exp5 = Data.Cell2.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + 6
            Data.Cell2.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID6 = char(all.RecTable{i,10});
            Data.Cell2.Exp6 = Data.Cell2.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + 7
            Data.Cell2.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID7 = char(all.RecTable{i,10});
            Data.Cell2.Exp7 = Data.Cell2.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + 8
            Data.Cell2.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID8 = char(all.RecTable{i,10});
            Data.Cell2.Exp8 = Data.Cell2.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + 9
            Data.Cell2.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID9 = char(all.RecTable{i,10});
            Data.Cell2.Exp9 = Data.Cell2.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + 10
            Data.Cell2.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID10 = char(all.RecTable{i,10});
            Data.Cell2.Exp10 = Data.Cell2.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + 11
            Data.Cell2.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID11 = char(all.RecTable{i,10});
            Data.Cell2.Exp11 = Data.Cell2.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + 12
            Data.Cell2.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID12 = char(all.RecTable{i,10});
            Data.Cell2.Exp12 = Data.Cell2.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + 13
            Data.Cell2.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID13 = char(all.RecTable{i,10});
            Data.Cell2.Exp13 = Data.Cell2.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + 14
            Data.Cell2.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID14 = char(all.RecTable{i,10});
            Data.Cell2.Exp14 = Data.Cell2.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + 15
            Data.Cell2.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID15 = char(all.RecTable{i,10});
            Data.Cell2.Exp15 = Data.Cell2.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + 1
            Data.Cell3.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID1 = char(all.RecTable{i,10});
            Data.Cell3.Exp1 = Data.Cell3.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 2
            Data.Cell3.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID2 = char(all.RecTable{i,10});
            Data.Cell3.Exp2 = Data.Cell3.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 3
            Data.Cell3.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID3 = char(all.RecTable{i,10});
            Data.Cell3.Exp3 = Data.Cell3.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 4
            Data.Cell3.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID4 = char(all.RecTable{i,10});
            Data.Cell3.Exp4 = Data.Cell3.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 5
            Data.Cell3.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID5 = char(all.RecTable{i,10});
            Data.Cell3.Exp5 = Data.Cell3.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 6
            Data.Cell3.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID6 = char(all.RecTable{i,10});
            Data.Cell3.Exp6 = Data.Cell3.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 7
            Data.Cell3.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID7 = char(all.RecTable{i,10});
            Data.Cell3.Exp7 = Data.Cell3.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 8
            Data.Cell3.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID8 = char(all.RecTable{i,10});
            Data.Cell3.Exp8 = Data.Cell3.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 9
            Data.Cell3.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID9 = char(all.RecTable{i,10});
            Data.Cell3.Exp9 = Data.Cell3.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 10
            Data.Cell3.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID10 = char(all.RecTable{i,10});
            Data.Cell3.Exp10 = Data.Cell3.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 11
            Data.Cell3.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID11 = char(all.RecTable{i,10});
            Data.Cell3.Exp11 = Data.Cell3.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 12
            Data.Cell3.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID12 = char(all.RecTable{i,10});
            Data.Cell3.Exp12 = Data.Cell3.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 13
            Data.Cell3.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID13 = char(all.RecTable{i,10});
            Data.Cell3.Exp13 = Data.Cell3.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 14
            Data.Cell3.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID14 = char(all.RecTable{i,10});
            Data.Cell3.Exp14 = Data.Cell3.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 15
            Data.Cell3.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID15 = char(all.RecTable{i,10});
            Data.Cell3.Exp15 = Data.Cell3.Exp15 * 1000;
        end
    end
elseif Data.CellNum == 4
    for i = 1:Data.Cell1.Expts
        if i == 1
            Data.Cell1.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID1 = char(all.RecTable{i,10});
            Data.Cell1.Exp1 = Data.Cell1.Exp1 * 1000;
        elseif i == 2
            Data.Cell1.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID2 = char(all.RecTable{i,10});
            Data.Cell1.Exp2 = Data.Cell1.Exp2 * 1000;
        elseif i == 3
            Data.Cell1.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID3 = char(all.RecTable{i,10});
            Data.Cell1.Exp3 = Data.Cell1.Exp3 * 1000;
        elseif i == 4
            Data.Cell1.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID4 = char(all.RecTable{i,10});
            Data.Cell1.Exp4 = Data.Cell1.Exp4 * 1000;
        elseif i == 5
            Data.Cell1.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID5 = char(all.RecTable{i,10});
            Data.Cell1.Exp5 = Data.Cell1.Exp5 * 1000;
        elseif i == 6
            Data.Cell1.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID6 = char(all.RecTable{i,10});
            Data.Cell1.Exp6 = Data.Cell1.Exp6 * 1000;
        elseif i == 7
            Data.Cell1.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID7 = char(all.RecTable{i,10});
            Data.Cell1.Exp7 = Data.Cell1.Exp7 * 1000;
        elseif i == 8
            Data.Cell1.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID8 = char(all.RecTable{i,10});
            Data.Cell1.Exp8 = Data.Cell1.Exp8 * 1000;
        elseif i == 9
            Data.Cell1.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID9 = char(all.RecTable{i,10});
            Data.Cell1.Exp9 = Data.Cell1.Exp9 * 1000;
        elseif i == 10
            Data.Cell1.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID10 = char(all.RecTable{i,10});
            Data.Cell1.Exp10 = Data.Cell1.Exp10 * 1000;
        elseif i == 11
            Data.Cell1.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID11 = char(all.RecTable{i,10});
            Data.Cell1.Exp11 = Data.Cell1.Exp11 * 1000;
        elseif i == 12
            Data.Cell1.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID12 = char(all.RecTable{i,10});
            Data.Cell1.Exp12 = Data.Cell1.Exp12 * 1000;
        elseif i == 13
            Data.Cell1.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID13 = char(all.RecTable{i,10});
            Data.Cell1.Exp13 = Data.Cell1.Exp13 * 1000;
        elseif i == 14
            Data.Cell1.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID14 = char(all.RecTable{i,10});
            Data.Cell1.Exp14 = Data.Cell1.Exp14 * 1000;
        elseif i == 15
            Data.Cell1.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID15 = char(all.RecTable{i,10});
            Data.Cell1.Exp15 = Data.Cell1.Exp15 * 1000;
        end
    end
    for i = Data.Cell1.Expts:(Data.Cell1.Expts + Data.Cell2.Expts)
        if i == Data.Cell1.Expts + 1
            Data.Cell2.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID1 = char(all.RecTable{i,10});
            Data.Cell2.Exp1 = Data.Cell2.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + 2
            Data.Cell2.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID2 = char(all.RecTable{i,10});
            Data.Cell2.Exp2 = Data.Cell2.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + 3
            Data.Cell2.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID3 = char(all.RecTable{i,10});
            Data.Cell2.Exp3 = Data.Cell2.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + 4
            Data.Cell2.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID4 = char(all.RecTable{i,10});
            Data.Cell2.Exp4 = Data.Cell2.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + 5
            Data.Cell2.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID5 = char(all.RecTable{i,10});
            Data.Cell2.Exp5 = Data.Cell2.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + 6
            Data.Cell2.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID6 = char(all.RecTable{i,10});
            Data.Cell2.Exp6 = Data.Cell2.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + 7
            Data.Cell2.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID7 = char(all.RecTable{i,10});
            Data.Cell2.Exp7 = Data.Cell2.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + 8
            Data.Cell2.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID8 = char(all.RecTable{i,10});
            Data.Cell2.Exp8 = Data.Cell2.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + 9
            Data.Cell2.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID9 = char(all.RecTable{i,10});
            Data.Cell2.Exp9 = Data.Cell2.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + 10
            Data.Cell2.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID10 = char(all.RecTable{i,10});
            Data.Cell2.Exp10 = Data.Cell2.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + 11
            Data.Cell2.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID11 = char(all.RecTable{i,10});
            Data.Cell2.Exp11 = Data.Cell2.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + 12
            Data.Cell2.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID12 = char(all.RecTable{i,10});
            Data.Cell2.Exp12 = Data.Cell2.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + 13
            Data.Cell2.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID13 = char(all.RecTable{i,10});
            Data.Cell2.Exp13 = Data.Cell2.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + 14
            Data.Cell2.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID14 = char(all.RecTable{i,10});
            Data.Cell2.Exp14 = Data.Cell2.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + 15
            Data.Cell2.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID15 = char(all.RecTable{i,10});
            Data.Cell2.Exp15 = Data.Cell2.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + 1
            Data.Cell3.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID1 = char(all.RecTable{i,10});
            Data.Cell3.Exp1 = Data.Cell3.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 2
            Data.Cell3.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID2 = char(all.RecTable{i,10});
            Data.Cell3.Exp2 = Data.Cell3.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 3
            Data.Cell3.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID3 = char(all.RecTable{i,10});
            Data.Cell3.Exp3 = Data.Cell3.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 4
            Data.Cell3.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID4 = char(all.RecTable{i,10});
            Data.Cell3.Exp4 = Data.Cell3.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 5
            Data.Cell3.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID5 = char(all.RecTable{i,10});
            Data.Cell3.Exp5 = Data.Cell3.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 6
            Data.Cell3.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID6 = char(all.RecTable{i,10});
            Data.Cell3.Exp6 = Data.Cell3.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 7
            Data.Cell3.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID7 = char(all.RecTable{i,10});
            Data.Cell3.Exp7 = Data.Cell3.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 8
            Data.Cell3.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID8 = char(all.RecTable{i,10});
            Data.Cell3.Exp8 = Data.Cell3.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 9
            Data.Cell3.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID9 = char(all.RecTable{i,10});
            Data.Cell3.Exp9 = Data.Cell3.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 10
            Data.Cell3.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID10 = char(all.RecTable{i,10});
            Data.Cell3.Exp10 = Data.Cell3.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 11
            Data.Cell3.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID11 = char(all.RecTable{i,10});
            Data.Cell3.Exp11 = Data.Cell3.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 12
            Data.Cell3.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID12 = char(all.RecTable{i,10});
            Data.Cell3.Exp12 = Data.Cell3.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 13
            Data.Cell3.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID13 = char(all.RecTable{i,10});
            Data.Cell3.Exp13 = Data.Cell3.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 14
            Data.Cell3.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID14 = char(all.RecTable{i,10});
            Data.Cell3.Exp14 = Data.Cell3.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 15
            Data.Cell3.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID15 = char(all.RecTable{i,10});
            Data.Cell3.Exp15 = Data.Cell3.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 1
            Data.Cell4.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID1 = char(all.RecTable{i,10});
            Data.Cell4.Exp1 = Data.Cell4.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 2
            Data.Cell4.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID2 = char(all.RecTable{i,10});
            Data.Cell4.Exp2 = Data.Cell4.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 3
            Data.Cell4.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID3 = char(all.RecTable{i,10});
            Data.Cell4.Exp3 = Data.Cell4.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 4
            Data.Cell4.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID4 = char(all.RecTable{i,10});
            Data.Cell4.Exp4 = Data.Cell4.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 5
            Data.Cell4.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID5 = char(all.RecTable{i,10});
            Data.Cell4.Exp5 = Data.Cell4.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 6
            Data.Cell4.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID6 = char(all.RecTable{i,10});
            Data.Cell4.Exp6 = Data.Cell4.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 7
            Data.Cell4.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID7 = char(all.RecTable{i,10});
            Data.Cell4.Exp7 = Data.Cell4.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 8
            Data.Cell4.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID8 = char(all.RecTable{i,10});
            Data.Cell4.Exp8 = Data.Cell4.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 9
            Data.Cell4.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID9 = char(all.RecTable{i,10});
            Data.Cell4.Exp9 = Data.Cell4.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 10
            Data.Cell4.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID10 = char(all.RecTable{i,10});
            Data.Cell4.Exp10 = Data.Cell4.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 11
            Data.Cell4.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID11 = char(all.RecTable{i,10});
            Data.Cell4.Exp11 = Data.Cell4.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 12
            Data.Cell4.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID12 = char(all.RecTable{i,10});
            Data.Cell4.Exp12 = Data.Cell4.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 13
            Data.Cell4.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID13 = char(all.RecTable{i,10});
            Data.Cell4.Exp13 = Data.Cell4.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 14
            Data.Cell4.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID14 = char(all.RecTable{i,10});
            Data.Cell4.Exp14 = Data.Cell4.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 15
            Data.Cell4.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID15 = char(all.RecTable{i,10});
            Data.Cell4.Exp15 = Data.Cell4.Exp15 * 1000;
        end
    end
elseif Data.CellNum == 5
    for i = 1:Data.Cell1.Expts
        if i == 1
            Data.Cell1.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID1 = char(all.RecTable{i,10});
            Data.Cell1.Exp1 = Data.Cell1.Exp1 * 1000;
        elseif i == 2
            Data.Cell1.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID2 = char(all.RecTable{i,10});
            Data.Cell1.Exp2 = Data.Cell1.Exp2 * 1000;
        elseif i == 3
            Data.Cell1.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID3 = char(all.RecTable{i,10});
            Data.Cell1.Exp3 = Data.Cell1.Exp3 * 1000;
        elseif i == 4
            Data.Cell1.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID4 = char(all.RecTable{i,10});
            Data.Cell1.Exp4 = Data.Cell1.Exp4 * 1000;
        elseif i == 5
            Data.Cell1.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID5 = char(all.RecTable{i,10});
            Data.Cell1.Exp5 = Data.Cell1.Exp5 * 1000;
        elseif i == 6
            Data.Cell1.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID6 = char(all.RecTable{i,10});
            Data.Cell1.Exp6 = Data.Cell1.Exp6 * 1000;
        elseif i == 7
            Data.Cell1.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID7 = char(all.RecTable{i,10});
            Data.Cell1.Exp7 = Data.Cell1.Exp7 * 1000;
        elseif i == 8
            Data.Cell1.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID8 = char(all.RecTable{i,10});
            Data.Cell1.Exp8 = Data.Cell1.Exp8 * 1000;
        elseif i == 9
            Data.Cell1.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID9 = char(all.RecTable{i,10});
            Data.Cell1.Exp9 = Data.Cell1.Exp9 * 1000;
        elseif i == 10
            Data.Cell1.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID10 = char(all.RecTable{i,10});
            Data.Cell1.Exp10 = Data.Cell1.Exp10 * 1000;
        elseif i == 11
            Data.Cell1.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID11 = char(all.RecTable{i,10});
            Data.Cell1.Exp11 = Data.Cell1.Exp11 * 1000;
        elseif i == 12
            Data.Cell1.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID12 = char(all.RecTable{i,10});
            Data.Cell1.Exp12 = Data.Cell1.Exp12 * 1000;
        elseif i == 13
            Data.Cell1.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID13 = char(all.RecTable{i,10});
            Data.Cell1.Exp13 = Data.Cell1.Exp13 * 1000;
        elseif i == 14
            Data.Cell1.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID14 = char(all.RecTable{i,10});
            Data.Cell1.Exp14 = Data.Cell1.Exp14 * 1000;
        elseif i == 15
            Data.Cell1.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID15 = char(all.RecTable{i,10});
            Data.Cell1.Exp15 = Data.Cell1.Exp15 * 1000;
        end
    end
    for i = Data.Cell1.Expts:(Data.Cell1.Expts + Data.Cell2.Expts)
        if i == Data.Cell1.Expts + 1
            Data.Cell2.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID1 = char(all.RecTable{i,10});
            Data.Cell2.Exp1 = Data.Cell2.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + 2
            Data.Cell2.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID2 = char(all.RecTable{i,10});
            Data.Cell2.Exp2 = Data.Cell2.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + 3
            Data.Cell2.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID3 = char(all.RecTable{i,10});
            Data.Cell2.Exp3 = Data.Cell2.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + 4
            Data.Cell2.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID4 = char(all.RecTable{i,10});
            Data.Cell2.Exp4 = Data.Cell2.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + 5
            Data.Cell2.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID5 = char(all.RecTable{i,10});
            Data.Cell2.Exp5 = Data.Cell2.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + 6
            Data.Cell2.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID6 = char(all.RecTable{i,10});
            Data.Cell2.Exp6 = Data.Cell2.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + 7
            Data.Cell2.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID7 = char(all.RecTable{i,10});
            Data.Cell2.Exp7 = Data.Cell2.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + 8
            Data.Cell2.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID8 = char(all.RecTable{i,10});
            Data.Cell2.Exp8 = Data.Cell2.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + 9
            Data.Cell2.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID9 = char(all.RecTable{i,10});
            Data.Cell2.Exp9 = Data.Cell2.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + 10
            Data.Cell2.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID10 = char(all.RecTable{i,10});
            Data.Cell2.Exp10 = Data.Cell2.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + 11
            Data.Cell2.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID11 = char(all.RecTable{i,10});
            Data.Cell2.Exp11 = Data.Cell2.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + 12
            Data.Cell2.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID12 = char(all.RecTable{i,10});
            Data.Cell2.Exp12 = Data.Cell2.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + 13
            Data.Cell2.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID13 = char(all.RecTable{i,10});
            Data.Cell2.Exp13 = Data.Cell2.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + 14
            Data.Cell2.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID14 = char(all.RecTable{i,10});
            Data.Cell2.Exp14 = Data.Cell2.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + 15
            Data.Cell2.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID15 = char(all.RecTable{i,10});
            Data.Cell2.Exp15 = Data.Cell2.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + 1
            Data.Cell3.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID1 = char(all.RecTable{i,10});
            Data.Cell3.Exp1 = Data.Cell3.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 2
            Data.Cell3.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID2 = char(all.RecTable{i,10});
            Data.Cell3.Exp2 = Data.Cell3.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 3
            Data.Cell3.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID3 = char(all.RecTable{i,10});
            Data.Cell3.Exp3 = Data.Cell3.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 4
            Data.Cell3.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID4 = char(all.RecTable{i,10});
            Data.Cell3.Exp4 = Data.Cell3.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 5
            Data.Cell3.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID5 = char(all.RecTable{i,10});
            Data.Cell3.Exp5 = Data.Cell3.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 6
            Data.Cell3.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID6 = char(all.RecTable{i,10});
            Data.Cell3.Exp6 = Data.Cell3.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 7
            Data.Cell3.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID7 = char(all.RecTable{i,10});
            Data.Cell3.Exp7 = Data.Cell3.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 8
            Data.Cell3.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID8 = char(all.RecTable{i,10});
            Data.Cell3.Exp8 = Data.Cell3.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 9
            Data.Cell3.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID9 = char(all.RecTable{i,10});
            Data.Cell3.Exp9 = Data.Cell3.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 10
            Data.Cell3.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID10 = char(all.RecTable{i,10});
            Data.Cell3.Exp10 = Data.Cell3.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 11
            Data.Cell3.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID11 = char(all.RecTable{i,10});
            Data.Cell3.Exp11 = Data.Cell3.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 12
            Data.Cell3.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID12 = char(all.RecTable{i,10});
            Data.Cell3.Exp12 = Data.Cell3.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 13
            Data.Cell3.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID13 = char(all.RecTable{i,10});
            Data.Cell3.Exp13 = Data.Cell3.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 14
            Data.Cell3.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID14 = char(all.RecTable{i,10});
            Data.Cell3.Exp14 = Data.Cell3.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 15
            Data.Cell3.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID15 = char(all.RecTable{i,10});
            Data.Cell3.Exp15 = Data.Cell3.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 1
            Data.Cell4.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID1 = char(all.RecTable{i,10});
            Data.Cell4.Exp1 = Data.Cell4.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 2
            Data.Cell4.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID2 = char(all.RecTable{i,10});
            Data.Cell4.Exp2 = Data.Cell4.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 3
            Data.Cell4.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID3 = char(all.RecTable{i,10});
            Data.Cell4.Exp3 = Data.Cell4.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 4
            Data.Cell4.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID4 = char(all.RecTable{i,10});
            Data.Cell4.Exp4 = Data.Cell4.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 5
            Data.Cell4.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID5 = char(all.RecTable{i,10});
            Data.Cell4.Exp5 = Data.Cell4.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 6
            Data.Cell4.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID6 = char(all.RecTable{i,10});
            Data.Cell4.Exp6 = Data.Cell4.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 7
            Data.Cell4.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID7 = char(all.RecTable{i,10});
            Data.Cell4.Exp7 = Data.Cell4.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 8
            Data.Cell4.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID8 = char(all.RecTable{i,10});
            Data.Cell4.Exp8 = Data.Cell4.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 9
            Data.Cell4.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID9 = char(all.RecTable{i,10});
            Data.Cell4.Exp9 = Data.Cell4.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 10
            Data.Cell4.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID10 = char(all.RecTable{i,10});
            Data.Cell4.Exp10 = Data.Cell4.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 11
            Data.Cell4.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID11 = char(all.RecTable{i,10});
            Data.Cell4.Exp11 = Data.Cell4.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 12
            Data.Cell4.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID12 = char(all.RecTable{i,10});
            Data.Cell4.Exp12 = Data.Cell4.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 13
            Data.Cell4.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID13 = char(all.RecTable{i,10});
            Data.Cell4.Exp13 = Data.Cell4.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 14
            Data.Cell4.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID14 = char(all.RecTable{i,10});
            Data.Cell4.Exp14 = Data.Cell4.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 15
            Data.Cell4.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID15 = char(all.RecTable{i,10});
            Data.Cell4.Exp15 = Data.Cell4.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 1
            Data.Cell5.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID1 = char(all.RecTable{i,10});
            Data.Cell5.Exp1 = Data.Cell5.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 2
            Data.Cell5.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID2 = char(all.RecTable{i,10});
            Data.Cell5.Exp2 = Data.Cell5.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 3
            Data.Cell5.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID3 = char(all.RecTable{i,10});
            Data.Cell5.Exp3 = Data.Cell5.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 4
            Data.Cell5.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID4 = char(all.RecTable{i,10});
            Data.Cell5.Exp4 = Data.Cell5.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 5
            Data.Cell5.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID5 = char(all.RecTable{i,10});
            Data.Cell5.Exp5 = Data.Cell5.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 6
            Data.Cell5.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID6 = char(all.RecTable{i,10});
            Data.Cell5.Exp6 = Data.Cell5.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 7
            Data.Cell5.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID7 = char(all.RecTable{i,10});
            Data.Cell5.Exp7 = Data.Cell5.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 8
            Data.Cell5.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID8 = char(all.RecTable{i,10});
            Data.Cell5.Exp8 = Data.Cell5.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 9
            Data.Cell5.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID9 = char(all.RecTable{i,10});
            Data.Cell5.Exp9 = Data.Cell5.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 10
            Data.Cell5.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID10 = char(all.RecTable{i,10});
            Data.Cell5.Exp10 = Data.Cell5.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 11
            Data.Cell5.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID11 = char(all.RecTable{i,10});
            Data.Cell5.Exp11 = Data.Cell5.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 12
            Data.Cell5.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID12 = char(all.RecTable{i,10});
            Data.Cell5.Exp12 = Data.Cell5.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 13
            Data.Cell5.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID13 = char(all.RecTable{i,10});
            Data.Cell5.Exp13 = Data.Cell5.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 14
            Data.Cell5.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID14 = char(all.RecTable{i,10});
            Data.Cell5.Exp14 = Data.Cell5.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts +  15
            Data.Cell5.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID15 = char(all.RecTable{i,10});
            Data.Cell5.Exp15 = Data.Cell5.Exp15 * 1000;
        end
    end
elseif Data.CellNum == 6
    for i = 1:Data.Cell1.Expts
        if i == 1
            Data.Cell1.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID1 = char(all.RecTable{i,10});
            Data.Cell1.Exp1 = Data.Cell1.Exp1 * 1000;
        elseif i == 2
            Data.Cell1.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID2 = char(all.RecTable{i,10});
            Data.Cell1.Exp2 = Data.Cell1.Exp2 * 1000;
        elseif i == 3
            Data.Cell1.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID3 = char(all.RecTable{i,10});
            Data.Cell1.Exp3 = Data.Cell1.Exp3 * 1000;
        elseif i == 4
            Data.Cell1.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID4 = char(all.RecTable{i,10});
            Data.Cell1.Exp4 = Data.Cell1.Exp4 * 1000;
        elseif i == 5
            Data.Cell1.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID5 = char(all.RecTable{i,10});
            Data.Cell1.Exp5 = Data.Cell1.Exp5 * 1000;
        elseif i == 6
            Data.Cell1.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID6 = char(all.RecTable{i,10});
            Data.Cell1.Exp6 = Data.Cell1.Exp6 * 1000;
        elseif i == 7
            Data.Cell1.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID7 = char(all.RecTable{i,10});
            Data.Cell1.Exp7 = Data.Cell1.Exp7 * 1000;
        elseif i == 8
            Data.Cell1.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID8 = char(all.RecTable{i,10});
            Data.Cell1.Exp8 = Data.Cell1.Exp8 * 1000;
        elseif i == 9
            Data.Cell1.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID9 = char(all.RecTable{i,10});
            Data.Cell1.Exp9 = Data.Cell1.Exp9 * 1000;
        elseif i == 10
            Data.Cell1.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID10 = char(all.RecTable{i,10});
            Data.Cell1.Exp10 = Data.Cell1.Exp10 * 1000;
        elseif i == 11
            Data.Cell1.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID11 = char(all.RecTable{i,10});
            Data.Cell1.Exp11 = Data.Cell1.Exp11 * 1000;
        elseif i == 12
            Data.Cell1.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID12 = char(all.RecTable{i,10});
            Data.Cell1.Exp12 = Data.Cell1.Exp12 * 1000;
        elseif i == 13
            Data.Cell1.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID13 = char(all.RecTable{i,10});
            Data.Cell1.Exp13 = Data.Cell1.Exp13 * 1000;
        elseif i == 14
            Data.Cell1.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID14 = char(all.RecTable{i,10});
            Data.Cell1.Exp14 = Data.Cell1.Exp14 * 1000;
        elseif i == 15
            Data.Cell1.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID15 = char(all.RecTable{i,10});
            Data.Cell1.Exp15 = Data.Cell1.Exp15 * 1000;
        end
    end
    for i = Data.Cell1.Expts:(Data.Cell1.Expts + Data.Cell2.Expts)
        if i == Data.Cell1.Expts + 1
            Data.Cell2.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID1 = char(all.RecTable{i,10});
            Data.Cell2.Exp1 = Data.Cell2.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + 2
            Data.Cell2.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID2 = char(all.RecTable{i,10});
            Data.Cell2.Exp2 = Data.Cell2.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + 3
            Data.Cell2.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID3 = char(all.RecTable{i,10});
            Data.Cell2.Exp3 = Data.Cell2.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + 4
            Data.Cell2.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID4 = char(all.RecTable{i,10});
            Data.Cell2.Exp4 = Data.Cell2.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + 5
            Data.Cell2.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID5 = char(all.RecTable{i,10});
            Data.Cell2.Exp5 = Data.Cell2.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + 6
            Data.Cell2.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID6 = char(all.RecTable{i,10});
            Data.Cell2.Exp6 = Data.Cell2.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + 7
            Data.Cell2.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID7 = char(all.RecTable{i,10});
            Data.Cell2.Exp7 = Data.Cell2.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + 8
            Data.Cell2.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID8 = char(all.RecTable{i,10});
            Data.Cell2.Exp8 = Data.Cell2.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + 9
            Data.Cell2.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID9 = char(all.RecTable{i,10});
            Data.Cell2.Exp9 = Data.Cell2.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + 10
            Data.Cell2.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID10 = char(all.RecTable{i,10});
            Data.Cell2.Exp10 = Data.Cell2.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + 11
            Data.Cell2.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID11 = char(all.RecTable{i,10});
            Data.Cell2.Exp11 = Data.Cell2.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + 12
            Data.Cell2.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID12 = char(all.RecTable{i,10});
            Data.Cell2.Exp12 = Data.Cell2.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + 13
            Data.Cell2.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID13 = char(all.RecTable{i,10});
            Data.Cell2.Exp13 = Data.Cell2.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + 14
            Data.Cell2.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID14 = char(all.RecTable{i,10});
            Data.Cell2.Exp14 = Data.Cell2.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + 15
            Data.Cell2.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID15 = char(all.RecTable{i,10});
            Data.Cell2.Exp15 = Data.Cell2.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + 1
            Data.Cell3.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID1 = char(all.RecTable{i,10});
            Data.Cell3.Exp1 = Data.Cell3.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 2
            Data.Cell3.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID2 = char(all.RecTable{i,10});
            Data.Cell3.Exp2 = Data.Cell3.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 3
            Data.Cell3.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID3 = char(all.RecTable{i,10});
            Data.Cell3.Exp3 = Data.Cell3.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 4
            Data.Cell3.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID4 = char(all.RecTable{i,10});
            Data.Cell3.Exp4 = Data.Cell3.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 5
            Data.Cell3.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID5 = char(all.RecTable{i,10});
            Data.Cell3.Exp5 = Data.Cell3.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 6
            Data.Cell3.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID6 = char(all.RecTable{i,10});
            Data.Cell3.Exp6 = Data.Cell3.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 7
            Data.Cell3.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID7 = char(all.RecTable{i,10});
            Data.Cell3.Exp7 = Data.Cell3.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 8
            Data.Cell3.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID8 = char(all.RecTable{i,10});
            Data.Cell3.Exp8 = Data.Cell3.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 9
            Data.Cell3.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID9 = char(all.RecTable{i,10});
            Data.Cell3.Exp9 = Data.Cell3.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 10
            Data.Cell3.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID10 = char(all.RecTable{i,10});
            Data.Cell3.Exp10 = Data.Cell3.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 11
            Data.Cell3.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID11 = char(all.RecTable{i,10});
            Data.Cell3.Exp11 = Data.Cell3.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 12
            Data.Cell3.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID12 = char(all.RecTable{i,10});
            Data.Cell3.Exp12 = Data.Cell3.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 13
            Data.Cell3.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID13 = char(all.RecTable{i,10});
            Data.Cell3.Exp13 = Data.Cell3.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 14
            Data.Cell3.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID14 = char(all.RecTable{i,10});
            Data.Cell3.Exp14 = Data.Cell3.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 15
            Data.Cell3.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID15 = char(all.RecTable{i,10});
            Data.Cell3.Exp15 = Data.Cell3.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 1
            Data.Cell4.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID1 = char(all.RecTable{i,10});
            Data.Cell4.Exp1 = Data.Cell4.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 2
            Data.Cell4.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID2 = char(all.RecTable{i,10});
            Data.Cell4.Exp2 = Data.Cell4.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 3
            Data.Cell4.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID3 = char(all.RecTable{i,10});
            Data.Cell4.Exp3 = Data.Cell4.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 4
            Data.Cell4.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID4 = char(all.RecTable{i,10});
            Data.Cell4.Exp4 = Data.Cell4.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 5
            Data.Cell4.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID5 = char(all.RecTable{i,10});
            Data.Cell4.Exp5 = Data.Cell4.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 6
            Data.Cell4.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID6 = char(all.RecTable{i,10});
            Data.Cell4.Exp6 = Data.Cell4.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 7
            Data.Cell4.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID7 = char(all.RecTable{i,10});
            Data.Cell4.Exp7 = Data.Cell4.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 8
            Data.Cell4.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID8 = char(all.RecTable{i,10});
            Data.Cell4.Exp8 = Data.Cell4.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 9
            Data.Cell4.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID9 = char(all.RecTable{i,10});
            Data.Cell4.Exp9 = Data.Cell4.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 10
            Data.Cell4.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID10 = char(all.RecTable{i,10});
            Data.Cell4.Exp10 = Data.Cell4.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 11
            Data.Cell4.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID11 = char(all.RecTable{i,10});
            Data.Cell4.Exp11 = Data.Cell4.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 12
            Data.Cell4.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID12 = char(all.RecTable{i,10});
            Data.Cell4.Exp12 = Data.Cell4.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 13
            Data.Cell4.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID13 = char(all.RecTable{i,10});
            Data.Cell4.Exp13 = Data.Cell4.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 14
            Data.Cell4.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID14 = char(all.RecTable{i,10});
            Data.Cell4.Exp14 = Data.Cell4.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 15
            Data.Cell4.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID15 = char(all.RecTable{i,10});
            Data.Cell4.Exp15 = Data.Cell4.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 1
            Data.Cell5.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID1 = char(all.RecTable{i,10});
            Data.Cell5.Exp1 = Data.Cell5.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 2
            Data.Cell5.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID2 = char(all.RecTable{i,10});
            Data.Cell5.Exp2 = Data.Cell5.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 3
            Data.Cell5.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID3 = char(all.RecTable{i,10});
            Data.Cell5.Exp3 = Data.Cell5.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 4
            Data.Cell5.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID4 = char(all.RecTable{i,10});
            Data.Cell5.Exp4 = Data.Cell5.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 5
            Data.Cell5.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID5 = char(all.RecTable{i,10});
            Data.Cell5.Exp5 = Data.Cell5.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 6
            Data.Cell5.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID6 = char(all.RecTable{i,10});
            Data.Cell5.Exp6 = Data.Cell5.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 7
            Data.Cell5.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID7 = char(all.RecTable{i,10});
            Data.Cell5.Exp7 = Data.Cell5.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 8
            Data.Cell5.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID8 = char(all.RecTable{i,10});
            Data.Cell5.Exp8 = Data.Cell5.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 9
            Data.Cell5.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID9 = char(all.RecTable{i,10});
            Data.Cell5.Exp9 = Data.Cell5.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 10
            Data.Cell5.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID10 = char(all.RecTable{i,10});
            Data.Cell5.Exp10 = Data.Cell5.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 11
            Data.Cell5.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID11 = char(all.RecTable{i,10});
            Data.Cell5.Exp11 = Data.Cell5.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 12
            Data.Cell5.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID12 = char(all.RecTable{i,10});
            Data.Cell5.Exp12 = Data.Cell5.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 13
            Data.Cell5.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID13 = char(all.RecTable{i,10});
            Data.Cell5.Exp13 = Data.Cell5.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 14
            Data.Cell5.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID14 = char(all.RecTable{i,10});
            Data.Cell5.Exp14 = Data.Cell5.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts +  15
            Data.Cell5.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID15 = char(all.RecTable{i,10});
            Data.Cell5.Exp15 = Data.Cell5.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 1
            Data.Cell6.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID1 = char(all.RecTable{i,10});
            Data.Cell6.Exp1 = Data.Cell6.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 2
            Data.Cell6.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID2 = char(all.RecTable{i,10});
            Data.Cell6.Exp2 = Data.Cell6.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 3
            Data.Cell6.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID3 = char(all.RecTable{i,10});
            Data.Cell6.Exp3 = Data.Cell6.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 4
            Data.Cell6.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID4 = char(all.RecTable{i,10});
            Data.Cell6.Exp4 = Data.Cell6.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 5
            Data.Cell6.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID5 = char(all.RecTable{i,10});
            Data.Cell6.Exp5 = Data.Cell6.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 6
            Data.Cell6.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID6 = char(all.RecTable{i,10});
            Data.Cell6.Exp6 = Data.Cell6.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 7
            Data.Cell6.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID7 = char(all.RecTable{i,10});
            Data.Cell6.Exp7 = Data.Cell6.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 8
            Data.Cell6.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID8 = char(all.RecTable{i,10});
            Data.Cell6.Exp8 = Data.Cell6.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 9
            Data.Cell6.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID9 = char(all.RecTable{i,10});
            Data.Cell6.Exp9 = Data.Cell6.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 10
            Data.Cell6.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID10 = char(all.RecTable{i,10});
            Data.Cell6.Exp10 = Data.Cell6.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 11
            Data.Cell6.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID11 = char(all.RecTable{i,10});
            Data.Cell6.Exp11 = Data.Cell6.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 12
            Data.Cell6.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID12 = char(all.RecTable{i,10});
            Data.Cell6.Exp12 = Data.Cell6.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 13
            Data.Cell6.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID13 = char(all.RecTable{i,10});
            Data.Cell6.Exp13 = Data.Cell6.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 14
            Data.Cell6.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID14 = char(all.RecTable{i,10});
            Data.Cell6.Exp14 = Data.Cell6.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 15
            Data.Cell6.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID15 = char(all.RecTable{i,10});
            Data.Cell6.Exp15 = Data.Cell6.Exp15 * 1000;
        end
    end
elseif Data.CellNum == 7
    for i = 1:Data.Cell1.Expts
        if i == 1
            Data.Cell1.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID1 = char(all.RecTable{i,10});
            Data.Cell1.Exp1 = Data.Cell1.Exp1 * 1000;
        elseif i == 2
            Data.Cell1.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID2 = char(all.RecTable{i,10});
            Data.Cell1.Exp2 = Data.Cell1.Exp2 * 1000;
        elseif i == 3
            Data.Cell1.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID3 = char(all.RecTable{i,10});
            Data.Cell1.Exp3 = Data.Cell1.Exp3 * 1000;
        elseif i == 4
            Data.Cell1.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID4 = char(all.RecTable{i,10});
            Data.Cell1.Exp4 = Data.Cell1.Exp4 * 1000;
        elseif i == 5
            Data.Cell1.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID5 = char(all.RecTable{i,10});
            Data.Cell1.Exp5 = Data.Cell1.Exp5 * 1000;
        elseif i == 6
            Data.Cell1.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID6 = char(all.RecTable{i,10});
            Data.Cell1.Exp6 = Data.Cell1.Exp6 * 1000;
        elseif i == 7
            Data.Cell1.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID7 = char(all.RecTable{i,10});
            Data.Cell1.Exp7 = Data.Cell1.Exp7 * 1000;
        elseif i == 8
            Data.Cell1.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID8 = char(all.RecTable{i,10});
            Data.Cell1.Exp8 = Data.Cell1.Exp8 * 1000;
        elseif i == 9
            Data.Cell1.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID9 = char(all.RecTable{i,10});
            Data.Cell1.Exp9 = Data.Cell1.Exp9 * 1000;
        elseif i == 10
            Data.Cell1.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID10 = char(all.RecTable{i,10});
            Data.Cell1.Exp10 = Data.Cell1.Exp10 * 1000;
        elseif i == 11
            Data.Cell1.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID11 = char(all.RecTable{i,10});
            Data.Cell1.Exp11 = Data.Cell1.Exp11 * 1000;
        elseif i == 12
            Data.Cell1.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID12 = char(all.RecTable{i,10});
            Data.Cell1.Exp12 = Data.Cell1.Exp12 * 1000;
        elseif i == 13
            Data.Cell1.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID13 = char(all.RecTable{i,10});
            Data.Cell1.Exp13 = Data.Cell1.Exp13 * 1000;
        elseif i == 14
            Data.Cell1.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID14 = char(all.RecTable{i,10});
            Data.Cell1.Exp14 = Data.Cell1.Exp14 * 1000;
        elseif i == 15
            Data.Cell1.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID15 = char(all.RecTable{i,10});
            Data.Cell1.Exp15 = Data.Cell1.Exp15 * 1000;
        end
end
    for i = Data.Cell1.Expts:(Data.Cell1.Expts + Data.Cell2.Expts)
        if i == Data.Cell1.Expts + 1
            Data.Cell2.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID1 = char(all.RecTable{i,10});
            Data.Cell2.Exp1 = Data.Cell2.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + 2
            Data.Cell2.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID2 = char(all.RecTable{i,10});
            Data.Cell2.Exp2 = Data.Cell2.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + 3
            Data.Cell2.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID3 = char(all.RecTable{i,10});
            Data.Cell2.Exp3 = Data.Cell2.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + 4
            Data.Cell2.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID4 = char(all.RecTable{i,10});
            Data.Cell2.Exp4 = Data.Cell2.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + 5
            Data.Cell2.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID5 = char(all.RecTable{i,10});
            Data.Cell2.Exp5 = Data.Cell2.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + 6
            Data.Cell2.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID6 = char(all.RecTable{i,10});
            Data.Cell2.Exp6 = Data.Cell2.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + 7
            Data.Cell2.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID7 = char(all.RecTable{i,10});
            Data.Cell2.Exp7 = Data.Cell2.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + 8
            Data.Cell2.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID8 = char(all.RecTable{i,10});
            Data.Cell2.Exp8 = Data.Cell2.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + 9
            Data.Cell2.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID9 = char(all.RecTable{i,10});
            Data.Cell2.Exp9 = Data.Cell2.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + 10
            Data.Cell2.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID10 = char(all.RecTable{i,10});
            Data.Cell2.Exp10 = Data.Cell2.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + 11
            Data.Cell2.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID11 = char(all.RecTable{i,10});
            Data.Cell2.Exp11 = Data.Cell2.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + 12
            Data.Cell2.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID12 = char(all.RecTable{i,10});
            Data.Cell2.Exp12 = Data.Cell2.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + 13
            Data.Cell2.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID13 = char(all.RecTable{i,10});
            Data.Cell2.Exp13 = Data.Cell2.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + 14
            Data.Cell2.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID14 = char(all.RecTable{i,10});
            Data.Cell2.Exp14 = Data.Cell2.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + 15
            Data.Cell2.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID15 = char(all.RecTable{i,10});
            Data.Cell2.Exp15 = Data.Cell2.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + 1
            Data.Cell3.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID1 = char(all.RecTable{i,10});
            Data.Cell3.Exp1 = Data.Cell3.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 2
            Data.Cell3.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID2 = char(all.RecTable{i,10});
            Data.Cell3.Exp2 = Data.Cell3.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 3
            Data.Cell3.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID3 = char(all.RecTable{i,10});
            Data.Cell3.Exp3 = Data.Cell3.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 4
            Data.Cell3.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID4 = char(all.RecTable{i,10});
            Data.Cell3.Exp4 = Data.Cell3.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 5
            Data.Cell3.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID5 = char(all.RecTable{i,10});
            Data.Cell3.Exp5 = Data.Cell3.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 6
            Data.Cell3.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID6 = char(all.RecTable{i,10});
            Data.Cell3.Exp6 = Data.Cell3.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 7
            Data.Cell3.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID7 = char(all.RecTable{i,10});
            Data.Cell3.Exp7 = Data.Cell3.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 8
            Data.Cell3.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID8 = char(all.RecTable{i,10});
            Data.Cell3.Exp8 = Data.Cell3.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 9
            Data.Cell3.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID9 = char(all.RecTable{i,10});
            Data.Cell3.Exp9 = Data.Cell3.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 10
            Data.Cell3.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID10 = char(all.RecTable{i,10});
            Data.Cell3.Exp10 = Data.Cell3.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 11
            Data.Cell3.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID11 = char(all.RecTable{i,10});
            Data.Cell3.Exp11 = Data.Cell3.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 12
            Data.Cell3.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID12 = char(all.RecTable{i,10});
            Data.Cell3.Exp12 = Data.Cell3.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 13
            Data.Cell3.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID13 = char(all.RecTable{i,10});
            Data.Cell3.Exp13 = Data.Cell3.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 14
            Data.Cell3.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID14 = char(all.RecTable{i,10});
            Data.Cell3.Exp14 = Data.Cell3.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 15
            Data.Cell3.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID15 = char(all.RecTable{i,10});
            Data.Cell3.Exp15 = Data.Cell3.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 1
            Data.Cell4.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID1 = char(all.RecTable{i,10});
            Data.Cell4.Exp1 = Data.Cell4.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 2
            Data.Cell4.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID2 = char(all.RecTable{i,10});
            Data.Cell4.Exp2 = Data.Cell4.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 3
            Data.Cell4.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID3 = char(all.RecTable{i,10});
            Data.Cell4.Exp3 = Data.Cell4.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 4
            Data.Cell4.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID4 = char(all.RecTable{i,10});
            Data.Cell4.Exp4 = Data.Cell4.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 5
            Data.Cell4.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID5 = char(all.RecTable{i,10});
            Data.Cell4.Exp5 = Data.Cell4.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 6
            Data.Cell4.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID6 = char(all.RecTable{i,10});
            Data.Cell4.Exp6 = Data.Cell4.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 7
            Data.Cell4.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID7 = char(all.RecTable{i,10});
            Data.Cell4.Exp7 = Data.Cell4.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 8
            Data.Cell4.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID8 = char(all.RecTable{i,10});
            Data.Cell4.Exp8 = Data.Cell4.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 9
            Data.Cell4.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID9 = char(all.RecTable{i,10});
            Data.Cell4.Exp9 = Data.Cell4.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 10
            Data.Cell4.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID10 = char(all.RecTable{i,10});
            Data.Cell4.Exp10 = Data.Cell4.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 11
            Data.Cell4.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID11 = char(all.RecTable{i,10});
            Data.Cell4.Exp11 = Data.Cell4.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 12
            Data.Cell4.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID12 = char(all.RecTable{i,10});
            Data.Cell4.Exp12 = Data.Cell4.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 13
            Data.Cell4.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID13 = char(all.RecTable{i,10});
            Data.Cell4.Exp13 = Data.Cell4.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 14
            Data.Cell4.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID14 = char(all.RecTable{i,10});
            Data.Cell4.Exp14 = Data.Cell4.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 15
            Data.Cell4.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID15 = char(all.RecTable{i,10});
            Data.Cell4.Exp15 = Data.Cell4.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 1
            Data.Cell5.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID1 = char(all.RecTable{i,10});
            Data.Cell5.Exp1 = Data.Cell5.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 2
            Data.Cell5.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID2 = char(all.RecTable{i,10});
            Data.Cell5.Exp2 = Data.Cell5.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 3
            Data.Cell5.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID3 = char(all.RecTable{i,10});
            Data.Cell5.Exp3 = Data.Cell5.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 4
            Data.Cell5.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID4 = char(all.RecTable{i,10});
            Data.Cell5.Exp4 = Data.Cell5.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 5
            Data.Cell5.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID5 = char(all.RecTable{i,10});
            Data.Cell5.Exp5 = Data.Cell5.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 6
            Data.Cell5.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID6 = char(all.RecTable{i,10});
            Data.Cell5.Exp6 = Data.Cell5.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 7
            Data.Cell5.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID7 = char(all.RecTable{i,10});
            Data.Cell5.Exp7 = Data.Cell5.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 8
            Data.Cell5.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID8 = char(all.RecTable{i,10});
            Data.Cell5.Exp8 = Data.Cell5.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 9
            Data.Cell5.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID9 = char(all.RecTable{i,10});
            Data.Cell5.Exp9 = Data.Cell5.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 10
            Data.Cell5.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID10 = char(all.RecTable{i,10});
            Data.Cell5.Exp10 = Data.Cell5.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 11
            Data.Cell5.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID11 = char(all.RecTable{i,10});
            Data.Cell5.Exp11 = Data.Cell5.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 12
            Data.Cell5.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID12 = char(all.RecTable{i,10});
            Data.Cell5.Exp12 = Data.Cell5.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 13
            Data.Cell5.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID13 = char(all.RecTable{i,10});
            Data.Cell5.Exp13 = Data.Cell5.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 14
            Data.Cell5.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID14 = char(all.RecTable{i,10});
            Data.Cell5.Exp14 = Data.Cell5.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts +  15
            Data.Cell5.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID15 = char(all.RecTable{i,10});
            Data.Cell5.Exp15 = Data.Cell5.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 1
            Data.Cell6.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID1 = char(all.RecTable{i,10});
            Data.Cell6.Exp1 = Data.Cell6.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 2
            Data.Cell6.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID2 = char(all.RecTable{i,10});
            Data.Cell6.Exp2 = Data.Cell6.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 3
            Data.Cell6.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID3 = char(all.RecTable{i,10});
            Data.Cell6.Exp3 = Data.Cell6.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 4
            Data.Cell6.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID4 = char(all.RecTable{i,10});
            Data.Cell6.Exp4 = Data.Cell6.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 5
            Data.Cell6.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID5 = char(all.RecTable{i,10});
            Data.Cell6.Exp5 = Data.Cell6.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 6
            Data.Cell6.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID6 = char(all.RecTable{i,10});
            Data.Cell6.Exp6 = Data.Cell6.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 7
            Data.Cell6.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID7 = char(all.RecTable{i,10});
            Data.Cell6.Exp7 = Data.Cell6.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 8
            Data.Cell6.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID8 = char(all.RecTable{i,10});
            Data.Cell6.Exp8 = Data.Cell6.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 9
            Data.Cell6.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID9 = char(all.RecTable{i,10});
            Data.Cell6.Exp9 = Data.Cell6.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 10
            Data.Cell6.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID10 = char(all.RecTable{i,10});
            Data.Cell6.Exp10 = Data.Cell6.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 11
            Data.Cell6.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID11 = char(all.RecTable{i,10});
            Data.Cell6.Exp11 = Data.Cell6.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 12
            Data.Cell6.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID12 = char(all.RecTable{i,10});
            Data.Cell6.Exp12 = Data.Cell6.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 13
            Data.Cell6.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID13 = char(all.RecTable{i,10});
            Data.Cell6.Exp13 = Data.Cell6.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 14
            Data.Cell6.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID14 = char(all.RecTable{i,10});
            Data.Cell6.Exp14 = Data.Cell6.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 15
            Data.Cell6.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID15 = char(all.RecTable{i,10});
            Data.Cell6.Exp15 = Data.Cell6.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 1
            Data.Cell7.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID1 = char(all.RecTable{i,10});
            Data.Cell7.Exp1 = Data.Cell7.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 2
            Data.Cell7.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID2 = char(all.RecTable{i,10});
            Data.Cell7.Exp2 = Data.Cell7.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 3
            Data.Cell7.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID3 = char(all.RecTable{i,10});
            Data.Cell7.Exp3 = Data.Cell7.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 4
            Data.Cell7.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID4 = char(all.RecTable{i,10});
            Data.Cell7.Exp4 = Data.Cell7.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 5
            Data.Cell7.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID5 = char(all.RecTable{i,10});
            Data.Cell7.Exp5 = Data.Cell7.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 6
            Data.Cell7.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID6 = char(all.RecTable{i,10});
            Data.Cell7.Exp6 = Data.Cell7.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 7
            Data.Cell7.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID7 = char(all.RecTable{i,10});
            Data.Cell7.Exp7 = Data.Cell7.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 8
            Data.Cell7.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID8 = char(all.RecTable{i,10});
            Data.Cell7.Exp8 = Data.Cell7.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 9
            Data.Cell7.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID9 = char(all.RecTable{i,10});
            Data.Cell7.Exp9 = Data.Cell7.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 10
            Data.Cell7.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID10 = char(all.RecTable{i,10});
            Data.Cell7.Exp10 = Data.Cell7.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 11
            Data.Cell7.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID11 = char(all.RecTable{i,10});
            Data.Cell7.Exp11 = Data.Cell7.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 12
            Data.Cell7.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID12 = char(all.RecTable{i,10});
            Data.Cell7.Exp12 = Data.Cell7.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 13
            Data.Cell7.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID13 = char(all.RecTable{i,10});
            Data.Cell7.Exp13 = Data.Cell7.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 14
            Data.Cell7.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID14 = char(all.RecTable{i,10});
            Data.Cell7.Exp14 = Data.Cell7.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 15
            Data.Cell7.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID15 = char(all.RecTable{i,10});
            Data.Cell7.Exp15 = Data.Cell7.Exp15 * 1000;
        end
    end
elseif Data.CellNum == 8
    for i = 1:Data.Cell1.Expts
        if i == 1
            Data.Cell1.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID1 = char(all.RecTable{i,10});
            Data.Cell1.Exp1 = Data.Cell1.Exp1 * 1000;
        elseif i == 2
            Data.Cell1.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID2 = char(all.RecTable{i,10});
            Data.Cell1.Exp2 = Data.Cell1.Exp2 * 1000;
        elseif i == 3
            Data.Cell1.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID3 = char(all.RecTable{i,10});
            Data.Cell1.Exp3 = Data.Cell1.Exp3 * 1000;
        elseif i == 4
            Data.Cell1.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID4 = char(all.RecTable{i,10});
            Data.Cell1.Exp4 = Data.Cell1.Exp4 * 1000;
        elseif i == 5
            Data.Cell1.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID5 = char(all.RecTable{i,10});
            Data.Cell1.Exp5 = Data.Cell1.Exp5 * 1000;
        elseif i == 6
            Data.Cell1.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID6 = char(all.RecTable{i,10});
            Data.Cell1.Exp6 = Data.Cell1.Exp6 * 1000;
        elseif i == 7
            Data.Cell1.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID7 = char(all.RecTable{i,10});
            Data.Cell1.Exp7 = Data.Cell1.Exp7 * 1000;
        elseif i == 8
            Data.Cell1.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID8 = char(all.RecTable{i,10});
            Data.Cell1.Exp8 = Data.Cell1.Exp8 * 1000;
        elseif i == 9
            Data.Cell1.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID9 = char(all.RecTable{i,10});
            Data.Cell1.Exp9 = Data.Cell1.Exp9 * 1000;
        elseif i == 10
            Data.Cell1.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID10 = char(all.RecTable{i,10});
            Data.Cell1.Exp10 = Data.Cell1.Exp10 * 1000;
        elseif i == 11
            Data.Cell1.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID11 = char(all.RecTable{i,10});
            Data.Cell1.Exp11 = Data.Cell1.Exp11 * 1000;
        elseif i == 12
            Data.Cell1.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID12 = char(all.RecTable{i,10});
            Data.Cell1.Exp12 = Data.Cell1.Exp12 * 1000;
        elseif i == 13
            Data.Cell1.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID13 = char(all.RecTable{i,10});
            Data.Cell1.Exp13 = Data.Cell1.Exp13 * 1000;
        elseif i == 14
            Data.Cell1.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID14 = char(all.RecTable{i,10});
            Data.Cell1.Exp14 = Data.Cell1.Exp14 * 1000;
        elseif i == 15
            Data.Cell1.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID15 = char(all.RecTable{i,10});
            Data.Cell1.Exp15 = Data.Cell1.Exp15 * 1000;
        end
    end
    for i = Data.Cell1.Expts:(Data.Cell1.Expts + Data.Cell2.Expts)
        if i == Data.Cell1.Expts + 1
            Data.Cell2.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID1 = char(all.RecTable{i,10});
            Data.Cell2.Exp1 = Data.Cell2.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + 2
            Data.Cell2.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID2 = char(all.RecTable{i,10});
            Data.Cell2.Exp2 = Data.Cell2.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + 3
            Data.Cell2.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID3 = char(all.RecTable{i,10});
            Data.Cell2.Exp3 = Data.Cell2.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + 4
            Data.Cell2.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID4 = char(all.RecTable{i,10});
            Data.Cell2.Exp4 = Data.Cell2.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + 5
            Data.Cell2.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID5 = char(all.RecTable{i,10});
            Data.Cell2.Exp5 = Data.Cell2.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + 6
            Data.Cell2.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID6 = char(all.RecTable{i,10});
            Data.Cell2.Exp6 = Data.Cell2.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + 7
            Data.Cell2.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID7 = char(all.RecTable{i,10});
            Data.Cell2.Exp7 = Data.Cell2.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + 8
            Data.Cell2.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID8 = char(all.RecTable{i,10});
            Data.Cell2.Exp8 = Data.Cell2.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + 9
            Data.Cell2.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID9 = char(all.RecTable{i,10});
            Data.Cell2.Exp9 = Data.Cell2.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + 10
            Data.Cell2.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID10 = char(all.RecTable{i,10});
            Data.Cell2.Exp10 = Data.Cell2.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + 11
            Data.Cell2.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID11 = char(all.RecTable{i,10});
            Data.Cell2.Exp11 = Data.Cell2.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + 12
            Data.Cell2.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID12 = char(all.RecTable{i,10});
            Data.Cell2.Exp12 = Data.Cell2.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + 13
            Data.Cell2.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID13 = char(all.RecTable{i,10});
            Data.Cell2.Exp13 = Data.Cell2.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + 14
            Data.Cell2.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID14 = char(all.RecTable{i,10});
            Data.Cell2.Exp14 = Data.Cell2.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + 15
            Data.Cell2.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID15 = char(all.RecTable{i,10});
            Data.Cell2.Exp15 = Data.Cell2.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + 1
            Data.Cell3.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID1 = char(all.RecTable{i,10});
            Data.Cell3.Exp1 = Data.Cell3.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 2
            Data.Cell3.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID2 = char(all.RecTable{i,10});
            Data.Cell3.Exp2 = Data.Cell3.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 3
            Data.Cell3.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID3 = char(all.RecTable{i,10});
            Data.Cell3.Exp3 = Data.Cell3.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 4
            Data.Cell3.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID4 = char(all.RecTable{i,10});
            Data.Cell3.Exp4 = Data.Cell3.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 5
            Data.Cell3.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID5 = char(all.RecTable{i,10});
            Data.Cell3.Exp5 = Data.Cell3.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 6
            Data.Cell3.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID6 = char(all.RecTable{i,10});
            Data.Cell3.Exp6 = Data.Cell3.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 7
            Data.Cell3.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID7 = char(all.RecTable{i,10});
            Data.Cell3.Exp7 = Data.Cell3.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 8
            Data.Cell3.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID8 = char(all.RecTable{i,10});
            Data.Cell3.Exp8 = Data.Cell3.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 9
            Data.Cell3.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID9 = char(all.RecTable{i,10});
            Data.Cell3.Exp9 = Data.Cell3.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 10
            Data.Cell3.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID10 = char(all.RecTable{i,10});
            Data.Cell3.Exp10 = Data.Cell3.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 11
            Data.Cell3.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID11 = char(all.RecTable{i,10});
            Data.Cell3.Exp11 = Data.Cell3.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 12
            Data.Cell3.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID12 = char(all.RecTable{i,10});
            Data.Cell3.Exp12 = Data.Cell3.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 13
            Data.Cell3.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID13 = char(all.RecTable{i,10});
            Data.Cell3.Exp13 = Data.Cell3.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 14
            Data.Cell3.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID14 = char(all.RecTable{i,10});
            Data.Cell3.Exp14 = Data.Cell3.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 15
            Data.Cell3.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID15 = char(all.RecTable{i,10});
            Data.Cell3.Exp15 = Data.Cell3.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 1
            Data.Cell4.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID1 = char(all.RecTable{i,10});
            Data.Cell4.Exp1 = Data.Cell4.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 2
            Data.Cell4.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID2 = char(all.RecTable{i,10});
            Data.Cell4.Exp2 = Data.Cell4.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 3
            Data.Cell4.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID3 = char(all.RecTable{i,10});
            Data.Cell4.Exp3 = Data.Cell4.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 4
            Data.Cell4.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID4 = char(all.RecTable{i,10});
            Data.Cell4.Exp4 = Data.Cell4.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 5
            Data.Cell4.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID5 = char(all.RecTable{i,10});
            Data.Cell4.Exp5 = Data.Cell4.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 6
            Data.Cell4.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID6 = char(all.RecTable{i,10});
            Data.Cell4.Exp6 = Data.Cell4.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 7
            Data.Cell4.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID7 = char(all.RecTable{i,10});
            Data.Cell4.Exp7 = Data.Cell4.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 8
            Data.Cell4.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID8 = char(all.RecTable{i,10});
            Data.Cell4.Exp8 = Data.Cell4.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 9
            Data.Cell4.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID9 = char(all.RecTable{i,10});
            Data.Cell4.Exp9 = Data.Cell4.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 10
            Data.Cell4.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID10 = char(all.RecTable{i,10});
            Data.Cell4.Exp10 = Data.Cell4.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 11
            Data.Cell4.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID11 = char(all.RecTable{i,10});
            Data.Cell4.Exp11 = Data.Cell4.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 12
            Data.Cell4.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID12 = char(all.RecTable{i,10});
            Data.Cell4.Exp12 = Data.Cell4.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 13
            Data.Cell4.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID13 = char(all.RecTable{i,10});
            Data.Cell4.Exp13 = Data.Cell4.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 14
            Data.Cell4.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID14 = char(all.RecTable{i,10});
            Data.Cell4.Exp14 = Data.Cell4.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 15
            Data.Cell4.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID15 = char(all.RecTable{i,10});
            Data.Cell4.Exp15 = Data.Cell4.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 1
            Data.Cell5.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID1 = char(all.RecTable{i,10});
            Data.Cell5.Exp1 = Data.Cell5.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 2
            Data.Cell5.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID2 = char(all.RecTable{i,10});
            Data.Cell5.Exp2 = Data.Cell5.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 3
            Data.Cell5.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID3 = char(all.RecTable{i,10});
            Data.Cell5.Exp3 = Data.Cell5.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 4
            Data.Cell5.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID4 = char(all.RecTable{i,10});
            Data.Cell5.Exp4 = Data.Cell5.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 5
            Data.Cell5.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID5 = char(all.RecTable{i,10});
            Data.Cell5.Exp5 = Data.Cell5.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 6
            Data.Cell5.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID6 = char(all.RecTable{i,10});
            Data.Cell5.Exp6 = Data.Cell5.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 7
            Data.Cell5.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID7 = char(all.RecTable{i,10});
            Data.Cell5.Exp7 = Data.Cell5.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 8
            Data.Cell5.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID8 = char(all.RecTable{i,10});
            Data.Cell5.Exp8 = Data.Cell5.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 9
            Data.Cell5.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID9 = char(all.RecTable{i,10});
            Data.Cell5.Exp9 = Data.Cell5.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 10
            Data.Cell5.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID10 = char(all.RecTable{i,10});
            Data.Cell5.Exp10 = Data.Cell5.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 11
            Data.Cell5.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID11 = char(all.RecTable{i,10});
            Data.Cell5.Exp11 = Data.Cell5.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 12
            Data.Cell5.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID12 = char(all.RecTable{i,10});
            Data.Cell5.Exp12 = Data.Cell5.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 13
            Data.Cell5.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID13 = char(all.RecTable{i,10});
            Data.Cell5.Exp13 = Data.Cell5.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 14
            Data.Cell5.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID14 = char(all.RecTable{i,10});
            Data.Cell5.Exp14 = Data.Cell5.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts +  15
            Data.Cell5.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID15 = char(all.RecTable{i,10});
            Data.Cell5.Exp15 = Data.Cell5.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 1
            Data.Cell6.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID1 = char(all.RecTable{i,10});
            Data.Cell6.Exp1 = Data.Cell6.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 2
            Data.Cell6.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID2 = char(all.RecTable{i,10});
            Data.Cell6.Exp2 = Data.Cell6.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 3
            Data.Cell6.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID3 = char(all.RecTable{i,10});
            Data.Cell6.Exp3 = Data.Cell6.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 4
            Data.Cell6.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID4 = char(all.RecTable{i,10});
            Data.Cell6.Exp4 = Data.Cell6.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 5
            Data.Cell6.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID5 = char(all.RecTable{i,10});
            Data.Cell6.Exp5 = Data.Cell6.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 6
            Data.Cell6.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID6 = char(all.RecTable{i,10});
            Data.Cell6.Exp6 = Data.Cell6.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 7
            Data.Cell6.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID7 = char(all.RecTable{i,10});
            Data.Cell6.Exp7 = Data.Cell6.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 8
            Data.Cell6.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID8 = char(all.RecTable{i,10});
            Data.Cell6.Exp8 = Data.Cell6.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 9
            Data.Cell6.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID9 = char(all.RecTable{i,10});
            Data.Cell6.Exp9 = Data.Cell6.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 10
            Data.Cell6.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID10 = char(all.RecTable{i,10});
            Data.Cell6.Exp10 = Data.Cell6.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 11
            Data.Cell6.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID11 = char(all.RecTable{i,10});
            Data.Cell6.Exp11 = Data.Cell6.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 12
            Data.Cell6.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID12 = char(all.RecTable{i,10});
            Data.Cell6.Exp12 = Data.Cell6.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 13
            Data.Cell6.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID13 = char(all.RecTable{i,10});
            Data.Cell6.Exp13 = Data.Cell6.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 14
            Data.Cell6.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID14 = char(all.RecTable{i,10});
            Data.Cell6.Exp14 = Data.Cell6.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 15
            Data.Cell6.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID15 = char(all.RecTable{i,10});
            Data.Cell6.Exp15 = Data.Cell6.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 1
            Data.Cell7.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID1 = char(all.RecTable{i,10});
            Data.Cell7.Exp1 = Data.Cell7.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 2
            Data.Cell7.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID2 = char(all.RecTable{i,10});
            Data.Cell7.Exp2 = Data.Cell7.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 3
            Data.Cell7.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID3 = char(all.RecTable{i,10});
            Data.Cell7.Exp3 = Data.Cell7.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 4
            Data.Cell7.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID4 = char(all.RecTable{i,10});
            Data.Cell7.Exp4 = Data.Cell7.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 5
            Data.Cell7.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID5 = char(all.RecTable{i,10});
            Data.Cell7.Exp5 = Data.Cell7.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 6
            Data.Cell7.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID6 = char(all.RecTable{i,10});
            Data.Cell7.Exp6 = Data.Cell7.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 7
            Data.Cell7.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID7 = char(all.RecTable{i,10});
            Data.Cell7.Exp7 = Data.Cell7.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 8
            Data.Cell7.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID8 = char(all.RecTable{i,10});
            Data.Cell7.Exp8 = Data.Cell7.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 9
            Data.Cell7.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID9 = char(all.RecTable{i,10});
            Data.Cell7.Exp9 = Data.Cell7.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 10
            Data.Cell7.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID10 = char(all.RecTable{i,10});
            Data.Cell7.Exp10 = Data.Cell7.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 11
            Data.Cell7.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID11 = char(all.RecTable{i,10});
            Data.Cell7.Exp11 = Data.Cell7.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 12
            Data.Cell7.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID12 = char(all.RecTable{i,10});
            Data.Cell7.Exp12 = Data.Cell7.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 13
            Data.Cell7.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID13 = char(all.RecTable{i,10});
            Data.Cell7.Exp13 = Data.Cell7.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 14
            Data.Cell7.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID14 = char(all.RecTable{i,10});
            Data.Cell7.Exp14 = Data.Cell7.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 15
            Data.Cell7.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID15 = char(all.RecTable{i,10});
            Data.Cell7.Exp15 = Data.Cell7.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 1
            Data.Cell8.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID1 = char(all.RecTable{i,10});
            Data.Cell8.Exp1 = Data.Cell8.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 2
            Data.Cell8.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID2 = char(all.RecTable{i,10});
            Data.Cell8.Exp2 = Data.Cell8.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 3
            Data.Cell8.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID3 = char(all.RecTable{i,10});
            Data.Cell8.Exp3 = Data.Cell8.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 4
            Data.Cell8.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID4 = char(all.RecTable{i,10});
            Data.Cell8.Exp4 = Data.Cell8.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 5
            Data.Cell8.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID5 = char(all.RecTable{i,10});
            Data.Cell8.Exp5 = Data.Cell8.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 6
            Data.Cell8.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID6 = char(all.RecTable{i,10});
            Data.Cell8.Exp6 = Data.Cell8.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 7
            Data.Cell8.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID7 = char(all.RecTable{i,10});
            Data.Cell8.Exp7 = Data.Cell8.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 8
            Data.Cell8.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID8 = char(all.RecTable{i,10});
            Data.Cell8.Exp8 = Data.Cell8.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 9
            Data.Cell8.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID9 = char(all.RecTable{i,10});
            Data.Cell8.Exp9 = Data.Cell8.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 10
            Data.Cell8.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID10 = char(all.RecTable{i,10});
            Data.Cell8.Exp10 = Data.Cell8.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 11
            Data.Cell8.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID11 = char(all.RecTable{i,10});
            Data.Cell8.Exp11 = Data.Cell8.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 12
            Data.Cell8.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID12 = char(all.RecTable{i,10});
            Data.Cell8.Exp12 = Data.Cell8.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 13
            Data.Cell8.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID13 = char(all.RecTable{i,10});
            Data.Cell8.Exp13 = Data.Cell8.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 14
            Data.Cell8.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID14 = char(all.RecTable{i,10});
            Data.Cell8.Exp14 = Data.Cell8.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 15
            Data.Cell8.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID15 = char(all.RecTable{i,10});
            Data.Cell8.Exp15 = Data.Cell8.Exp15 * 1000;
        end
    end
elseif Data.CellNum == 9
    for i = 1:Data.Cell1.Expts
        if i == 1
            Data.Cell1.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID1 = char(all.RecTable{i,10});
            Data.Cell1.Exp1 = Data.Cell1.Exp1 * 1000;
        elseif i == 2
            Data.Cell1.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID2 = char(all.RecTable{i,10});
            Data.Cell1.Exp2 = Data.Cell1.Exp2 * 1000;
        elseif i == 3
            Data.Cell1.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID3 = char(all.RecTable{i,10});
            Data.Cell1.Exp3 = Data.Cell1.Exp3 * 1000;
        elseif i == 4
            Data.Cell1.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID4 = char(all.RecTable{i,10});
            Data.Cell1.Exp4 = Data.Cell1.Exp4 * 1000;
        elseif i == 5
            Data.Cell1.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID5 = char(all.RecTable{i,10});
            Data.Cell1.Exp5 = Data.Cell1.Exp5 * 1000;
        elseif i == 6
            Data.Cell1.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID6 = char(all.RecTable{i,10});
            Data.Cell1.Exp6 = Data.Cell1.Exp6 * 1000;
        elseif i == 7
            Data.Cell1.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID7 = char(all.RecTable{i,10});
            Data.Cell1.Exp7 = Data.Cell1.Exp7 * 1000;
        elseif i == 8
            Data.Cell1.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID8 = char(all.RecTable{i,10});
            Data.Cell1.Exp8 = Data.Cell1.Exp8 * 1000;
        elseif i == 9
            Data.Cell1.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID9 = char(all.RecTable{i,10});
            Data.Cell1.Exp9 = Data.Cell1.Exp9 * 1000;
        elseif i == 10
            Data.Cell1.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID10 = char(all.RecTable{i,10});
            Data.Cell1.Exp10 = Data.Cell1.Exp10 * 1000;
        elseif i == 11
            Data.Cell1.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID11 = char(all.RecTable{i,10});
            Data.Cell1.Exp11 = Data.Cell1.Exp11 * 1000;
        elseif i == 12
            Data.Cell1.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID12 = char(all.RecTable{i,10});
            Data.Cell1.Exp12 = Data.Cell1.Exp12 * 1000;
        elseif i == 13
            Data.Cell1.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID13 = char(all.RecTable{i,10});
            Data.Cell1.Exp13 = Data.Cell1.Exp13 * 1000;
        elseif i == 14
            Data.Cell1.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID14 = char(all.RecTable{i,10});
            Data.Cell1.Exp14 = Data.Cell1.Exp14 * 1000;
        elseif i == 15
            Data.Cell1.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID15 = char(all.RecTable{i,10});
            Data.Cell1.Exp15 = Data.Cell1.Exp15 * 1000;
        end
    end
    for i = Data.Cell1.Expts:(Data.Cell1.Expts + Data.Cell2.Expts)
        if i == Data.Cell1.Expts + 1
            Data.Cell2.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID1 = char(all.RecTable{i,10});
            Data.Cell2.Exp1 = Data.Cell2.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + 2
            Data.Cell2.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID2 = char(all.RecTable{i,10});
            Data.Cell2.Exp2 = Data.Cell2.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + 3
            Data.Cell2.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID3 = char(all.RecTable{i,10});
            Data.Cell2.Exp3 = Data.Cell2.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + 4
            Data.Cell2.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID4 = char(all.RecTable{i,10});
            Data.Cell2.Exp4 = Data.Cell2.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + 5
            Data.Cell2.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID5 = char(all.RecTable{i,10});
            Data.Cell2.Exp5 = Data.Cell2.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + 6
            Data.Cell2.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID6 = char(all.RecTable{i,10});
            Data.Cell2.Exp6 = Data.Cell2.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + 7
            Data.Cell2.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID7 = char(all.RecTable{i,10});
            Data.Cell2.Exp7 = Data.Cell2.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + 8
            Data.Cell2.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID8 = char(all.RecTable{i,10});
            Data.Cell2.Exp8 = Data.Cell2.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + 9
            Data.Cell2.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID9 = char(all.RecTable{i,10});
            Data.Cell2.Exp9 = Data.Cell2.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + 10
            Data.Cell2.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID10 = char(all.RecTable{i,10});
            Data.Cell2.Exp10 = Data.Cell2.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + 11
            Data.Cell2.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID11 = char(all.RecTable{i,10});
            Data.Cell2.Exp11 = Data.Cell2.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + 12
            Data.Cell2.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID12 = char(all.RecTable{i,10});
            Data.Cell2.Exp12 = Data.Cell2.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + 13
            Data.Cell2.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID13 = char(all.RecTable{i,10});
            Data.Cell2.Exp13 = Data.Cell2.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + 14
            Data.Cell2.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID14 = char(all.RecTable{i,10});
            Data.Cell2.Exp14 = Data.Cell2.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + 15
            Data.Cell2.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID15 = char(all.RecTable{i,10});
            Data.Cell2.Exp15 = Data.Cell2.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + 1
            Data.Cell3.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID1 = char(all.RecTable{i,10});
            Data.Cell3.Exp1 = Data.Cell3.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 2
            Data.Cell3.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID2 = char(all.RecTable{i,10});
            Data.Cell3.Exp2 = Data.Cell3.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 3
            Data.Cell3.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID3 = char(all.RecTable{i,10});
            Data.Cell3.Exp3 = Data.Cell3.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 4
            Data.Cell3.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID4 = char(all.RecTable{i,10});
            Data.Cell3.Exp4 = Data.Cell3.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 5
            Data.Cell3.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID5 = char(all.RecTable{i,10});
            Data.Cell3.Exp5 = Data.Cell3.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 6
            Data.Cell3.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID6 = char(all.RecTable{i,10});
            Data.Cell3.Exp6 = Data.Cell3.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 7
            Data.Cell3.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID7 = char(all.RecTable{i,10});
            Data.Cell3.Exp7 = Data.Cell3.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 8
            Data.Cell3.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID8 = char(all.RecTable{i,10});
            Data.Cell3.Exp8 = Data.Cell3.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 9
            Data.Cell3.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID9 = char(all.RecTable{i,10});
            Data.Cell3.Exp9 = Data.Cell3.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 10
            Data.Cell3.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID10 = char(all.RecTable{i,10});
            Data.Cell3.Exp10 = Data.Cell3.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 11
            Data.Cell3.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID11 = char(all.RecTable{i,10});
            Data.Cell3.Exp11 = Data.Cell3.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 12
            Data.Cell3.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID12 = char(all.RecTable{i,10});
            Data.Cell3.Exp12 = Data.Cell3.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 13
            Data.Cell3.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID13 = char(all.RecTable{i,10});
            Data.Cell3.Exp13 = Data.Cell3.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 14
            Data.Cell3.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID14 = char(all.RecTable{i,10});
            Data.Cell3.Exp14 = Data.Cell3.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 15
            Data.Cell3.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID15 = char(all.RecTable{i,10});
            Data.Cell3.Exp15 = Data.Cell3.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 1
            Data.Cell4.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID1 = char(all.RecTable{i,10});
            Data.Cell4.Exp1 = Data.Cell4.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 2
            Data.Cell4.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID2 = char(all.RecTable{i,10});
            Data.Cell4.Exp2 = Data.Cell4.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 3
            Data.Cell4.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID3 = char(all.RecTable{i,10});
            Data.Cell4.Exp3 = Data.Cell4.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 4
            Data.Cell4.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID4 = char(all.RecTable{i,10});
            Data.Cell4.Exp4 = Data.Cell4.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 5
            Data.Cell4.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID5 = char(all.RecTable{i,10});
            Data.Cell4.Exp5 = Data.Cell4.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 6
            Data.Cell4.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID6 = char(all.RecTable{i,10});
            Data.Cell4.Exp6 = Data.Cell4.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 7
            Data.Cell4.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID7 = char(all.RecTable{i,10});
            Data.Cell4.Exp7 = Data.Cell4.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 8
            Data.Cell4.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID8 = char(all.RecTable{i,10});
            Data.Cell4.Exp8 = Data.Cell4.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 9
            Data.Cell4.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID9 = char(all.RecTable{i,10});
            Data.Cell4.Exp9 = Data.Cell4.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 10
            Data.Cell4.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID10 = char(all.RecTable{i,10});
            Data.Cell4.Exp10 = Data.Cell4.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 11
            Data.Cell4.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID11 = char(all.RecTable{i,10});
            Data.Cell4.Exp11 = Data.Cell4.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 12
            Data.Cell4.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID12 = char(all.RecTable{i,10});
            Data.Cell4.Exp12 = Data.Cell4.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 13
            Data.Cell4.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID13 = char(all.RecTable{i,10});
            Data.Cell4.Exp13 = Data.Cell4.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 14
            Data.Cell4.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID14 = char(all.RecTable{i,10});
            Data.Cell4.Exp14 = Data.Cell4.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 15
            Data.Cell4.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID15 = char(all.RecTable{i,10});
            Data.Cell4.Exp15 = Data.Cell4.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 1
            Data.Cell5.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID1 = char(all.RecTable{i,10});
            Data.Cell5.Exp1 = Data.Cell5.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 2
            Data.Cell5.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID2 = char(all.RecTable{i,10});
            Data.Cell5.Exp2 = Data.Cell5.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 3
            Data.Cell5.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID3 = char(all.RecTable{i,10});
            Data.Cell5.Exp3 = Data.Cell5.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 4
            Data.Cell5.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID4 = char(all.RecTable{i,10});
            Data.Cell5.Exp4 = Data.Cell5.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 5
            Data.Cell5.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID5 = char(all.RecTable{i,10});
            Data.Cell5.Exp5 = Data.Cell5.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 6
            Data.Cell5.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID6 = char(all.RecTable{i,10});
            Data.Cell5.Exp6 = Data.Cell5.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 7
            Data.Cell5.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID7 = char(all.RecTable{i,10});
            Data.Cell5.Exp7 = Data.Cell5.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 8
            Data.Cell5.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID8 = char(all.RecTable{i,10});
            Data.Cell5.Exp8 = Data.Cell5.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 9
            Data.Cell5.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID9 = char(all.RecTable{i,10});
            Data.Cell5.Exp9 = Data.Cell5.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 10
            Data.Cell5.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID10 = char(all.RecTable{i,10});
            Data.Cell5.Exp10 = Data.Cell5.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 11
            Data.Cell5.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID11 = char(all.RecTable{i,10});
            Data.Cell5.Exp11 = Data.Cell5.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 12
            Data.Cell5.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID12 = char(all.RecTable{i,10});
            Data.Cell5.Exp12 = Data.Cell5.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 13
            Data.Cell5.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID13 = char(all.RecTable{i,10});
            Data.Cell5.Exp13 = Data.Cell5.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 14
            Data.Cell5.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID14 = char(all.RecTable{i,10});
            Data.Cell5.Exp14 = Data.Cell5.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts +  15
            Data.Cell5.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID15 = char(all.RecTable{i,10});
            Data.Cell5.Exp15 = Data.Cell5.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 1
            Data.Cell6.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID1 = char(all.RecTable{i,10});
            Data.Cell6.Exp1 = Data.Cell6.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 2
            Data.Cell6.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID2 = char(all.RecTable{i,10});
            Data.Cell6.Exp2 = Data.Cell6.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 3
            Data.Cell6.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID3 = char(all.RecTable{i,10});
            Data.Cell6.Exp3 = Data.Cell6.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 4
            Data.Cell6.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID4 = char(all.RecTable{i,10});
            Data.Cell6.Exp4 = Data.Cell6.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 5
            Data.Cell6.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID5 = char(all.RecTable{i,10});
            Data.Cell6.Exp5 = Data.Cell6.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 6
            Data.Cell6.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID6 = char(all.RecTable{i,10});
            Data.Cell6.Exp6 = Data.Cell6.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 7
            Data.Cell6.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID7 = char(all.RecTable{i,10});
            Data.Cell6.Exp7 = Data.Cell6.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 8
            Data.Cell6.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID8 = char(all.RecTable{i,10});
            Data.Cell6.Exp8 = Data.Cell6.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 9
            Data.Cell6.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID9 = char(all.RecTable{i,10});
            Data.Cell6.Exp9 = Data.Cell6.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 10
            Data.Cell6.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID10 = char(all.RecTable{i,10});
            Data.Cell6.Exp10 = Data.Cell6.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 11
            Data.Cell6.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID11 = char(all.RecTable{i,10});
            Data.Cell6.Exp11 = Data.Cell6.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 12
            Data.Cell6.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID12 = char(all.RecTable{i,10});
            Data.Cell6.Exp12 = Data.Cell6.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 13
            Data.Cell6.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID13 = char(all.RecTable{i,10});
            Data.Cell6.Exp13 = Data.Cell6.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 14
            Data.Cell6.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID14 = char(all.RecTable{i,10});
            Data.Cell6.Exp14 = Data.Cell6.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 15
            Data.Cell6.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID15 = char(all.RecTable{i,10});
            Data.Cell6.Exp15 = Data.Cell6.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 1
            Data.Cell7.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID1 = char(all.RecTable{i,10});
            Data.Cell7.Exp1 = Data.Cell7.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 2
            Data.Cell7.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID2 = char(all.RecTable{i,10});
            Data.Cell7.Exp2 = Data.Cell7.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 3
            Data.Cell7.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID3 = char(all.RecTable{i,10});
            Data.Cell7.Exp3 = Data.Cell7.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 4
            Data.Cell7.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID4 = char(all.RecTable{i,10});
            Data.Cell7.Exp4 = Data.Cell7.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 5
            Data.Cell7.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID5 = char(all.RecTable{i,10});
            Data.Cell7.Exp5 = Data.Cell7.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 6
            Data.Cell7.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID6 = char(all.RecTable{i,10});
            Data.Cell7.Exp6 = Data.Cell7.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 7
            Data.Cell7.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID7 = char(all.RecTable{i,10});
            Data.Cell7.Exp7 = Data.Cell7.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 8
            Data.Cell7.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID8 = char(all.RecTable{i,10});
            Data.Cell7.Exp8 = Data.Cell7.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 9
            Data.Cell7.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID9 = char(all.RecTable{i,10});
            Data.Cell7.Exp9 = Data.Cell7.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 10
            Data.Cell7.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID10 = char(all.RecTable{i,10});
            Data.Cell7.Exp10 = Data.Cell7.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 11
            Data.Cell7.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID11 = char(all.RecTable{i,10});
            Data.Cell7.Exp11 = Data.Cell7.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 12
            Data.Cell7.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID12 = char(all.RecTable{i,10});
            Data.Cell7.Exp12 = Data.Cell7.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 13
            Data.Cell7.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID13 = char(all.RecTable{i,10});
            Data.Cell7.Exp13 = Data.Cell7.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 14
            Data.Cell7.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID14 = char(all.RecTable{i,10});
            Data.Cell7.Exp14 = Data.Cell7.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 15
            Data.Cell7.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID15 = char(all.RecTable{i,10});
            Data.Cell7.Exp15 = Data.Cell7.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 1
            Data.Cell8.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID1 = char(all.RecTable{i,10});
            Data.Cell8.Exp1 = Data.Cell8.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 2
            Data.Cell8.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID2 = char(all.RecTable{i,10});
            Data.Cell8.Exp2 = Data.Cell8.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 3
            Data.Cell8.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID3 = char(all.RecTable{i,10});
            Data.Cell8.Exp3 = Data.Cell8.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 4
            Data.Cell8.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID4 = char(all.RecTable{i,10});
            Data.Cell8.Exp4 = Data.Cell8.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 5
            Data.Cell8.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID5 = char(all.RecTable{i,10});
            Data.Cell8.Exp5 = Data.Cell8.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 6
            Data.Cell8.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID6 = char(all.RecTable{i,10});
            Data.Cell8.Exp6 = Data.Cell8.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 7
            Data.Cell8.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID7 = char(all.RecTable{i,10});
            Data.Cell8.Exp7 = Data.Cell8.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 8
            Data.Cell8.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID8 = char(all.RecTable{i,10});
            Data.Cell8.Exp8 = Data.Cell8.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 9
            Data.Cell8.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID9 = char(all.RecTable{i,10});
            Data.Cell8.Exp9 = Data.Cell8.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 10
            Data.Cell8.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID10 = char(all.RecTable{i,10});
            Data.Cell8.Exp10 = Data.Cell8.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 11
            Data.Cell8.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID11 = char(all.RecTable{i,10});
            Data.Cell8.Exp11 = Data.Cell8.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 12
            Data.Cell8.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID12 = char(all.RecTable{i,10});
            Data.Cell8.Exp12 = Data.Cell8.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 13
            Data.Cell8.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID13 = char(all.RecTable{i,10});
            Data.Cell8.Exp13 = Data.Cell8.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 14
            Data.Cell8.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID14 = char(all.RecTable{i,10});
            Data.Cell8.Exp14 = Data.Cell8.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 15
            Data.Cell8.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID15 = char(all.RecTable{i,10});
            Data.Cell8.Exp15 = Data.Cell8.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + Data.Cell9.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 1
            Data.Cell9.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID1 = char(all.RecTable{i,10});
            Data.Cell9.Exp1 = Data.Cell9.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 2
            Data.Cell9.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID2 = char(all.RecTable{i,10});
            Data.Cell9.Exp2 = Data.Cell9.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 3
            Data.Cell9.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID3 = char(all.RecTable{i,10});
            Data.Cell9.Exp3 = Data.Cell9.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 4
            Data.Cell9.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID4 = char(all.RecTable{i,10});
            Data.Cell9.Exp4 = Data.Cell9.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 5
            Data.Cell9.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID5 = char(all.RecTable{i,10});
            Data.Cell9.Exp5 = Data.Cell9.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 6
            Data.Cell9.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID6 = char(all.RecTable{i,10});
            Data.Cell9.Exp6 = Data.Cell9.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 7
            Data.Cell9.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID7 = char(all.RecTable{i,10});
            Data.Cell9.Exp7 = Data.Cell9.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 8
            Data.Cell9.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID8 = char(all.RecTable{i,10});
            Data.Cell9.Exp8 = Data.Cell9.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 9
            Data.Cell9.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID9 = char(all.RecTable{i,10});
            Data.Cell9.Exp9 = Data.Cell9.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 10
            Data.Cell9.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID10 = char(all.RecTable{i,10});
            Data.Cell9.Exp10 = Data.Cell9.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 11
            Data.Cell9.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID11 = char(all.RecTable{i,10});
            Data.Cell9.Exp11 = Data.Cell9.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 12
            Data.Cell9.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID12 = char(all.RecTable{i,10});
            Data.Cell9.Exp12 = Data.Cell9.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 13
            Data.Cell9.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID13 = char(all.RecTable{i,10});
            Data.Cell9.Exp13 = Data.Cell9.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 14
            Data.Cell9.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID14 = char(all.RecTable{i,10});
            Data.Cell9.Exp14 = Data.Cell9.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 15
            Data.Cell9.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID15 = char(all.RecTable{i,10});
            Data.Cell9.Exp15 = Data.Cell9.Exp15 * 1000;
        end
    end
elseif Data.CellNum == 10
    for i = 1:Data.Cell1.Expts
        if i == 1
            Data.Cell1.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID1 = char(all.RecTable{i,10});
            Data.Cell1.Exp1 = Data.Cell1.Exp1 * 1000;
        elseif i == 2
            Data.Cell1.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID2 = char(all.RecTable{i,10});
            Data.Cell1.Exp2 = Data.Cell1.Exp2 * 1000;
        elseif i == 3
            Data.Cell1.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID3 = char(all.RecTable{i,10});
            Data.Cell1.Exp3 = Data.Cell1.Exp3 * 1000;
        elseif i == 4
            Data.Cell1.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID4 = char(all.RecTable{i,10});
            Data.Cell1.Exp4 = Data.Cell1.Exp4 * 1000;
        elseif i == 5
            Data.Cell1.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID5 = char(all.RecTable{i,10});
            Data.Cell1.Exp5 = Data.Cell1.Exp5 * 1000;
        elseif i == 6
            Data.Cell1.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID6 = char(all.RecTable{i,10});
            Data.Cell1.Exp6 = Data.Cell1.Exp6 * 1000;
        elseif i == 7
            Data.Cell1.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID7 = char(all.RecTable{i,10});
            Data.Cell1.Exp7 = Data.Cell1.Exp7 * 1000;
        elseif i == 8
            Data.Cell1.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID8 = char(all.RecTable{i,10});
            Data.Cell1.Exp8 = Data.Cell1.Exp8 * 1000;
        elseif i == 9
            Data.Cell1.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID9 = char(all.RecTable{i,10});
            Data.Cell1.Exp9 = Data.Cell1.Exp9 * 1000;
        elseif i == 10
            Data.Cell1.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID10 = char(all.RecTable{i,10});
            Data.Cell1.Exp10 = Data.Cell1.Exp10 * 1000;
        elseif i == 11
            Data.Cell1.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID11 = char(all.RecTable{i,10});
            Data.Cell1.Exp11 = Data.Cell1.Exp11 * 1000;
        elseif i == 12
            Data.Cell1.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID12 = char(all.RecTable{i,10});
            Data.Cell1.Exp12 = Data.Cell1.Exp12 * 1000;
        elseif i == 13
            Data.Cell1.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID13 = char(all.RecTable{i,10});
            Data.Cell1.Exp13 = Data.Cell1.Exp13 * 1000;
        elseif i == 14
            Data.Cell1.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID14 = char(all.RecTable{i,10});
            Data.Cell1.Exp14 = Data.Cell1.Exp14 * 1000;
        elseif i == 15
            Data.Cell1.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell1.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell1.ExptID15 = char(all.RecTable{i,10});
            Data.Cell1.Exp15 = Data.Cell1.Exp15 * 1000;
        end
    end
    for i = Data.Cell1.Expts:(Data.Cell1.Expts + Data.Cell2.Expts)
        if i == Data.Cell1.Expts + 1
            Data.Cell2.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID1 = char(all.RecTable{i,10});
            Data.Cell2.Exp1 = Data.Cell2.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + 2
            Data.Cell2.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID2 = char(all.RecTable{i,10});
            Data.Cell2.Exp2 = Data.Cell2.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + 3
            Data.Cell2.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID3 = char(all.RecTable{i,10});
            Data.Cell2.Exp3 = Data.Cell2.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + 4
            Data.Cell2.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID4 = char(all.RecTable{i,10});
            Data.Cell2.Exp4 = Data.Cell2.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + 5
            Data.Cell2.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID5 = char(all.RecTable{i,10});
            Data.Cell2.Exp5 = Data.Cell2.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + 6
            Data.Cell2.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID6 = char(all.RecTable{i,10});
            Data.Cell2.Exp6 = Data.Cell2.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + 7
            Data.Cell2.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID7 = char(all.RecTable{i,10});
            Data.Cell2.Exp7 = Data.Cell2.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + 8
            Data.Cell2.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID8 = char(all.RecTable{i,10});
            Data.Cell2.Exp8 = Data.Cell2.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + 9
            Data.Cell2.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID9 = char(all.RecTable{i,10});
            Data.Cell2.Exp9 = Data.Cell2.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + 10
            Data.Cell2.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID10 = char(all.RecTable{i,10});
            Data.Cell2.Exp10 = Data.Cell2.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + 11
            Data.Cell2.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID11 = char(all.RecTable{i,10});
            Data.Cell2.Exp11 = Data.Cell2.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + 12
            Data.Cell2.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID12 = char(all.RecTable{i,10});
            Data.Cell2.Exp12 = Data.Cell2.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + 13
            Data.Cell2.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID13 = char(all.RecTable{i,10});
            Data.Cell2.Exp13 = Data.Cell2.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + 14
            Data.Cell2.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID14 = char(all.RecTable{i,10});
            Data.Cell2.Exp14 = Data.Cell2.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + 15
            Data.Cell2.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell2.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell2.ExptID15 = char(all.RecTable{i,10});
            Data.Cell2.Exp15 = Data.Cell2.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + 1
            Data.Cell3.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID1 = char(all.RecTable{i,10});
            Data.Cell3.Exp1 = Data.Cell3.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 2
            Data.Cell3.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID2 = char(all.RecTable{i,10});
            Data.Cell3.Exp2 = Data.Cell3.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 3
            Data.Cell3.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID3 = char(all.RecTable{i,10});
            Data.Cell3.Exp3 = Data.Cell3.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 4
            Data.Cell3.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID4 = char(all.RecTable{i,10});
            Data.Cell3.Exp4 = Data.Cell3.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 5
            Data.Cell3.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID5 = char(all.RecTable{i,10});
            Data.Cell3.Exp5 = Data.Cell3.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 6
            Data.Cell3.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID6 = char(all.RecTable{i,10});
            Data.Cell3.Exp6 = Data.Cell3.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 7
            Data.Cell3.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID7 = char(all.RecTable{i,10});
            Data.Cell3.Exp7 = Data.Cell3.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 8
            Data.Cell3.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID8 = char(all.RecTable{i,10});
            Data.Cell3.Exp8 = Data.Cell3.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 9
            Data.Cell3.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID9 = char(all.RecTable{i,10});
            Data.Cell3.Exp9 = Data.Cell3.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 10
            Data.Cell3.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID10 = char(all.RecTable{i,10});
            Data.Cell3.Exp10 = Data.Cell3.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 11
            Data.Cell3.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID11 = char(all.RecTable{i,10});
            Data.Cell3.Exp11 = Data.Cell3.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 12
            Data.Cell3.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID12 = char(all.RecTable{i,10});
            Data.Cell3.Exp12 = Data.Cell3.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 13
            Data.Cell3.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID13 = char(all.RecTable{i,10});
            Data.Cell3.Exp13 = Data.Cell3.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 14
            Data.Cell3.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID14 = char(all.RecTable{i,10});
            Data.Cell3.Exp14 = Data.Cell3.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + 15
            Data.Cell3.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell3.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell3.ExptID15 = char(all.RecTable{i,10});
            Data.Cell3.Exp15 = Data.Cell3.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 1
            Data.Cell4.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID1 = char(all.RecTable{i,10});
            Data.Cell4.Exp1 = Data.Cell4.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 2
            Data.Cell4.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID2 = char(all.RecTable{i,10});
            Data.Cell4.Exp2 = Data.Cell4.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 3
            Data.Cell4.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID3 = char(all.RecTable{i,10});
            Data.Cell4.Exp3 = Data.Cell4.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 4
            Data.Cell4.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID4 = char(all.RecTable{i,10});
            Data.Cell4.Exp4 = Data.Cell4.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 5
            Data.Cell4.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID5 = char(all.RecTable{i,10});
            Data.Cell4.Exp5 = Data.Cell4.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 6
            Data.Cell4.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID6 = char(all.RecTable{i,10});
            Data.Cell4.Exp6 = Data.Cell4.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 7
            Data.Cell4.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID7 = char(all.RecTable{i,10});
            Data.Cell4.Exp7 = Data.Cell4.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 8
            Data.Cell4.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID8 = char(all.RecTable{i,10});
            Data.Cell4.Exp8 = Data.Cell4.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 9
            Data.Cell4.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID9 = char(all.RecTable{i,10});
            Data.Cell4.Exp9 = Data.Cell4.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 10
            Data.Cell4.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID10 = char(all.RecTable{i,10});
            Data.Cell4.Exp10 = Data.Cell4.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 11
            Data.Cell4.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID11 = char(all.RecTable{i,10});
            Data.Cell4.Exp11 = Data.Cell4.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 12
            Data.Cell4.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID12 = char(all.RecTable{i,10});
            Data.Cell4.Exp12 = Data.Cell4.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 13
            Data.Cell4.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID13 = char(all.RecTable{i,10});
            Data.Cell4.Exp13 = Data.Cell4.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 14
            Data.Cell4.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID14 = char(all.RecTable{i,10});
            Data.Cell4.Exp14 = Data.Cell4.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + 15
            Data.Cell4.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell4.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell4.ExptID15 = char(all.RecTable{i,10});
            Data.Cell4.Exp15 = Data.Cell4.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 1
            Data.Cell5.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID1 = char(all.RecTable{i,10});
            Data.Cell5.Exp1 = Data.Cell5.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 2
            Data.Cell5.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID2 = char(all.RecTable{i,10});
            Data.Cell5.Exp2 = Data.Cell5.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 3
            Data.Cell5.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID3 = char(all.RecTable{i,10});
            Data.Cell5.Exp3 = Data.Cell5.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 4
            Data.Cell5.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID4 = char(all.RecTable{i,10});
            Data.Cell5.Exp4 = Data.Cell5.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 5
            Data.Cell5.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID5 = char(all.RecTable{i,10});
            Data.Cell5.Exp5 = Data.Cell5.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 6
            Data.Cell5.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID6 = char(all.RecTable{i,10});
            Data.Cell5.Exp6 = Data.Cell5.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 7
            Data.Cell5.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID7 = char(all.RecTable{i,10});
            Data.Cell5.Exp7 = Data.Cell5.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 8
            Data.Cell5.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID8 = char(all.RecTable{i,10});
            Data.Cell5.Exp8 = Data.Cell5.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 9
            Data.Cell5.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID9 = char(all.RecTable{i,10});
            Data.Cell5.Exp9 = Data.Cell5.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 10
            Data.Cell5.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID10 = char(all.RecTable{i,10});
            Data.Cell5.Exp10 = Data.Cell5.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 11
            Data.Cell5.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID11 = char(all.RecTable{i,10});
            Data.Cell5.Exp11 = Data.Cell5.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 12
            Data.Cell5.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID12 = char(all.RecTable{i,10});
            Data.Cell5.Exp12 = Data.Cell5.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 13
            Data.Cell5.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID13 = char(all.RecTable{i,10});
            Data.Cell5.Exp13 = Data.Cell5.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + 14
            Data.Cell5.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID14 = char(all.RecTable{i,10});
            Data.Cell5.Exp14 = Data.Cell5.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts +  15
            Data.Cell5.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell5.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell5.ExptID15 = char(all.RecTable{i,10});
            Data.Cell5.Exp15 = Data.Cell5.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 1
            Data.Cell6.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID1 = char(all.RecTable{i,10});
            Data.Cell6.Exp1 = Data.Cell6.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 2
            Data.Cell6.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID2 = char(all.RecTable{i,10});
            Data.Cell6.Exp2 = Data.Cell6.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 3
            Data.Cell6.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID3 = char(all.RecTable{i,10});
            Data.Cell6.Exp3 = Data.Cell6.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 4
            Data.Cell6.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID4 = char(all.RecTable{i,10});
            Data.Cell6.Exp4 = Data.Cell6.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 5
            Data.Cell6.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID5 = char(all.RecTable{i,10});
            Data.Cell6.Exp5 = Data.Cell6.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 6
            Data.Cell6.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID6 = char(all.RecTable{i,10});
            Data.Cell6.Exp6 = Data.Cell6.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 7
            Data.Cell6.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID7 = char(all.RecTable{i,10});
            Data.Cell6.Exp7 = Data.Cell6.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 8
            Data.Cell6.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID8 = char(all.RecTable{i,10});
            Data.Cell6.Exp8 = Data.Cell6.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 9
            Data.Cell6.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID9 = char(all.RecTable{i,10});
            Data.Cell6.Exp9 = Data.Cell6.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 10
            Data.Cell6.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID10 = char(all.RecTable{i,10});
            Data.Cell6.Exp10 = Data.Cell6.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 11
            Data.Cell6.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID11 = char(all.RecTable{i,10});
            Data.Cell6.Exp11 = Data.Cell6.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 12
            Data.Cell6.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID12 = char(all.RecTable{i,10});
            Data.Cell6.Exp12 = Data.Cell6.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 13
            Data.Cell6.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID13 = char(all.RecTable{i,10});
            Data.Cell6.Exp13 = Data.Cell6.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 14
            Data.Cell6.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID14 = char(all.RecTable{i,10});
            Data.Cell6.Exp14 = Data.Cell6.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + 15
            Data.Cell6.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell6.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell6.ExptID15 = char(all.RecTable{i,10});
            Data.Cell6.Exp15 = Data.Cell6.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 1
            Data.Cell7.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID1 = char(all.RecTable{i,10});
            Data.Cell7.Exp1 = Data.Cell7.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 2
            Data.Cell7.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID2 = char(all.RecTable{i,10});
            Data.Cell7.Exp2 = Data.Cell7.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 3
            Data.Cell7.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID3 = char(all.RecTable{i,10});
            Data.Cell7.Exp3 = Data.Cell7.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 4
            Data.Cell7.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID4 = char(all.RecTable{i,10});
            Data.Cell7.Exp4 = Data.Cell7.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 5
            Data.Cell7.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID5 = char(all.RecTable{i,10});
            Data.Cell7.Exp5 = Data.Cell7.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 6
            Data.Cell7.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID6 = char(all.RecTable{i,10});
            Data.Cell7.Exp6 = Data.Cell7.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 7
            Data.Cell7.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID7 = char(all.RecTable{i,10});
            Data.Cell7.Exp7 = Data.Cell7.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 8
            Data.Cell7.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID8 = char(all.RecTable{i,10});
            Data.Cell7.Exp8 = Data.Cell7.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 9
            Data.Cell7.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID9 = char(all.RecTable{i,10});
            Data.Cell7.Exp9 = Data.Cell7.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 10
            Data.Cell7.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID10 = char(all.RecTable{i,10});
            Data.Cell7.Exp10 = Data.Cell7.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 11
            Data.Cell7.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID11 = char(all.RecTable{i,10});
            Data.Cell7.Exp11 = Data.Cell7.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 12
            Data.Cell7.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID12 = char(all.RecTable{i,10});
            Data.Cell7.Exp12 = Data.Cell7.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 13
            Data.Cell7.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID13 = char(all.RecTable{i,10});
            Data.Cell7.Exp13 = Data.Cell7.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 14
            Data.Cell7.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID14 = char(all.RecTable{i,10});
            Data.Cell7.Exp14 = Data.Cell7.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + 15
            Data.Cell7.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell7.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell7.ExptID15 = char(all.RecTable{i,10});
            Data.Cell7.Exp15 = Data.Cell7.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 1
            Data.Cell8.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID1 = char(all.RecTable{i,10});
            Data.Cell8.Exp1 = Data.Cell8.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 2
            Data.Cell8.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID2 = char(all.RecTable{i,10});
            Data.Cell8.Exp2 = Data.Cell8.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 3
            Data.Cell8.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID3 = char(all.RecTable{i,10});
            Data.Cell8.Exp3 = Data.Cell8.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 4
            Data.Cell8.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID4 = char(all.RecTable{i,10});
            Data.Cell8.Exp4 = Data.Cell8.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 5
            Data.Cell8.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID5 = char(all.RecTable{i,10});
            Data.Cell8.Exp5 = Data.Cell8.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 6
            Data.Cell8.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID6 = char(all.RecTable{i,10});
            Data.Cell8.Exp6 = Data.Cell8.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 7
            Data.Cell8.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID7 = char(all.RecTable{i,10});
            Data.Cell8.Exp7 = Data.Cell8.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 8
            Data.Cell8.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID8 = char(all.RecTable{i,10});
            Data.Cell8.Exp8 = Data.Cell8.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 9
            Data.Cell8.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID9 = char(all.RecTable{i,10});
            Data.Cell8.Exp9 = Data.Cell8.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 10
            Data.Cell8.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID10 = char(all.RecTable{i,10});
            Data.Cell8.Exp10 = Data.Cell8.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 11
            Data.Cell8.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID11 = char(all.RecTable{i,10});
            Data.Cell8.Exp11 = Data.Cell8.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 12
            Data.Cell8.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID12 = char(all.RecTable{i,10});
            Data.Cell8.Exp12 = Data.Cell8.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 13
            Data.Cell8.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID13 = char(all.RecTable{i,10});
            Data.Cell8.Exp13 = Data.Cell8.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 14
            Data.Cell8.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID14 = char(all.RecTable{i,10});
            Data.Cell8.Exp14 = Data.Cell8.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + 15
            Data.Cell8.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell8.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell8.ExptID15 = char(all.RecTable{i,10});
            Data.Cell8.Exp15 = Data.Cell8.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + Data.Cell9.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 1
            Data.Cell9.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID1 = char(all.RecTable{i,10});
            Data.Cell9.Exp1 = Data.Cell9.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 2
            Data.Cell9.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID2 = char(all.RecTable{i,10});
            Data.Cell9.Exp2 = Data.Cell9.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 3
            Data.Cell9.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID3 = char(all.RecTable{i,10});
            Data.Cell9.Exp3 = Data.Cell9.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 4
            Data.Cell9.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID4 = char(all.RecTable{i,10});
            Data.Cell9.Exp4 = Data.Cell9.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 5
            Data.Cell9.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID5 = char(all.RecTable{i,10});
            Data.Cell9.Exp5 = Data.Cell9.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 6
            Data.Cell9.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID6 = char(all.RecTable{i,10});
            Data.Cell9.Exp6 = Data.Cell9.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 7
            Data.Cell9.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID7 = char(all.RecTable{i,10});
            Data.Cell9.Exp7 = Data.Cell9.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 8
            Data.Cell9.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID8 = char(all.RecTable{i,10});
            Data.Cell9.Exp8 = Data.Cell9.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 9
            Data.Cell9.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID9 = char(all.RecTable{i,10});
            Data.Cell9.Exp9 = Data.Cell9.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 10
            Data.Cell9.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID10 = char(all.RecTable{i,10});
            Data.Cell9.Exp10 = Data.Cell9.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 11
            Data.Cell9.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID11 = char(all.RecTable{i,10});
            Data.Cell9.Exp11 = Data.Cell9.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 12
            Data.Cell9.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID12 = char(all.RecTable{i,10});
            Data.Cell9.Exp12 = Data.Cell9.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 13
            Data.Cell9.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID13 = char(all.RecTable{i,10});
            Data.Cell9.Exp13 = Data.Cell9.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 14
            Data.Cell9.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID14 = char(all.RecTable{i,10});
            Data.Cell9.Exp14 = Data.Cell9.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + 15
            Data.Cell9.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell9.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell9.ExptID15 = char(all.RecTable{i,10});
            Data.Cell9.Exp15 = Data.Cell9.Exp15 * 1000;
        end
    end
    for i = (Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + Data.Cell9.Expts):(Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + Data.Cell9.Expts + Data.Cell10.Expts)
        if i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + Data.Cell9.Expts + 1
            Data.Cell10.Exp1 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell10.Stim1 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell10.ExptID1 = char(all.RecTable{i,10});
            Data.Cell10.Exp1 = Data.Cell10.Exp1 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + Data.Cell9.Expts + 2
            Data.Cell10.Exp2 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell10.Stim2 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell10.ExptID2 = char(all.RecTable{i,10});
            Data.Cell10.Exp2 = Data.Cell10.Exp2 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + Data.Cell9.Expts + 3
            Data.Cell10.Exp3 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell10.Stim3 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell10.ExptID3 = char(all.RecTable{i,10});
            Data.Cell10.Exp3 = Data.Cell10.Exp3 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + Data.Cell9.Expts + 4
            Data.Cell10.Exp4 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell10.Stim4 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell10.ExptID4 = char(all.RecTable{i,10});
            Data.Cell10.Exp4 = Data.Cell10.Exp4 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + Data.Cell9.Expts + 5
            Data.Cell10.Exp5 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell10.Stim5 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell10.ExptID5 = char(all.RecTable{i,10});
            Data.Cell10.Exp5 = Data.Cell10.Exp5 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + Data.Cell9.Expts + 6
            Data.Cell10.Exp6 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell10.Stim6 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell10.ExptID6 = char(all.RecTable{i,10});
            Data.Cell10.Exp6 = Data.Cell10.Exp6 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + Data.Cell9.Expts + 7
            Data.Cell10.Exp7 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell10.Stim7 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell10.ExptID7 = char(all.RecTable{i,10});
            Data.Cell10.Exp7 = Data.Cell10.Exp7 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + Data.Cell9.Expts + 8
            Data.Cell10.Exp8 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell10.Stim8 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell10.ExptID8 = char(all.RecTable{i,10});
            Data.Cell10.Exp8 = Data.Cell10.Exp8 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + Data.Cell9.Expts + 9
            Data.Cell10.Exp9 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell10.Stim9 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell10.ExptID9 = char(all.RecTable{i,10});
            Data.Cell10.Exp9 = Data.Cell10.Exp9 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + Data.Cell9.Expts + 10
            Data.Cell10.Exp10 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell10.Stim10 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell10.ExptID10 = char(all.RecTable{i,10});
            Data.Cell10.Exp10 = Data.Cell10.Exp10 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + Data.Cell9.Expts + 11
            Data.Cell10.Exp11 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell10.Stim11 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell10.ExptID11 = char(all.RecTable{i,10});
            Data.Cell10.Exp11 = Data.Cell10.Exp11 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + Data.Cell9.Expts + 12
            Data.Cell10.Exp12 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell10.Stim12 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell10.ExptID12 = char(all.RecTable{i,10});
            Data.Cell10.Exp12 = Data.Cell10.Exp12 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + Data.Cell9.Expts + 13
            Data.Cell10.Exp13 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell10.Stim13 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell10.ExptID13 = char(all.RecTable{i,10});
            Data.Cell10.Exp13 = Data.Cell10.Exp13 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + Data.Cell9.Expts + 14
            Data.Cell10.Exp14 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell10.Stim14 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell10.ExptID14 = char(all.RecTable{i,10});
            Data.Cell10.Exp14 = Data.Cell10.Exp14 * 1000;
        elseif i == Data.Cell1.Expts + Data.Cell2.Expts + Data.Cell3.Expts + Data.Cell4.Expts + Data.Cell5.Expts + Data.Cell6.Expts + Data.Cell7.Expts + Data.Cell8.Expts + Data.Cell9.Expts + 15
            Data.Cell10.Exp15 = cell2mat(all.RecTable.dataRaw{i,1});
            Data.Cell10.Stim15 = all.RecTable.stimWave{i,1}.DA_3;
            Data.Cell10.ExptID15 = char(all.RecTable{i,10});
            Data.Cell10.Exp15 = Data.Cell10.Exp15 * 1000;
        end
    end                    
end

save(filename,'Data','filename')