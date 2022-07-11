import subprocess
import os
from usrtoexcelconv import conv_to_excel
from split_to_txt import *
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError('Format: split_to_txt.py [filename]')
    
    inputfile = sys.argv[1]
    outputfile = str.join('', ((inputfile.split('.')[0], '_output.txt')))
    txtdirectory = inputfile.split('.')[0]
    os.mkdir(txtdirectory)
    create_corpora_simple_sentences(inputfile)
    sentotxtconverter(txtdirectory, outputfile)

    bashCommand = f'sh bulk_usr_generator.sh {txtdirectory}'
    subprocess.call(bashCommand, shell=True)

    outputDirName = '_'.join((txtdirectory, 'output'))
    conv_to_excel(outputDirName)