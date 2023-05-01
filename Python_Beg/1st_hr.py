text = ''' hello,
how are you,
what is your dad's name'''
print(text)

s = eval(input("Enter the any value:-"))
print(s, type(s))


a = int(input("Enter the integer:-"))
if a%2==0:
    print(a, ": it's even value")
else:
    print(a, ": It's odd value")