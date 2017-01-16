import openpyxl
from openpyxl import Workbook
from openpyxl import load_workbook

from Progetto import parserGetAllClasses
from Progetto.diffClassiVersioni import diff
from Progetto.diff_file import count_class_mod
from Progetto.request import getNumIssue
from Progetto.getCoreCallsInstabilityValues import getCoreCallsValues

numVerPrec="5.8.0"
numVerSucc="5.9.0"
#numVerSuccI="3.2.1"
nomeCompleto="activemq-parent"
nomeProgetto="ActiveMQ"

pathSourceVerPrec="C:\\eeqdsw\\source\\"+nomeCompleto+"-"+numVerPrec
pathSourceVerSucc="C:\\eeqdsw\\source\\"+nomeCompleto+"-"+numVerSucc
pathDotVerPrec="C:\\eeqdsw\\dot\\"+nomeCompleto+"-"+numVerPrec
pathDotVerSucc="C:\\eeqdsw\\dot\\"+nomeCompleto+"-"+numVerSucc
uriProject="https://issues.apache.org/jira/rest/api/2/project/AMQ" #esempio (per ogni progetto dobbiamo trovare che valore mettere al posto di HHH)


classiVerPrec=parserGetAllClasses.parse(pathDotVerPrec)
classiVerSucc=parserGetAllClasses.parse(pathDotVerSucc)
numClassiEliminate=diff(classiVerPrec,classiVerSucc)
numClassiAggiunte=diff(classiVerSucc,classiVerPrec)
numClassiModificate=count_class_mod(pathSourceVerPrec,pathSourceVerSucc)
coreCallsInstabilityValues=getCoreCallsValues(pathDotVerPrec, pathDotVerSucc)
issues=getNumIssue(uriProject, numVerSucc)
#issue e' un array di 4 elementi
wb=load_workbook("result.xlsx")

ws=wb.active

ws.append([nomeProgetto,numVerPrec,numVerSucc,len(classiVerPrec),len(classiVerSucc),numClassiEliminate,numClassiAggiunte,numClassiModificate,coreCallsInstabilityValues[0],coreCallsInstabilityValues[1],coreCallsInstabilityValues[2],coreCallsInstabilityValues[3],issues[0], issues[1],issues[2],issues[3]])

wb.save("result.xlsx")
