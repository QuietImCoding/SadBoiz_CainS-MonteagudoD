from pymongo import MongoClient

#server = MongoClient("149.89.150.100")
server = MongoClient("127.0.0.1")
db = server.sadboizdb
s = db.students
t = db.teachers

# Opens and reads file into stringthing
f=open("peeps.csv", "r")
students = f.read().strip()
f.close()

f=open("courses.csv", "r")
courses = f.read().strip()
f.close()

f = open("teachers.csv", "r")
teachers = f.read().strip()
f.close()

# Splits the string into an array called splitString
splitStudent = str.split(students, "\n")
splitCourses = str.split(courses, "\n")
splitTeachers = str.split(teachers, "\n")
    
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
        s.insert_one(studentinfo)

for entry in splitTeachers:
    data = str.split(entry, ",")
    if "code" not in data:
        teacherinfo = {"code":data[0], "name": data[1], "period":int(data[2])}
        studentids = []
        for student in s.find():
            for grade in student["grades"]:
                if data[0] in grade and data[0] not in studentids:
                    studentids.append(student["id"])
        teacherinfo["studentids"] = studentids
        t.insert_one(teacherinfo)

print "STUDENTS:\n"
for i in s.find():
    print i

print "\n\nTEACHERS:\n"
for i in t.find():
    print i
