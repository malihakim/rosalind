import re

def computingGC(filePath):                  
    file = open(filePath, 'r')
    fileText = file.read()

    nameRegex = re.compile(r'Rosalind_\d+')     #Rosalind_xxxx
    moName = nameRegex.findall(fileText)        #list

    stringRegex = re.compile(r'([\nATGC\n<])')  #DNA String
    mo1 = stringRegex.findall(fileText)         #['A', 'T', '\n', '\n', 'G']
    moString = ''.join(mo1).split('\n\n')       #['AT', 'GC']

    perGC = []

    for i in moString:
        countGC = i.count('G') + i.count('C')
        total = i.count('G') + i.count('C') + i.count('A') + i.count('T')
        percentGC = (countGC/total)*100
        perGC.append(percentGC)

    dict1 = dict(zip(moName, perGC))

    maxKey = max(dict1, key=dict1.get)
    maxValue = max(dict1.values())
    print(maxKey)
    print(maxValue)
    
    file.close()
    
computingGC('C:\\Users\\Maliha\Desktop\\rosalind_gc.txt') #C:\\ file path + name

