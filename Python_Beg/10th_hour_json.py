import json
d={
    'course_name' : 'python',
    'fees' : 2000
}
j=json.dumps(d)
print(j, type(j))