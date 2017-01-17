import parserCountChiamateClassi

#funzione che date due liste restituisce tutti gli elementi presenti nella prima ma non nella seconda
def diffClassi(first, second):
    result=[item for item in first if item not in second]
    return len(result)

#funzione che dati in ingresso i percorsi delle directory contenenti i file .dot
#restituisce una array con: il numero di chiamate della versione 1,
# il numero di chiamate della versione 2, il numero di chiamate non piu' presenti, il numero di chiamate aggiunte
def getCoreCallsValues(path1, path2):
    calls1= parserCountChiamateClassi.getDotFiles(path1)
    calls2= parserCountChiamateClassi.getDotFiles(path2)
    old=diffClassi(calls1,calls2)
    new=diffClassi(calls2,calls1)
    return [len(calls1), len(calls2), old, new]
