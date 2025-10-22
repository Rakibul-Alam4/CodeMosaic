num1 = int (input("Enter the num1: "))
num2 = int (input("Enter the num2: "))
num3 = int (input("Enter the num3: "))


if num1>num2 and num1>num3:
 print("The getter num is: ",num1)
elif num2>num3 and num2>num1:
 print("The getter num is: ",num2)
elif num3>num1 and num3>num2:
 print("The getter num is:",num3)
else:
 print("Invalid Input")