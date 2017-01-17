import parserGetAllClasses
from itertools import chain

#funzione che fa il diff di due liste:
#restituisce tutti gli elementi ch sono presenti nella prima lista e non nella seconda
#nel caso specifico dei file di una versione:
#diff(classiVerPrec,classiVerSucc) restituisce il numero di classi eliminate
#diff(classiVerSucc,classiVerPrec) restituisce il numero di classi aggiunte
def diff(first, second):
    result=[item for item in first if item not in second]
    l = list(chain(*result))
    return len(l)


