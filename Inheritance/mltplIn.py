#Multiple_Inheritance
class AA:
    name= "Car"
    model = "bmw"
    country = "German"

class BB:
    phone="apple"
    camera="canon"
class CC:
    bike="honda"
    laptop="hp"

class ZZ(AA,BB,CC):
    placeholder = " "

z =ZZ()
print(z.laptop)