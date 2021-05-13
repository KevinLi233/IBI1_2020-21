from xml.dom.minidom import parse
import xml.dom.minidom
import re
import os
import matplotlib.pyplot as plt 

labels = 'DNA-associated','RNA-associated','protein-associated','carbohydrate-associated'
sizes = [7977,10373,31296,2558]
plt.pie(sizes, explode=None, labels=labels,
    colors=('b', 'g', 'r', 'c'),
    autopct='%1.2f%%', pctdistance=0.6, shadow=True,
    labeldistance=1.1, startangle=0, radius=1,
    counterclock=True, wedgeprops=None, textprops=None,
    center = (0, 0), frame = False )
plt.title('Child Nodes of Macromolecules in the Ontology')
plt.axis('equal')
plt.show()