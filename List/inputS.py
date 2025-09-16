numOfWords = 0
numOfLetters = 0
numOfDigit = 0

text = input ("enter the number: ")
for x in text:
    x=x.lower()
    if   x >= 'a' and x<= "z":
        numOfLetters = numOfLetters+1
    elif x>='0' and x<='9':
        numOfDigit = numOfDigit+1
    elif x == ' ':
        numOfWords = numOfWords+1

print("number of letters: ", numOfLetters)
print("number of digit: ",numOfDigit)
print("number of words: ",numOfWords)