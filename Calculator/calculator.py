print("1 - Addition")
print("2 - Substar")
print("3 - Multiply")
print("4 - Divided")
option = int (input ("Chose an operation: "))

if option in ([1,2,3,4]):
  
  num1= int (input ("Enter the num1: "))
  num2= int (input ("Enter the num2: "))

if(option==1):
 result=num1+num2
elif(option==2):
  result=num1-num2
elif(option==3):
  result=num1*num2
elif(option==4):
  result=num1/num2
else:
  print("Chosse an correct option")
  
print("The result is the operation is: {}".format(result))