print("Calculator")
num1 = input("Give the first number: ")
num2 = input("Give the second number: ")
num1_covt = int(num1)
num2_covt = int(num2)

print("\t(1) +\n\t(2) -\n\t(3) *\n\t(4) /\n")
choice = input("Please select something (1-4): ")

if(choice == "1"):
    print("The result is: ", num1_covt + num2_covt)
elif(choice == "2"):
    print("The result is: ", num1_covt - num2_covt)
elif(choice == "3"):
    print("The result is: ", num1_covt * num2_covt)
elif(choice == "4"):
    print("The result is: ", num1_covt / num2_covt)
else:
    print("Selection was not correct")