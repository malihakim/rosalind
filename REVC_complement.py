DNA = input() 

#flip DNA sequence
reverseDNA = DNA[::-1]

#convert nucleotides without changing sequence
lowerDNA = reverseDNA.replace('T', 'a').replace('A', 't').replace('C', 'g').replace('G', 'c')

#fix
complement = lowerDNA.upper()

#print to obtain output
print(complement)




#use reversed.translate(str.maketrans('AGCT', 'TCGA'))
