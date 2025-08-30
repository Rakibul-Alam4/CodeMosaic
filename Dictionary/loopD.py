StudentInfo = {
    "Jamal":{
        "Name": "jamal",
        "Roll": 22,
        "Vill": "Cumilla"
    },
    "Kamal":{
        "Name":"Kamal",
        "Roll": 33,
        "Vill": "Chadpur"
    },
    "Masud": 430
}
"""
print(StudentInfo)
StudentInfo.update({"Roll": 66})
print(StudentInfo)
"""
"""
for i in StudentInfo:
 print(i)
"""
for a in StudentInfo.values():
 print(a)
StudentInfo.update({"Masud": "Dinajpur"})
print(StudentInfo)