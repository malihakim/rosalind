# M1 = 1 immature               = 1 
# M2 = 1 mature                 = 1
# M3 = 1 alive + 3 immature     = 4      
# M4 = 4 alive + 3 mature       = 7     (1 alive + 3 mature + 4*3 offsprings)
# M5 = 7 alive + 12 immature    = 19    
# M6 = 19 alive + 21 mature     = 40
# M7 = 40 alive + 19*3 immature   

# 1, 1, 4, 7, 19, 40, 

#n months and k pairs of rabbits
#(5, 3) = 5 months and 3 rabbit pairs as offspring
# M1 = 1(immature). Hence, M2 = 1(mature)

def fibRabbits(n, k):
    a, b = 1, 1
    c = 1
    for i in range(2, n):
        c = a + b*k
        a, b = c, a
    return c
    
print(fibRabbits(33, 4))



        
