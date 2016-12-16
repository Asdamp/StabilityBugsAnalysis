from filecmp import dircmp
import os

def count_class_mod(path, path2):
    #prendo tutti i file che NON sono di interesse della versione1
    excludedFile1 = dotFiles = [os.path.join(root, name)
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
    #elimino il pecorso, prelavndo solo il nome dei file
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

    dcmp = dircmp(path,path2, ignore=str)
    return dcmp.diff_files.__len__()

path="C:\Users\Assunta\Desktop\JEDIT_prove_varie\jeditJava\\"
path2="C:\Users\Assunta\Desktop\JEDIT_prove_varie\jeditJava2\\"
print(count_class_mod(path, path2))