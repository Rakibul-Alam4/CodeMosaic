from random  import randint

for x in range(1,6):
 guessNumber = int (input ("Enter the guess number: "))
 randomNumber= randint(1,5)
 if guessNumber==randomNumber:
    print("you won")
 else:
    print("you lost")
    print("random number is : ",randomNumber)