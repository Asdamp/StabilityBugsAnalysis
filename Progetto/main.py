from openpyxl import load_workbook
from Progetto import parserGetAllClasses
from Progetto.diffClassiVersioni import diff
from Progetto.getClassiModificate import count_class_mod
from Progetto.request import getNumIssue
from Progetto.getCoreCallsInstabilityValues import getCoreCallsValues

#definizione delle variabili per indicare:
#nome del progetto e versioni di interesse
nomeCompleto="activemq-parent"
nomeProgetto="ActiveMQ"
numVerPrec="5.8.0"
numVerSucc="5.9.0"

#definizione dei percorsi delle directory da cui prelevare:
#i file del progetto e i file .dot generati da Doxygen
pathSourceVerPrec="C:\\eeqdsw\\source\\"+nomeCompleto+"-"+numVerPrec
pathSourceVerSucc="C:\\eeqdsw\\source\\"+nomeCompleto+"-"+numVerSucc
pathDotVerPrec="C:\\eeqdsw\\dot\\"+nomeCompleto+"-"+numVerPrec
pathDotVerSucc="C:\\eeqdsw\\dot\\"+nomeCompleto+"-"+numVerSucc
#definisco la prima parte dell'uri per fare le richieste a JIRA
uriProject="https://issues.apache.org/jira/rest/api/2/project/AMQ"

#invocazione dei metodi per ottenere i valori di interesse
classiVerPrec=parserGetAllClasses.parse(pathDotVerPrec)
classiVerSucc=parserGetAllClasses.parse(pathDotVerSucc)
numClassiEliminate=diff(classiVerPrec,classiVerSucc)
numClassiAggiunte=diff(classiVerSucc,classiVerPrec)
numClassiModificate=count_class_mod(pathSourceVerPrec,pathSourceVerSucc)
coreCallsInstabilityValues=getCoreCallsValues(pathDotVerPrec, pathDotVerSucc)
issues=getNumIssue(uriProject, numVerSucc)

#utilizzando la libreria openpyxl si riportano i risultati in un file .xlsx
wb=load_workbook("result.xlsx")
ws=wb.active
ws.append([nomeProgetto,numVerPrec,numVerSucc,len(classiVerPrec),len(classiVerSucc),numClassiEliminate,numClassiAggiunte,numClassiModificate,coreCallsInstabilityValues[0],coreCallsInstabilityValues[1],coreCallsInstabilityValues[2],coreCallsInstabilityValues[3],issues[0], issues[1],issues[2],issues[3]])
wb.save("result.xlsx")
