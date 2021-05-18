"""
Approach:
In this script, I use recursion to do the practical
Though I have done some preconditioning to make the search faster, 
it still needs several mins
***A faster version using graph theory is in the script called "settreetofindnodes.py"
"""
import re
from xml.dom.minidom import parse
import xml.dom.minidom
import os
import matplotlib.pyplot as plt 
#recursion to determine if there is a sequence in all the parent node defstr
#invoking itself with parent node
def find(j,term):
    is_a = []
    flag = False
    is_a = term.getElementsByTagName('is_a')
    if is_a == []:
        flag = False
    else:
        for a in is_a:
            parentid = a.childNodes[0].data
            s = re.findall(':(\d.*)$',parentid)
            digitid = int(s[0])
            fatherterm = terms[loc[digitid]]
            defstr = fatherterm.getElementsByTagName('defstr')[0]
            d = defstr.childNodes[0].data
            if re.search(j,d):
                flag = True
            elif find(j,fatherterm):
                flag = True
    return flag
#change working directory
os.chdir("D:\IBI1\IBI1_2020-21\Practical14")
go_obo = open('go_obo.xml','r')
DOMTree = xml.dom.minidom.parse('go_obo.xml')
collection = DOMTree.documentElement
terms = collection.getElementsByTagName('term')       
#initialization             
DNAcount = 0
RNAcount = 0
proteincount = 0
chcount = 0
i = 0
loc = [0]*10000000
for term in terms:
    termid = term.getElementsByTagName('id')[0].childNodes[0].data
    p = re.findall(':(\d.*)$',termid)
    q = int(p[0])
    loc[q] = i
    i = i+1
#the number of childNodes associated with DNA#
for term in terms:
    if find('DNA',term):
        DNAcount = DNAcount+1
#the number of childNodes associated with RNA#
for term in terms:
    if find('RNA',term):
        RNAcount = RNAcount+1
#the number of childNodes associated with protein#
for term in terms:
    if find('protein',term):
        proteincount = proteincount+1
#the number of childNodes associated with carbohydrate#
for term in terms:
    if find('carbohydrate',term):
        chcount = chcount+1
print('the number of childNodes associated with DNA: ',DNAcount)#8651
print('the number of childNodes associated with RNA: ',RNAcount)#11004
print('the number of childNodes associated with protein: ',proteincount)#33459
print('the number of childNodes associated with carbohydrate: ',chcount)#4879
#Draw the pie chart
labels = 'DNA-associated\n'+str(DNAcount),'RNA-associated\n'+str(RNAcount),'protein-associated\n'+str(proteincount),'carbohydrate-associated\n'+str(chcount)
sizes = [DNAcount,RNAcount,proteincount,chcount]
plt.pie(sizes, explode=None, labels=labels,
    colors=('b', 'g', 'r', 'c'),
    autopct='%1.2f%%', pctdistance=0.6, shadow=True,
    labeldistance=1.1, startangle=0, radius=1,
    counterclock=True, wedgeprops=None, textprops=None,
    center = (0, 0), frame = False )
plt.title('Child Nodes of Macromolecules in the Ontology')
plt.axis('equal')
plt.show()

