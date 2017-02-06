from pymongo import MongoClient

#server = MongoClient("149.89.150.100")
server = MongoClient("127.0.0.1")
db = server.sadboizdb
c = db.sadboizc

# Opens and reads file into stringthing
f=open("peeps.csv", "r")
students = f.read().strip()
f.close()

f=open("courses.csv", "r")
courses = f.read().strip()
f.close()


# Splits the string into an array called splitString
splitStudent = str.split(students, "\n")
splitCourses = str.split(courses, "\n")
    
studentsGrades = {}
for entry in splitCourses:
    data = str.split(entry, ",")
    if "id" not in data and int(data[2]) not in studentsGrades:
        studentsGrades[int(data[2])] = [{data[0]:int(data[1])}]
    elif "id" not in data:
        studentsGrades[int(data[2])].append({data[0]:int(data[1])})

for entry in splitStudent:
    data = str.split(entry, ",")
    if "id" not in data:
        studentinfo = {"name":data[0], "age":int(data[1]), "id":int(data[2])}
        studentinfo["grades"] = studentsGrades[studentinfo["id"]]
        c.insert_one(studentinfo)


