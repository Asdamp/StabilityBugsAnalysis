import requests
import parserVersionJira

#funzione che preso in ingresso l'url del progetto e il nome della versione di interesse
#restituisce result, una lista di 4 valori contenenti:
# numero di issueFixed, numero di issueAffected, numero di issueWithCustomFields e numero di issueUnresolved
def getNumIssue(projectName,versionName):
    url=projectName
    #richiesta GET per ottenere tutte le versioni
    r = requests.get(projectName+'/versions')
    #ottengo tutte le versioni e cerco quella corrispondente a quella richiesta
    #di questa prendo il campo self, ovvero l'url specifica per quella versione
    for v in parserVersionJira.getAllVersions(str(r.json())):
        if v.name==versionName:
           url=v.self
    #utilizzando l'url ottenuta dalla ricerca precedente si esegue una nuova richiesta get per ottenere le relatedIssue
    r = requests.get(url+"/relatedIssueCounts")
    result=parserVersionJira.parserNumIssue(str(r.json())) #result=[issueFixed, issueAffected, issueWithCustomFileds]
    #si esegue una nuova richiesta per ottenere tutte le issue unresolved per quella versione
    r = requests.get(url + "/unresolvedIssueCount")
    unresolved=parserVersionJira.parseUnresolvedIssue(str(r.json()))
    result.append(unresolved) #result=[issueFixed, issueAffected, issueWithCustomFileds, issueUnresolved]
    return(result)

