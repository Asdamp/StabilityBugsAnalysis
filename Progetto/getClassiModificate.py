from filecmp import dircmp
import os

#funzione che dati in ingresso due percorsi restituisce il numero di classi differenti
def count_class_mod(path, path2):
    #prendo tutti i file che NON sono di interesse della versione1
    excludedFile1 = [os.path.join(root, name)
                    for root, dirs, files in os.walk(path)
                    for name in files
                    if not name.endswith(".java")
                    ]
    #prendo tutti i file che NON sono di interesse della versione 2
    excludedFile2 = [os.path.join(root, name)
                     for root, dirs, files in os.walk(path2)
                     for name in files
                     if not name.endswith(".java")
                     ]
    #elimino il pecorso, prelevando solo il nome dei file
    list1=[]
    list2=[]
    for file in excludedFile1:
        list1.append(file.split("\\")[-1])
    for file in excludedFile2:
        list2.append((file.split("\\"))[-1])
    #metto insieme i file dei due percorsi, evitando ripetizioni
    set1=set(list1)
    set2=set(list2)
    in_2_not_in_1=set2-set1
    excludedFile=list1+list(in_2_not_in_1)
    str=[]
    #concateno tutti i file trovati che non sono di interesse per metterli nel ignore di dircmp
    for file in excludedFile:
        str.append(file)

    #si utilizza la funzione di libreria per fare la comparazione, ignorando i file che non sono di progetto
    #precedentemente selezionati e presenti in str
    dcmp = dircmp(path,path2, ignore=str)
    #invoco la funzione redircmp per realizzare il confronto file in tutte le sottodirectory
    # e restituire il numero di file che differiscono
    return recdircmp(dcmp)

#funzione che ricorsivamente confronta i file nelle sottodirectory
def recdircmp(dcmp):
    len=0
    for sub_dcmp in dcmp.subdirs.values():
        len+=recdircmp(sub_dcmp)
    return dcmp.diff_files.__len__() + len

