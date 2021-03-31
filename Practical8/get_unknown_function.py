import sys
import os
import re

os.chdir("D:\IBI1\IBI1_2020-21\Practical8")
file1 = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
file2 = open('unknown_function.fa','w')
line = next(file1,'0')
while True:
    if line.startswith('>'):
        if re.search(r'unknown function',line):
            m = re.findall('gene:(\S+)',line)
            s = ''
            
            while True:
                line = next(file1,'0')
                if line.startswith('>') or (line == '0'):
                    break
                line1 = line.replace('\n','')
                s = s + line1 
            f = '>>'+m[0]
            file2.write(f'{f:14}')
            file2.write(str(int(len(s))))
            file2.write('\n')            
            file2.write(s)
            file2.write('\n')
        else:
            line = next(file1,'0')  
    else:
        line = next(file1,'0')  
    if line == '0':
        break
    
file1.close()
file2.close()

