with open('C:\\Users\\Maliha\Desktop\\rosalind_subs2.txt') as file:  #rosalind_ID NAME.txt
   content = file.read()
   s, t = content.split()

[print(i+1) for i in range(len(s)) if s[i:i+len(t)] == t]

#locations = []
#[locations.append(i+1) for i in range(len(s)) if s[i:i+len(t)] == t] 
