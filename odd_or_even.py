num1 = input("Give a number: ")
num2 = input("Give a number: ")
num1_covt = int(num1)
num2_covt = int(num2)
if(num1_covt%2 == 0 and num2_covt%2 == 0):
    print("Both numbers are even.")
elif(num1_covt%2 == 0 or num1_covt%2 == 0):
    print("One of the numbers is even.")
else:
    print("Both numbers are odd.")