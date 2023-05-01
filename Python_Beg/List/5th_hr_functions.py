p = []
for a in range(1,101):
    p.append(a)

#print(p,"\n")

n=[m for m in range(1,101) if m%2==0]
#print(n)

s = 'welcome'
k = [b for b in s]
#print(k)

l = [10,20,30,101,10,50,60,70,80,10,20]
#print(l.count(10))
#print(max(l))
#print(min(l))
l.sort()
l.reverse()
print(l)
print(l.index(50))