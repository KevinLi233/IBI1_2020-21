# Import libraries
import numpy as np
import matplotlib.pyplot as plt 

# List initialization
# Input gene lengths
gene_len = [9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
# Input exon counts
exon_cot = [51,1142,42,216,25,650,32533,57,1,523]
aver = []
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
plt.title("Boxplot of Average Exon Length")
plt.show()