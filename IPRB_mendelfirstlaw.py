# KK = AA AA AA AA
# MM = AA Aa Aa aa - 1/4
# nn = aa aa aa aa - 1

# KM = AA AA Aa Aa
# Kn = Aa Aa Aa Aa
# Mn = Aa Aa aa aa - 1/2

# MM = P(X=M, Y=M) = P(M)*P(M) = m/total * m-1/total-1
# nn = P(X=n, Y=n) = P(n)*P(n) = n/total * n-1/total-1
# Mn = P(X=M, Y=n) + P(X=n, Y=m)
#    = (m/total * n/total-1) + (n/total * m/total-1)

def mendelLaw(filePath):
    file = open(filePath, 'r')
    k, m, n = file.read().split()

    k = float(k)
    m = float(m)
    n = float(n)
    
    total = k + m + n

    recMn = (m/total)*(n/(total-1))*0.5 + (n/total)*(m/(total-1))*0.5
    recMM = (m/total)*((m-1)/(total-1))*0.25
    recnn = (n/total)*((n-1)/(total-1))*1

    oneDom = 1 - (recMn + recMM + recnn)
    print(oneDom)
    
    file.close()

mendelLaw('C:\\Users\\Maliha\\Desktop\\rosalind_iprb.txt')
