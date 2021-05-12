from xml.dom.minidom import parse
import xml.dom.minidom
import re
import os
import matplotlib.pyplot as plt 

os.chdir("D:\IBI1\IBI1_2020-21\Practical14")
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")

DNAcount = 0
RNAcount = 0
proteincount = 0
chcount = 0
for term in terms:
    defstr = term.getElementsByTagName('defstr')[0]
    defs = defstr.childNodes[0].data
    if re.search('DNA',defs):
        DNAcount += 1
for term in terms:
    defstr = term.getElementsByTagName('defstr')[0]
    defs = defstr.childNodes[0].data
    if re.search('RNA',defs):
        RNAcount += 1
for term in terms:
    defstr = term.getElementsByTagName('defstr')[0]
    defs = defstr.childNodes[0].data
    if re.search('protein',defs):
        proteincount += 1
for term in terms:
    defstr = term.getElementsByTagName('defstr')[0]
    defs = defstr.childNodes[0].data
    if re.search('carbohydrate',defs):
        chcount += 1

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