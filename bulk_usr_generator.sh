#!/bin/bash
inputDir=$1
numFiles=$(ls $inputDir | wc -l)
outputDir=${1}_output
mkdir $outputDir
i=1
for file in $inputDir/*
do
    filename0=$(basename "$file")
    filename=${filename0%.*}
    echo $filename
    cat $file>tmp.txt
    isc-parser -i tmp.txt > parser-output.txt
    echo "$file: Parsing completed."
    utf8_wx tmp.txt > wx.txt
    echo "$file: wx completed."
    python3 getMorphPruneAndNER3.py tmp.txt prune-output.txt
    echo "$file: Morph completed."
    g++ newdup_copy.cpp
    echo "$file: Compilation completed."
    ./a.out > oup.txt
    echo "$file: Execution completed."
    mv oup.txt ${outputDir}/"$filename.txt" #outputdirectory "create output directory in parent directory"
    echo "$file: Output written $i/$numFiles"
    i=$((i+1))
done 
