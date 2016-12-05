import os
import re

def  findNodoNome(line):
    # cerco tutte le stringhe che contengono Node e label
    result = re.search("Node[\S|\s]*\[label=", line)
    if (result != None):
        # faccio lo split di tutte le parole separate da spazio
        res = result.string.split()
        nodo = res[0]
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


def parse(path):
    print(path)
    dotfiles=[os.path.join(root,name)
               for root, dirs, files in os.walk(path)
               for name in files
               if name.endswith(".dot")
              ]
    classi=[]

    for el in dotfiles:
        file=open(el, 'r')
        for line in file:
            result = re.search("Node", line)
            if (result != None):
                #cerco i nomi delle classi nei nodi
                classe= findNodoNome(line)
                if(classe!=None):
                    if(not classi.__contains__(classe)):
                        classi.insert(classi.__len__(),classe)
    print (len(classi))
    return classi

def print_classi(classi):
    fNodi = open("ClassiPresuntaAltraVersione.csv", 'w')
    fNodi.write("Classe\n")
    print(classi.__len__())
    for item in classi:
        fNodi.write(item.__str__())
        fNodi.write("\n")
    fNodi.close()


#print_classi(parse("C:\\Users\\Assunta\\Desktop\\JEDIT_prove_varie\\risultatiSoloJavaPresuntaAltraVersione"))

