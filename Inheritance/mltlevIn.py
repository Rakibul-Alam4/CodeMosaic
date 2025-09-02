#Multi_Level Inheritance
class AA:
    name= "Car"
    model = "bmw"
    country = "German"

class BB(AA):
    phone="apple"
    camera="canon"
class CC(BB):
    bike="honda"
    laptop="hp"
c=CC()

class ZZ(CC):
    placeholder = " "

z =ZZ()
print(z.laptop)
print(z.bike)
print(c.camera)