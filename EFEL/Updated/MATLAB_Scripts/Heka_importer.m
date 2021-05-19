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

%Determine sampling frequency for each experiment type
timerow = 2;
Time(1,1) = 0;

freq = (1/20000)*1000; %This value must be set as the sampling frequency
for i = 1:120049
    Time(timerow,1) = 0 + freq;
    freq = freq + 0.05;
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
            Data.Cell2.Exp1 = Data.Cell2.Exp1 * 1000;
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
            Data.Cell2.Exp1 = Data.Cell2.Exp1 * 1000;
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
            Data.Cell2.Exp1 = Data.Cell2.Exp1 * 1000;
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
        end
    end
end

save(filename,'Data','filename')