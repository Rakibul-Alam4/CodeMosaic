number_of_letter = 0
number_of_word = 0
number_of_digit = 0

text = input("Enter the text: ")

for x in text:
  if x>= 'a' and x<='z':
    number_of_word=number_of_word+1
  elif x>= '0' and x<='9':
    number_of_digit=number_of_digit+1
  elif x==' ':
     number_of_letter=number_of_letter+1

print("Number of word: ", number_of_word)
print("Number of letter: ", number_of_letter)
print("Number of digit: ", number_of_digit)