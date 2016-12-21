import requests
import parserVersionJira
def getNumIssue(projectName,versionName):
    url=""
    #mi resituisce tutte le versioni per quel progetto mi serve trovare l'id corrispondente per una cera versione
    r = requests.get(projectName+'/versions')
    for v in parserVersionJira.getAllVersions(str(r.json())):
        if v.name==versionName:
           print(v.name+"\t"+v.self+"\t"+v.id)
           url=v.self

    #una volta trovato l'id o l'url completa dal getversions richiedo tutte le issue relative a quella versione
    r = requests.get(url+"/relatedIssueCounts")
    result=parserVersionJira.parserNumIssue(str(r.json()))
    print(result)
    #result e' un array contenente il numero di issue chisue le issue affected e quele with custom fied

    #faccio una nuova richiesta per ottenere tutte le issue unresolved per quella versione
    r = requests.get(url + "/unresolvedIssueCount")
    unresolved=parserVersionJira.parseUnresolvedIssue(str(r.json()))
    print(unresolved)
    result.append(unresolved)
    return(result)

#print(getNumIssue("https://hibernate.atlassian.net/rest/api/2/project/HHH","5.2.5"))

