j = "loop is running"
#print(j.find('n'))        #--> finding index value of string
#print(j.find('n',11))
#print(j.find('n',12))
#print(j.find('is'))


print(j.index('i', 6))     #--> finding index value of string and result skippig first 6 values
print(j.isalpha())         # --> False, due to the whitespace
print(j.isalnum())
print(j.isdigit())
print(j.islower())

#a = int(input("Enter the ASCII integer: "))
#print("\n ASCII equivalent String characters: ",chr(a))

#a = input("Enter a character: ")
#print("\n ASCII values are: ",ord(a))

w="while loop is {0} {1} running".format("not","failed to")   ##String format
print(w)