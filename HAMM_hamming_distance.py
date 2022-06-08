def hamd(filepath):
    file = open(filepath, 'r')
    fileContent = file.readlines()
    a = fileContent[0]      #string not list
    b = fileContent[-1]

    print(len(a))           #hence, length is not 1
    print(len(b))
    
    sum = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            sum += 1
    return sum

    file.close()

print(hamd('C:\\Users\\Maliha\\Desktop\\rosalind_hamm.txt'))

    

    
