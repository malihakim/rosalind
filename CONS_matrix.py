import re, numpy as np

with open('C:\\Users\\Maliha\\Desktop\\rosalind_cons.txt') as file:
    content = file.read()
    rosRegex = re.compile(r'[^>Rosalind_\d+]+')
    mat = rosRegex.findall(content.replace('\n', ''))

tmat = list(zip(*mat))

a, c, g, t = [], [], [], []
cons = []

for string in tmat: #AGAATAA
    asum, csum, gsum, tsum = 0, 0, 0, 0
    for dna in string: # A, G, A, A, T, A, A
        if dna == 'A': asum += 1
        if dna == 'C': csum += 1
        if dna == 'G': gsum += 1
        if dna == 'T': tsum += 1
    a.append(asum), c.append(csum), g.append(gsum), t.append(tsum)
    max_count = max(asum, csum, gsum, tsum)
    if max_count == asum: cons.append('A')
    elif max_count == csum: cons.append('C')
    elif max_count == gsum: cons.append('G')
    elif max_count == tsum: cons.append('T')


print(''.join(cons))    
print('A: ' + str(' '.join(map(str, a))))
print('C: ' + str(' '.join(map(str, c))))
print('G: ' + str(' '.join(map(str, g))))
print('T: ' + str(' '.join(map(str, t))))
