import os
import sys
import pandas as pd

def conv_to_excel(dirname):
    newdirName = '_'.join((dirname, 'excel'))
    os.mkdir(newdirName)
    for filename in os.listdir(dirname): #enter the directory where the txt-USRs are stored
        f=open(os.path.join(dirname,filename),'r',encoding="UTF-8")
        print(f'At file {filename}.')
        lines = []
        for line in f.readlines():
            lines.append(line.strip())
        print(lines)
        if len(lines) < 10:
            continue
        usrCommas = list(map(lambda x: x.split(','), lines[1:9]))
        print(usrCommas)
        df = pd.DataFrame(data=usrCommas)
        usrdf = pd.DataFrame(data=[lines[0]]).append(df).reset_index().drop(columns='index').append(pd.Series(lines[9]), ignore_index=True).fillna('')
        usrdf.to_excel(newdirName+"/"+filename[:-4]+".xlsx",header=None,index=None)

# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         raise ValueError('Format: python3 usrtoexcelconv.py [DirectoryName]')
    
#     dirname = sys.argv[1]
    
#     conv_to_excel(dirname)