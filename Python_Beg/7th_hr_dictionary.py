d = {
    'name' : 'munna',
    'class' : '5th',
     'fees' :  200
}
#print(d, type(d))
#print(d['name'])
#print(d.get('name'))

#print("\n\n")

#for a in d.keys():
#    print(a)

#print("\n\n")

for a in d.values():
    print(a)

print("\n\n")

for a,b in d.items():
    print(a,b)

#del d['fees']

#z = d.pop('class')
#print("pop operation:-",z)
d.update({'fees': 2000})

#d.clear()

d['desc']="dictionary program"    ### dictionary item inserting

d['name'] = "chhunna"     ### other way for key updating

print(d)