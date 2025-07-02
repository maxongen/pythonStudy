studentDict={
    "studentPerInfo":{
        "name":"hemant",
        "age":18,
        "address":"Katraj"
},
    "studentSchoolInfo":{
        "schoolName":"pantBodhPeeth",
        "className":"Pune"
    },
    "studentClassInfo":{
        "rollNo":28,
        "subjects":["premtarang","sfut lekh","premlahari","pushp"]
    }
}

print(studentDict)

print("create 3 dictionaries and we can add them to one dictionary")
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

finalDict={
    "child1":child1,
    "child2":child2,
    "child3":child3
}

print(finalDict)

print("access items from nested dictionary\nStudent Name : ",studentDict["studentPerInfo"]["name"])

print("loop through nested dictionary")
for std,obj in studentDict.items():
    print(std)
    for y in obj:
        print(y+" : ",obj[y])
