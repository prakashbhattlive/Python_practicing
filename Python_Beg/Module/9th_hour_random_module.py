import  random
n=random.randint(1, 6)
print(n)

p=random.randrange(1,101) #### Guessing game
#print("computer generated value:---",p)

l=[10,20,30,40]

lc=random.choice(l)

print(lc)
print(random.random())
print(random.shuffle(l),l)
print(random.uniform(1, 3))

q = int(input("Enter your number:---")) ###guessing game

if q > p:
    print("computer generated value:---",p)
    print("your guess number is too high")
elif p > q:
    print("computer generated value:---",p)
    print("your guess number is too low")

else:
    print("computer generated value:---",p)
    print("your guess is correct")