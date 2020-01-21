import re
lits_in = [1,0,2,4,3]
#aggrent in accending order
for i in range(4):
    temp = lits_in[i]
    if temp > lits_in[i+1]:
        lits_in[i] = temp
        temp= lits_in[i+1]
print(lits_in)




