t=(10,20,39,49,12,21,20)
print(type(t))
#print(t)
l=len(t)

for n in range(l):
    print(n,t[n])

#for a in t:
#    print(a)

print('min in tuple:',min(t))
print('max:', max(t))
print('count of 20:', t.count(20))
print('index of 39:', t.index(39))
print('sum :', sum(t))
print('sum :', sum(t,10))   

    

