import re
from xml.dom.minidom import parse
import xml.dom.minidom
import os
import matplotlib.pyplot as plt 

def findDNA(j,term):
    is_a=[]
    is_a=term.getElementsByTagName('is_a')
    if is_a ==[]:
        return False
    else:
        for a in is_a:
            parentid=a.childNodes[0].data
            s=re.findall(':(\d.*)$',parentid)
            digitid=int(s[0])
            fatherterm=terms[loc[digitid]]
            defstr=fatherterm.getElementsByTagName('defstr')[0]
            d=defstr.childNodes[0].data
            if re.search(j,d):
                return True
            elif findDNA(j,fatherterm):
                return True
            else:
                return False
os.chdir("D:\IBI1\IBI1_2020-21\Practical14")
go_obo = open('go_obo.xml','r')
DOMTree = xml.dom.minidom.parse('go_obo.xml')
collection = DOMTree.documentElement
terms = collection.getElementsByTagName('term')                    
DNAcount=0
RNAcount=0
proteincount=0
chcount=0
i=0
loc=[0]*10000000
for term in terms:
    termid=term.getElementsByTagName('id')[0].childNodes[0].data
    p=re.findall(':(\d.*)$',termid)
    q=int(p[0])
    loc[q]=i
    i=i+1
#the number of childNodes associated with DNA#
for term in terms:
    if findDNA('DNA',term):
        DNAcount = DNAcount+1
#the number of childNodes associated with RNA#
for term in terms:
    if findDNA('RNA',term):
        RNAcount = RNAcount+1
#the number of childNodes associated with protein#
for term in terms:
    if findDNA('protein',term):
        proteincount = proteincount+1
#the number of childNodes associated with carbohydrate#
for term in terms:
    if findDNA('carbohydrate',term):
        chcount = chcount+1
print('the number of childNodes associated with DNA: ',DNAcount)
print('the number of childNodes associated with RNA: ',RNAcount)
print('the number of childNodes associated with protein: ',proteincount)
print('the number of childNodes associated with carbohydrate: ',chcount)
labels = 'DNA-associated','RNA-associated','protein-associated','carbohydrate-associated'
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

