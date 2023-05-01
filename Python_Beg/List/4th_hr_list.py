l = [10,30,40,"hello", [1,3,5]]
print(l[4][1])
print(l[-1::-1])  ### reversing

#### List Iteration
print("\n\n")

t = len(l)

for n in range(t-1,-1,-1):    ###reversing via loop
    print(l[n])

print("\n\n")

for a in l:
    print(a)