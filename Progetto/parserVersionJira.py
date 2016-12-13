#input json response getAllVersions
import json
import re

class Version (object):
    def __init__(self, j):
        self.__dict__=json.loads(j)


#funzione che data la risposta in formato json alla richiesta get per ottenere tutte le versioni di un progetto su jira restituisce
# una lista di versioni. ogni oggetto versione ha un nome (es "3.1.3"), un self (l'url) e un id (valore numerico che identifica la versione)
def getAllVersions(response):
        allVersion=[]
        #for line in response:
         #   print("*****"+line)
        version= response.split("{")
        #version.remove("")
        for item in version:
            item=item.replace("u'", "\"")
            item=item.replace("'", "\"")
            item="{"+item
            #print(item)
            infoVersion=item.split(",")
            n_v=""
            url_v=""
            id_v=""
            for info in infoVersion:
                name= re.search("\"name\": \"([a-zA-Z0-9]*|\.| |-|\+|\(|\))*\"", info)
                url= re.search("\"self\": \"([a-zA-Z0-9]*|/|\.|:)*\"", info)
                id= re.search("\"id\": \"[0-9]*\"", info)
                if(name != None):
                   # print(n_v)
                    n_v =(name.group())
                if(url!= None):
                   #print(url_v)
                   url_v = (url.group())
                if(id!=None):
                   #print(id_v)
                   id_v=(id.group())
            #print(n_v + "," + url_v + "," + id_v)
            if(not n_v.__eq__("")):
                j="{"+n_v+","+url_v+","+id_v+"}"
                v = Version(j)
                allVersion.append(v)
        #for v in allVersion:
         #   print(v.name+"\t"+v.self+"\t"+v.id)
        return allVersion


#funzione che data la risposta in formato json alla richiesta get per ottenere tutti i bug di una certa versione
#stampa il numero di bug divisi in tre categorie
def parserNumIssue(response):
    info=response.split(",")
    for item in info:
        issueFixed=re.search('\'issuesFixedCount\': [0-9]*',item)
        if issueFixed!=None:
            print(issueFixed.group())
        issuesAffected=re.search('\'issuesAffectedCount\': [0-9]*',item)
        if issuesAffected!=None:
            print(issuesAffected.group())
        issueC= re.search('\'issueCountWithCustomFieldsShowingVersion\': [0-9]*',item)
        if issueC!=None:
            print(issueC.group())

#parserNumIssue("{u'self': u'https://hibernate.atlassian.net/rest/api/2/version/26103', u'issuesFixedCount': 18, u'issuesAffectedCount': 0, u'issueCountWithCustomFieldsShowingVersion': 0}")


