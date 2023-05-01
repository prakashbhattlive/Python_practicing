l = []
while True:
    c = int(input('''
    1 Push Elements
    2 Pop Elements
    3 Peek Elements
    4 Display Stack
    5 Exit
    '''))
    if c == 1:
        n = input("Enter the value:-");
        l.append(n)
        print(l)
    elif c == 2:
        if len(l) == 0:
            print("Stack is Empty")
        else:
            p=l.pop()
            print(p)
            print(l)
    elif c == 3:
            if len(l) == 0:
                print("Stack is Empty")
            else:
                print("Peek Elements:- ", l[-1])
    elif c == 4:
         if len(l) == 0:
                print("Stack is Empty")
         else:
            print("Display Stack:- ", l)
    elif c == 5:
        break;
    else:
        print("Invalid operations...")