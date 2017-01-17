import os
import re

#funzione che data in ingresso una linea di un file .dot che presenta la stringa "Node"
#restituisce il nome della classe corrispondente a quel nodo
#il nome della classe è del tipo: 'package.package..package.Classe'
def  findNodoNome(line):
    # cerco tutte le stringhe che contengono Node e label
    result = re.search("Node[\S|\s]*\[label=", line)
    if (result != None):
        # faccio lo split di tutte le parole separate da spazio
        res = result.string.split()
        # res 1 contiene la parola con il nome del nodo, elimino i primi 8 caratteri ([label")
        nome = res[1][8:]
        # faccio lo split con le virgole per eliminare informazioni che non servono
        nome = nome.split(",")[0]
        # elimino l'ultimo carattere, ovvero le "
        nome = nome[:nome.__len__() - 1]
        #separo il nome del metodo, della classe e del package
        nome=nome.split(".")
        if (nome.__len__() > 3): #serve per elimnare dei nodi anomali es: ["if"]
            metodo= nome[nome.__len__()-1]
            classe= nome[nome.__len__()-2]
            nome.remove(metodo)
            nome.remove(classe)
            classe=classe.replace("\\l","")
            package=""
            for str in nome:
                str = str.replace("\\l", "")
                package+= str+"."
            nomeClasse=package+classe
            return [nomeClasse]
        else:
            return None

#funzione che dato in ingresso il path corrispondente alla directory contenente i file .dot
# restituisce una lista contenente i nomi di tutte le classi del progetto
def parse(path):
    #nel percorso indicato cerco tutti i file, in tutte le sottodirectory, con estensione .dot
    dotfiles=[os.path.join(root,name)
               for root, dirs, files in os.walk(path)
               for name in files
               if name.endswith(".dot")
              ]
    classi=[]
    #si parsa ogni file .dot
    for el in dotfiles:
        file=open(el, 'r')
        for line in file:
            result = re.search("Node", line)
            if (result != None):
                #cerco i nomi delle classi nei nodi utilizzando la funzione findNodoNome(line)
                classe= findNodoNome(line)
                #se trovo una classe e questa non è già stata inserita nella lista classi[] la inserisco
                if(classe!=None):
                    if(not classi.__contains__(classe)):
                        classi.insert(classi.__len__(),classe)
    return classi


#def print_classi(classi):
#    fNodi = open("ClassiPresuntaAltraVersione.csv", 'w')
#    fNodi.write("Classe\n")
#    print(classi.__len__())
#    for item in classi:
#        fNodi.write(item.__str__())
#        fNodi.write("\n")
#    fNodi.close()