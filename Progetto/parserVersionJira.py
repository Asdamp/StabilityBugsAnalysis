import json
import re

class Version (object):
    def __init__(self, j):
        self.__dict__=json.loads(j)


#funzione che data la risposta in formato json alla richiesta GET /rest/api/2/project/{projectIdOrKey}/versions
# per ottenere tutte le versioni di un progetto su jira restituisce una lista di oggetti Version.
# Ogni oggetto versione ha un nome (es "3.1.3"), un self (l'url) e un id (valore numerico che identifica la versione)
def getAllVersions(response):
        allVersion=[]
        version= response.split("{")
        for item in version:
            item=item.replace("u'", "\"")
            item=item.replace("'", "\"")
            item="{"+item
            infoVersion=item.split(",")
            n_v=""
            url_v=""
            id_v=""
            for info in infoVersion:
                name= re.search("\"name\": \"([a-zA-Z0-9]*|\.| |-|\+|\(|\))*\"", info)
                url= re.search("\"self\": \"([a-zA-Z0-9]*|/|\.|:)*\"", info)
                id= re.search("\"id\": \"[0-9]*\"", info)
                if(name != None):
                    n_v =(name.group())
                if(url!= None):
                   url_v = (url.group())
                if(id!=None):
                   id_v=(id.group())
            if(not n_v.__eq__("")):
                j="{"+n_v+","+url_v+","+id_v+"}"
                v = Version(j)
                allVersion.append(v)
        return allVersion


#funzione che data la risposta in formato json alla richiesta GET /rest/api/2/version/{id}/relatedIssueCounts
# per ottenere tutte le issues di una certa versione stampa il numero di issues divisi in tre categorie
def parserNumIssue(response):
    info=response.split(",")
    print(response)
    fixed=""
    affected=""
    custom=""
    for item in info:
        issueFixed=re.search('\'issuesFixedCount\': [0-9]*',item)
        if issueFixed!=None:
            fixed=issueFixed.group().strip("'issuesFixedCount': ")
        issuesAffected=re.search('\'issuesAffectedCount\': [0-9]*',item)
        if issuesAffected!=None:
            affected=(issuesAffected.group().strip("\'issuesAffectedCount\': "))
        issueC= re.search('\'issueCountWithCustomFieldsShowingVersion\': [0-9]*',item)
        if issueC!=None:
            custom=(issueC.group().strip("'issueCountWithCustomFieldsShowingVersion': "))
    return [fixed, affected, custom]

#funzione che data la risposta in formato json alla richiesta GET /rest/api/2/version/{id}/unresolvedIssueCount
#restituisce il numero di issues unresolved
def parseUnresolvedIssue(response):
    info=response.split(",")
    print(response)
    unresolved=""
    for item in info:
        issueUnresolved = re.search('\'issuesUnresolvedCount\': [0-9]*', item)
        if issueUnresolved != None:
            unresolved = issueUnresolved.group().strip("\'issuesUnresolvedCount\':  ")
    return unresolved


