import os
import re


def printParsedDot(nodeToPackage, assNodes):
    file = open("parsedJedit5_3.txt", 'a')
    for pair in assNodes:
        file.write(nodeToPackage[pair[0]])
        file.write("\t|\t")
        file.write(nodeToPackage[pair[1]])
        file.write("\n")

def getChiamate(nodoChiamaList,nodeToPackage,assNodes):
    for pair in assNodes:
       item=[nodeToPackage[pair[0]],nodeToPackage[pair[1]]]
       if(not nodoChiamaList.__contains__(item)):
        nodoChiamaList=nodoChiamaList+[item]
    return nodoChiamaList

def getDotFiles(path):
    dotFiles = [os.path.join(root, name)
                for root, dirs, files in os.walk(path)
                for name in files
                if name.endswith(".dot") and  not name.__contains__("graph_legend")
                ]
    nodoChiamaList=[]
    for el in dotFiles:
        nodeToPackage = {}
        assNodes = []
        file = open(el, 'r')
        for line in file:
            packageName = re.search("label=\"(\w+\.)*", line)
            if packageName:
                methodName = re.search('\\l\w+(\.\w+)*"', line)
                nodeName = re.search("Node\d+", line)
                packageName = packageName.group().lstrip("label=\"").rstrip(".")
                methodName = methodName.group().lstrip('l').rstrip("\"")
                classe= packageName+"."+ methodName.split(".")[0]
                nodeToPackage[nodeName.group()] = classe
            else:
                tmp=re.findall("Node\d+", line)
                if tmp:
                    assNodes.append(tmp)
        nodoChiamaList=getChiamate(nodoChiamaList,nodeToPackage,assNodes)
        printParsedDot(nodeToPackage, assNodes)
    for item in nodoChiamaList:
       print(item)
    return nodoChiamaList

list= getDotFiles("C:\\Users\\Assunta\\Desktop\\esercitazioneEQS\\Doxygen\\results\\html")
print(len(list))