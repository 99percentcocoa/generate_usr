#!/bin/bash
isc-parser -i $1 > parser-output.txt
utf8_wx $1 > wx.txt


python3 getMorphPruneAndNER3.py $1 prune-output.txt
g++ newdup_copy.cpp
./a.out > oup.txt