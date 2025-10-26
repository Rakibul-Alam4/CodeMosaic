"""
1+2+3+4+.....+n
"""
n= int (input ("enter the number: "))
sum = 0
for x in range ( 2, n+1, 2):
    sum=sum+x
print(sum)