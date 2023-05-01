l = []
while True:
    c = int(input('''
    1 Push Elements (Enqueue)
    2 Pop Elements (Dequeue)
    3 Front Element
    4 Last Element
    5 Display Queue
    6 Exit
    '''))

    if c == 1:
        n = input("Enter the value:-");
        l.append(n)
        print(l)
    elif c == 2:
        if len(l) == 0:
            print("Queue is Empty")
        else:
            del l[0]
            print(l)

    elif c == 3:
        if len(l) == 0:
            print("Queue is Empty")
        else:
            print("First element of the queue:-", l[0])
    elif c == 4:
            if len(l) == 0:
                print("Queue is Empty")
            else:
                print("Last element of the queue:-", l[-1])
    elif c == 5:
        if len(l) == 0:
            print("Queue is Empty")
        else:
            print("Display Queue:-", l)        
    elif c == 6:
        break;
    else:
        print("Entered option is not available for queue")