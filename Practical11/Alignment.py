import os
import sys
import re
import numpy
#get edit distance between two sequences
def edit_dis(se1,se2):
    edit_distance = 0
    for	i in range(len(se1)):
        if	se1[i]==se2[i]:
            edit_distance += 1
    return edit_distance/len(se1)*100
def getscore(se1,se2):
    fin = 0
    for i in range(len(se1)):
        fin += score[(se2[i],se1[i])]
    return fin
#Change working directory
os.chdir("D:\IBI1\IBI1_2020-21\Practical11")

BLOSUM62 = {}
#input files and open output file
fileblo = open('BLOSUM62.txt','r')
file1 = open("SOD2_human.fa",'r')
file2 = open("SOD2_mouse.fa",'r')
s = fileblo.read()
s1 = file1.read()
s2 = file2.read()
did = re.findall(' (\S+)',s)
humanseq = re.findall('\n(\w+)',s1)
mouseseq = re.findall('\n(\w+)',s2)
seq3 = 'WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL'
seq1 = humanseq[0]
seq2 = mouseseq[0]
#get BLOSUM62 table into dictionary
score = {}
for i in range(24):
    for j in range(24):
        tem = {(did[i],did[j]):int(did[(i+1)*24+j])}
        score.update(tem)


fin = 0

print('SOD2_human: ',seq1)
print('SOD2_mouse: ',seq2)
print('alignment score: ',getscore(seq1,seq2))
print("percentage of identical amino acids: %.2f%%" % edit_dis(seq1,seq2))

print('SOD2_human: ',seq1)
print('random    : ',seq3)
print('alignment score: ',getscore(seq1,seq3))
print("percentage of identical amino acids: %.2f%%" % edit_dis(seq1,seq3))

print('SOD2_mouse: ',seq2)
print('random    : ',seq3)
print('alignment score: ',getscore(seq2,seq3))
print("percentage of identical amino acids: %.2f%%" % edit_dis(seq2,seq3))
#close files
fileblo.close()
file1.close()
file2.close()