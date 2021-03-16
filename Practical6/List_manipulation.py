import numpy as np
import matplotlib.pyplot as plt 

gene_len = []
exon_cot = []
aver = []
g = input("input gene lengths:")
g = list(g.split(','))
for i in range(len(g)):
    gene_len.append(int(g[i]))

e = input("input exon counts:")
e = list(e.split(','))
for i in range(len(e)):
    exon_cot.append(int(e[i]))
print(gene_len)
for i in range(len(gene_len)):
    aver.append(gene_len[i] / exon_cot[i])
print(aver)
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