numberOfLetter = 0
numberOfWord = 0
numberOfDigit = 0

text = input ("Enter the text: ")
for x in text:
    x=x.lower()
    if x>='a' and x<='z':
      numberOfLetter=numberOfLetter+1
    elif x>='0' and x<='9':
       numberOfDigit=numberOfDigit+1
    elif x == ' ':
       numberOfWord = numberOfWord+1

print("Number of letters: ", numberOfLetter)
print("Number of digit: ",numberOfDigit)
print("Number of word: ", numberOfWord)