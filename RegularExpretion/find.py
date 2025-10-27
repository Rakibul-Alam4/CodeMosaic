import re
text = "1 is special character"
pattern = ("^1")

a=re.findall(pattern,text)

if a:
    print("1 is special character ")
else:
    print("no special character")