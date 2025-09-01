from random import randint

guessNumber = int (input("Enter the number: "))
randomNumber=randint(1,5)

if guessNumber == randomNumber:
 print("You won")
else:
 print("you lost")
 print("The guessNumber is: ", guessNumber)