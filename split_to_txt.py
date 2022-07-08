import re
import numpy as np
import os
import sys

def clean_sentences(s):
    s = s.strip()
    s = re.sub('  +', ' ', s)
    s = s.replace('|', '।')
    s = re.sub(r'(?<![ ])[।?!]', r' \g<0>', s)
    s = re.sub(r'\s+(?=,)', r'', s)
    s = re.sub(r',(?! )', r', ', s)
    if not bool(re.search(r'[।?!]$', s)):
        s = ' '.join((s, '।'))
    return s

def sentotxtconverter(txtdirectory, inputfile):
    f = open(inputfile, "r", encoding="UTF-8")
    corpora = f.readlines()
    for sentence in corpora:
        try:
            sentence = sentence.replace('\n', '').split("\t")
            # sentence = clean_sentences(sentence)
            filename = sentence[0]
            # with filename concatenate the path of folder you want foles saved.
            f1 = open(txtdirectory + "/" + filename, "w", encoding="UTF-8")
            f1.write(clean_sentences(sentence[1]))
        except:
            pass


# this module is for creating a file of simple sentences.
def create_corpora_simple_sentences(inputfile, outputfile):
    f1 = open(outputfile, "w")  # enter the output file with path
    # Enter the input file here with path
    with open(inputfile, encoding="UTF-8") as f:
        for sentence in f:
            if is_simple_sentence(sentence):
                # sentence = clean_sentences(sentence)
                sentence.strip()
                f1.write(sentence)


def is_simple_sentence(sentence):

    connectives = ['कि', 'तथा', 'यद्यपि', 'और', 'मानो', 'परन्तु', 'जो', 'जिसे', 'जिसने ', 'जिसको', 'जिसका', 'जिसके', 'जिससे', 'जिसमें', 'जिनको', 'जिनके', 'जिनसे', 'जिनमें', 'जिन्हें', 'जिन्होंने', 'इसलिए', 'इसलिये', 'इसीलिये', 'क्योंकि', 'जैसे', 'किन्तु', 'एवं', 'यद्यपि', 'तथापि', 'भले ही', 'तो', 'अगर', 'मगर', 'अतः', 'चूंकि', 'चूँकि', 'जिस तरह', 'जिस प्रकार', 'लेकिन', 'जब', 'तब', 'तभी', 'या', 'जहाँ', 'वरना', 'अन्यथा', 'ताकि', 'बशर्तें', 'जैसे', 'जबकि', 'यदि', 'मानो', 'वरन', 'परंतु', 'किंतु', 'हालाँकि', 'हालांकि', 'जिस', 'जिन']

    if True in np.in1d(connectives, sentence.split(' ')):
        return False
    else:
        return True


if __name__ == "__main__":

    if len(sys.argv) != 2:
        raise ValueError('Format: split_to_txt.py [filename]')

    inputfile = sys.argv[1]
    outputfile = str.join('', ((inputfile.split('.')[0], '_output.txt')))
    txtdirectory = inputfile.split('.')[0]
    os.mkdir(txtdirectory)
    create_corpora_simple_sentences(inputfile, outputfile)
    sentotxtconverter(txtdirectory, outputfile)
