import openpyxl
from openpyxl import Workbook

from Progetto import parserGetAllClasses
from Progetto.diffClassiVersioni import diff
from Progetto.diff_file import count_class_mod

pathSourceVerPrec="C:\\Users\\Antonio\\Desktop\\t\\wildfly-9.0.1.Final"
pathSourceVerSucc="C:\\Users\\Antonio\\Desktop\\t\\wildfly-10.1.0.Final"
pathDotVerPrec="C:\\Users\\Antonio\\Desktop\\t\\wildfly9"
pathDotVerSucc="C:\\Users\\Antonio\\Desktop\\t\\wildfly10"
#uriProject=
numVerPrec="9.0.1"
numVerSucc="10.1.0"
nomeProgetto="wildfly"

classiVerPrec=parserGetAllClasses.parse(pathDotVerPrec)
classiVerSucc=parserGetAllClasses.parse(pathDotVerSucc)
numClassiEliminate=diff(classiVerPrec,classiVerSucc)
numClassiAggiunte=diff(classiVerSucc,classiVerPrec)
numClassiModificate=count_class_mod(pathSourceVerPrec,pathSourceVerSucc)

wb=Workbook()

ws=wb.active

ws.append([nomeProgetto,numVerPrec,numVerSucc,len(classiVerPrec),len(classiVerSucc),numClassiEliminate,numClassiAggiunte,numClassiModificate])

wb.save("result.xlsx")
