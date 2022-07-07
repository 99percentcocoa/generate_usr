import json
import requests
import sys
import os

from argparse import ArgumentParser

morphURL = "https://ssmt.iiit.ac.in/samparkuniverse"

def getMorph(file):

    line = open(file, 'r').readline().strip()

    reqData = {"text": line, "source_language": "hin", "target_language": "urd", "start": 1, "end": 9}
    header = {"Content-Type": "application/json;charset=UTF-8"}
    res = requests.post(morphURL, data=json.dumps(reqData), headers=header)
    morphOutput = json.loads(res.text)
    # logging.debug(morphOutput)
    # returns a DICT containing morphOut, pruneOut and nerOut
    morphOut = morphOutput["modular_outputs"]["morph-3"]
    pruneOut = morphOutput["modular_outputs"]["pickonemorph-6"]
    nerOut = morphOutput["modular_outputs"]["ner-9"]

    temp = "Sentence :: " + line + "\nMorph Output:\n" + morphOut.strip() + "\n Pruning Output:\n" + pruneOut.strip() + "\nNER Output:\n" + nerOut + "\n..................................\n"

    return temp

if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise ValueError('Format: python3 getMorphPruneAndNER3.py [inputFileName] [outputFileName]')
    
    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]

    outputFile = open(outputFileName, 'w')
    outputFile.write(getMorph(inputFileName))