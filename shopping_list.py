list = []
i = 0
while True:
    op = input("Would you like to\n (1) Add or\n (2) Remove items or\n (3) Quit?: ")

    if op == "1":
        items = input("What will be added?: ")
        list.append(items)
    elif op == "2":
        for i in range (0, len(list)):
            i += 1
        print("There are ", i ," items in the list.")
        ch = input("Which item is deleted?: ")
        if int(ch) >= len(list):
            print("Incorrect selection.")
        else:
            list.pop(int(ch))
    elif op == "3":
        print("The following items remain in the list:")
        for i in list:
            print(i)
        break
    else:
        print("Incorrect selection.")