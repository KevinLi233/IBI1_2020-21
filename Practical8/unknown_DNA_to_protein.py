import sys
import os
import re


def encode(seq):
    ans = ''
    for i in range(0,len(seq),3):
        ans = ans + code[seq[i:i+3]]
    return ans

os.chdir("D:\IBI1\IBI1_2020-21\Practical8")
code = {
    "TTT":'F',"TTC":'F',"TTA":'L',"TTG":'L',
    "TCT":'S',"TCC":'S',"TCA":'S',"TCG":'S',
    "TAT":'Y',"TAC":'Y',"TAA":'O',"TAG":'U',
    "TGT":'C',"TGC":'C',"TGA":'X',"TGG":'W',
    "CTT":'L',"CTC":'L',"CTA":'L',"CTG":'L',
    "CCT":'P',"CCC":'P',"CCA":'P',"CCG":'P',
    "CAT":'H',"CAC":'H',"CAA":'Q',"CAG":'Z',
    "CGT":'R',"CGC":'R',"CGA":'R',"CGG":'R',
    "ATT":'I',"ATC":'I',"ATA":'J',"ATG":'M',
    "ACT":'T',"ACC":'T',"ACA":'T',"ACG":'T',
    "AAT":'N',"AAC":'B',"AAA":'K',"AAG":'K',
    "AGT":'S',"AGC":'S',"AGA":'R',"AGG":'R',
    "GTT":'V',"GTC":'V',"GTA":'V',"GTG":'V',
    "GCT":'A',"GCC":'A',"GCA":'A',"GCG":'A',
    "GAT":'D',"GAC":'D',"GAA":'E',"GAG":'E',
    "GGT":'G',"GGC":'G',"GGA":'G',"GGG":'G',
}
name = input('Please input the filename: ')
file1 = open('unknown_function.fa','r')
file2 = open(name,'w')

line = next(file1,'0')
while True:
    if line.startswith('>>'):
        m = line

        line = next(file1,'0')
        s = line.replace('\n','')
        
        f = m[0:14] + str(int(len(s)/3))
        file2.write(f)
        file2.write('\n')
        file2.write(encode(s))
        file2.write('\n')
            
    if line == '0':
        break
    line = next(file1,'0')
file1.close()
file2.close()