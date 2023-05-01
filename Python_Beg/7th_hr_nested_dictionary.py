course = {
    'php':{'duration':'3 months', 'fees':13000},
    'java':{'duration':'3 months', 'fees':15000},
    'python':{'duration':'1 months', 'fees':10000}
}
#print(course)
#print(course['php'] ['fees'])

course['java']['fees'] = 20000 ### value update

for k,v in course.items():
    #print(k,v)
    print(k,v['duration'], v['fees'])