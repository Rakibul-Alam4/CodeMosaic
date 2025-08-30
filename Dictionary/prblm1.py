StudentInfo = {
    "Eshan":{
        "Ins": "bkh",
        "Roll": 10,
        "Vill": "Rangpur"
    },
    "Samir":{
        "Ins": "bjhjkhj",
        "Roll": 12,
        "vill": "Dinajpur"
    }
} 
#print(StudentInfo)
#print(StudentInfo["Eshan"]["Vill"])
#x=StudentInfo.keys()
#print(x)
StudentInfo.update({"Samir": "Samir is a student"})
print(StudentInfo)