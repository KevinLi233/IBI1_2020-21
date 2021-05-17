
"""
Approach:
In this script, I establish connections a tree to speed up the search
it only needs several seconds, faster than Normal recursion.
"""

from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
import numpy as np

def parse_xml(path):
    DOMTree = xml.dom.minidom.parse(path)
    collection = DOMTree.documentElement
    terms = collection.getElementsByTagName("term")
    return terms

# 2 classes: Vertex & Graph for faster search
# can be learned from internet
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' \
               + str([x.id for x in self.connectedTo])

    def getConnection(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, item):
        return item in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[t].addNeighbor(self.vertList[f], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

def plantTree(terms):
    tree = Graph()
    for term in terms:
        id = term.getElementsByTagName("id")[0].childNodes[0].data
        is_a = term.getElementsByTagName("is_a")
        for fid in is_a:
            tree.addEdge(id,fid.childNodes[0].data)
    return tree

def getfather(terms, Specific_sequence):
    molecule_related = []
    for term in terms:
        defstr_text = term.getElementsByTagName("defstr")[0].childNodes[0].data
        if Specific_sequence in defstr_text:
            molecule_related.append(term)
    return molecule_related

def getAllChildren(tree, vertices):
    allChildren = []
    for v in vertices:
        if v:
            children = [i for i in v.connectedTo]
            allChildren += children
            allChildren += getAllChildren(tree, children)
    return allChildren

def countchild(tree, Specific_sequence):
    count = 0
    fatherlist = getfather(terms, Specific_sequence)
    childlist = [tree.getVertex(fid.getElementsByTagName("id")[0].childNodes[0].data) for fid in fatherlist]
    count = len(list(set(getAllChildren(tree, childlist))))
    return count

terms = parse_xml("D:\IBI1\IBI1_2020-21\Practical14\go_obo.xml")
tree = plantTree(terms)

DNAcount = countchild(tree, "DNA")  # 8651
RNAcount = countchild(tree, "RNA")  # 11004
proteincount = countchild(tree, "protein")  # 33459
chcount = countchild(tree, "carbohydrate")  # 4879
#the number of childNodes associated with DNA#
print('the number of childNodes associated with DNA: ',DNAcount)
#the number of childNodes associated with RNA#
print('the number of childNodes associated with RNA: ',RNAcount)
#the number of childNodes associated with protein#
print('the number of childNodes associated with protein: ',proteincount)
#the number of childNodes associated with carbohydrate#
print('the number of childNodes associated with carbohydrate: ',chcount)

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