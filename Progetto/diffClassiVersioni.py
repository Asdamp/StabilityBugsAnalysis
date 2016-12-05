import parserGetAllClasses
from itertools import chain

def diff(first, second):
    return[item for item in first if item not in second]


result=diff(parserGetAllClasses.parse("C:\\Users\\Assunta\\Desktop\\JEDIT_prove_varie\\risultatiSoloJava\\html"), parserGetAllClasses.parse("C:\\Users\\Assunta\\Desktop\\JEDIT_prove_varie\\risultatiSoloJavaPresuntaAltraVersione"))
#result e' un insieme di tuple....lo si deve converitre in lista e si fa cosi'...
list=list(chain(*result))
print(len(list))
