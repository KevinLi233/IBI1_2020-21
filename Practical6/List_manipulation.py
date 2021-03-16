# Import libraries
import numpy as np
import matplotlib.pyplot as plt 

# List initialization
gene_len = []
exon_cot = []
aver = []
# Input gene lengths
# Input data as a string
g = input("input gene lengths:")
# split the string into a list
g = list(g.split(','))
# convert data types
for i in range(len(g)):
    gene_len.append(int(g[i]))
# Input exon counts
# Input data as a string
e = input("input exon counts:")
# split the string into a list
e = list(e.split(','))
# convert data types
for i in range(len(e)):
    exon_cot.append(int(e[i]))
# get average exon length of each gene
for i in range(len(gene_len)):
    aver.append(gene_len[i] / exon_cot[i])
# sort values for the average
aver = sorted(aver)
# print the sorted values for the average exon length
print("sorted values for the average exon length:",aver)
# make a boxplot
plt.boxplot(
    aver,
    vert = True,
    whis = 1.5,
    patch_artist = True,
    meanline = False,
    showbox = True,
    showcaps = True,
    showfliers = True,
    notch = False
    )
plt.show()