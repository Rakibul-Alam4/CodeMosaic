import re
text = "1 is special character"
pattern = ("^character")
pattern = ("character$")

a=re.findall(pattern,text)
print(a)
if a:
    print("yes! the string ends with character")
else:
    print("no match")