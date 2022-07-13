import subprocess
import os
from usrtoexcelconv import conv_to_excel
from split_to_txt import *
import sys
from datetime import datetime
import csv

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError('Format: split_to_txt.py [filename]')
    
    inputfile = sys.argv[1]
    outputfile = str.join('', ((inputfile.split('.')[0], '_output.txt')))
    txtdirectory = inputfile.split('.')[0]
    os.mkdir(txtdirectory)
    create_corpora_simple_sentences(inputfile, outputfile)
    sentotxtconverter(txtdirectory, outputfile)

    bashCommand = f'sh bulk_usr_generator.sh {txtdirectory}'
    subprocess.call(bashCommand, shell=True)

    outputDirName = '_'.join((txtdirectory, 'output'))
    conv_to_excel(outputDirName)

    # logging
    logfileName = "USR_Generation_Log.tsv"
    for filename in os.listdir(outputDirName):
        f = os.path.join(outputDirName, filename)
        if os.path.isfile(f):
            with open(logfileName, 'a') as fp:
                writer = csv.writer(fp, delimiter='\t')
                writer.writerow([filename, open(f, 'r').readline(), datetime.now().strftime("%d/%m/%Y %H:%M:%S")])