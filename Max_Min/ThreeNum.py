num1 = int (input("Enter the num1: "))
num2 = int (input("Enter the num2: "))
num3 = int (input("Enter the num3: "))

if num1 > num2 and num1 > num3:
    print("num1 is bigger", num1)
elif num2 > num3 and num2 > num1:
    print("num2 is bigger",num2)
else:
    print("num3 is bigger",num3)
