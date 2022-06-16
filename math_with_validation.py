import math

def validation():
    while True:
        num = input("Give a number: ")
        try:
            valid_num = int(num)
        except ValueError:
            print("This input is invalid.")
        else:
            break
    return valid_num

def main():
    print("Calculator")
  
    fnum = validation()
           
    snum = validation()
        
            
    while True:
        print(" (1) +\n (2) -\n (3) *\n (4) /\n (5) sin(number1/number2)\n (6)cos(number1/number2)\n (7) Change numbers\n (8) quit\n")
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
            print("The result is: ", math.sin(fnum/snum))
            print()
        elif(choice == "6"):
            print("The result is: ", math.cos(fnum/snum))
            print()
        elif(choice == "7"):
            fnum = validation()
            snum = validation()
            print()
        elif(choice == "8"):
            print("Thank you!")
            break

if __name__ == "__main__":
    main()