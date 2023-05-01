l = [10,20,30,40,50,60]
l1 = [1,2,3,4,5,6]

for a,b in zip(l,l1):
    print(a,b)

print("\n")
### convert string to list

#n = input("Enter the string:-")

#print(n)

#l = n.split();
#print(l)


l = []
for a in range(1,4):
    n = input("Enter the string"+str(a)+":-")
    l.append(n)
print(l)

