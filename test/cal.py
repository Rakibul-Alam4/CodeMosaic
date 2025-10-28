print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

option = int (input("enter the option:"))

if option in ([1,2,3,4]):

 num1 = int(input("enter the number: "))
 num2 = int(input("enter the number: "))

if (option==1):
 print(num1+num2)
elif (option==2):
 print (num1-num2)
elif (option==3):
 print(num1*num2)
elif (option==4):
 print(num1/num2)

else:
 print("Invalid Input")
