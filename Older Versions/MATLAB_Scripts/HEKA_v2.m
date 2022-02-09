clear;
clc;
[path] = uigetdir;
cd(path);

file = uigetfile;
filename = file(1:end-4);
HEKA_Importer(file)

CellNum = 0;
C1Expts = 0;
C2Expts = 0;
C3Expts = 0;
IterVar = 1;
timerow = 2;
Time(1,1) = 0;
TraceLength = size(ans.RecTable.dataRaw{1,1}{1:end});

%Calculation of time constant (Sampling frequency of 20kHz or 0.05 per
%sampling point)
freq = (1/20000)*1000; %This value must be set as the sampling frequency
for i = 1:TraceLength(1,1)-1
    Time(timerow,1) = 0 + freq;
    freq = freq + 0.05;
    timerow = timerow + 1;
end

%Determines the number of cells and the number of experiments per cell
for i = 1:height(ans.RecTable)
    if ans.RecTable{IterVar,1} == 1 && strcmp(ans.RecTable{IterVar,2}, 'Exp-1')
        CellNum = 1;
        C1Expts = C1Expts + 1;
    elseif ans.RecTable{IterVar,1} == 2 && strcmp(ans.RecTable{IterVar,2}, 'Exp-2')
        CellNum = 2;
        C2Expts = C2Expts + 1;
    elseif ans.RecTable{IterVar,1} == 3 && strcmp(ans.RecTable{IterVar,3}, 'Exp-3')
        CellNum = 3;
        C3Expts = C3Expts + 1;
    else
    end
    IterVar = IterVar + 1;
end

%Depending upon the number of cells, segregate all traces of each
%experiment into a single array

%This will be used to separate each experiment into a separate list using
%the Python script
if CellNum == 1
    start = 1;
    ends = 11;
    x = 1;
    for i = 1:C1Expts
        C1data(:,start:ends) = cell2mat(ans.RecTable.dataRaw{x,1});
        start = start + 11;
        ends = ends + 11;
        x = x + 1;
    C1data = C1data * 1000;
    end
    
elseif CellNum == 2
    start = 1;
    ends = 11;
    x = 1;
    for i = 1:C1Expts
        C1data(:,start:ends) = cell2mat(ans.RecTable.dataRaw{x,1});
        start = start + 11;
        ends = ends + 11;
        x = x + 1;
    end
    start = 1;
    ends = 11;
    x = 1;
    for i = 1:C2Expts
        C2data(:,start:ends) = cell2mat(ans.RecTable.dataRaw{x,1});
        start = start + 11;
        ends = ends + 11;
        x = x + 1;
    end
    C1data = C1data * 1000;
    C2data = C2data * 1000;

elseif CellNum == 3
    start = 1;
    ends = 11;
    x = 1;
    for i = 1:C1Expts
        C1data(:,start:ends) = cell2mat(ans.RecTable.dataRaw{x,1});
        start = start + 11;
        ends = ends + 11;
        x = x + 1;
    end
    start = 1;
    ends = 11;
    x = 1;
    for i = 1:C2Expts
        C2data(:,start:ends) = cell2mat(ans.RecTable.dataRaw{x,1});
        start = start + 11;
        ends = ends + 11;
        x = x + 1;
    end
    start = 1;
    ends = 11;
    x = 1;
    for i = 1:C3Expts
        C3data(:,start:ends) = cell2mat(ans.RecTable.dataRaw{x,1});
        start = start + 11;
        ends = ends + 11;
        x = x + 1;
    end
    C1data = C1data * 1000;
    C2data = C2data * 1000;
    C3data = C3data * 1000;
end
    


%Save data according to the cell number with the appropriate
%data/measurements
if CellNum == 1
    save(filename,'CellNum','Time','C1data','C1Expts')
elseif CellNum == 2
    save(filename,'CellNum','Time','C1data','C1Expts','C2data','C2Expts')
elseif CellNum == 3
    save(filename,'CellNum','Time','C1data','C1Expts','C2data','C2Expts','C3data','C3Expts')
end
