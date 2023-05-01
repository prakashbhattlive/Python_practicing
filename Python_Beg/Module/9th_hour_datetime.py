import datetime

x=datetime.datetime.now() ## current date time

#x=datetime.datetime(2021,1,1) ## setting static value

print(x)

print('year', x.strftime("%y"))
print('Month', x.strftime("%b"))
print('Hour', x.strftime("%H"))

