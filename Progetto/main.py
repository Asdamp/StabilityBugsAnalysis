import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook

from Progetto import parserGetAllClasses
from Progetto.diffClassiVersioni import diff
from Progetto.diff_file import count_class_mod
from Progetto.request import getNumIssue
from Progetto.getCoreCallsInstabilityValues import getCoreCallsValues

pathSourceVerPrec="C:\\Users\\Antonio\\Desktop\\t\\wildfly-9.0.1.Final"
pathSourceVerSucc="C:\\Users\\Antonio\\Desktop\\t\\wildfly-10.1.0.Final"
pathDotVerPrec="C:\\Users\\Antonio\\Desktop\\t\\wildfly9"
pathDotVerSucc="C:\\Users\\Antonio\\Desktop\\t\\wildfly10"
uriProject="https://hibernate.atlassian.net/rest/api/2/project/HHH" #esempio (per ogni progetto dobbiamo trovare che valore mettere al posto di HHH)
numVerPrec="9.0.1"
numVerSucc="10.1.0"
nomeProgetto="wildfly"

classiVerPrec=parserGetAllClasses.parse(pathDotVerPrec)
classiVerSucc=parserGetAllClasses.parse(pathDotVerSucc)
numClassiEliminate=diff(classiVerPrec,classiVerSucc)
numClassiAggiunte=diff(classiVerSucc,classiVerPrec)
numClassiModificate=count_class_mod(pathSourceVerPrec,pathSourceVerSucc)
coreCallsInstabilityValues=getCoreCallsValues(pathDotVerPrec, pathDotVerSucc)
#coreCallsInstabilityValues è un array di 4 elementi:
#numero chiamate versionePrec; numero chiamate versioneSucc, chiamateRimosse, chimateAggiunte
issues=getNumIssue(uriProject, numVerPrec)
#issue e' un array di 4 elementi
wb=load_workbook("result.xlsx")

ws=wb.active

ws.append([nomeProgetto,numVerPrec,numVerSucc,len(classiVerPrec),len(classiVerSucc),numClassiEliminate,numClassiAggiunte,numClassiModificate])
for item in coreCallsInstabilityValues:
    ws.append(item)
for item in issues:
    ws.append(item)

wb.save("result.xlsx")
