import parserGetAllClasses
from itertools import chain

def diff(first, second):
    result=[item for item in first if item not in second]
    l = list(chain(*result))
    return len(l)

#result=diff(parserGetAllClasses.parse("C:\\Users\\Antonio\\Desktop\\t\\wildfly9"), parserGetAllClasses.parse("C:\\Users\\Antonio\\Desktop\\t\\wildfly10"))
#print(result)
