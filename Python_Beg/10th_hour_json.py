import json
d={
    'course_name' : 'python',
    'fees' : 2000
}
j=json.dumps(d)
print(j, type(j))

d1= '{"cname" : "python", "fees" : 3000, "duration" : "2 months"}'
x1=json.loads(d1)
print(x1, type(x1))

for a in x1:
    print(a, x1[a])

####Writing & reading Json

file2=open('nifty_data.json','r')
x2=file2.read()
final_data=json.loads(x2)

for a in final_data:
    #print(a)
    print(a['HistoricalDate'], a['OPEN'])    