from re import T


print("Calculator")
fnum = int(input("Give the first number: "))
snum = int(input("Give the second number: "))
while(True):
    print(" (1) +\n (2) -\n (3) *\n (4) /\n (5) Change numbers\n (6) quit\n")
    print("Current numbers: ", fnum, snum)
    choice = input("Please select something(1-6): ")
    if(choice == "1"):
        print("The result is: ", fnum + snum)
        print()
    elif(choice == "2"):
        print("The result is: ", fnum - snum)
        print()
    elif(choice == "3"):
        print("The result is: ", fnum * snum)
        print()
    elif(choice == "4"):
        print("The result is: ", fnum / snum)
        print()
    elif(choice == "5"):
        fnum = int(input("Give the first number: "))
        snum = int(input("Give the second number: "))
        print()
    elif(choice == "6"):
        print("Thank you!")
        break
