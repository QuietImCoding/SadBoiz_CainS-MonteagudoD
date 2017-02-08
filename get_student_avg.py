from pymongo import MongoClient

def avgGrades(gradeList):
    items = len(gradeList)
    total = 0
    for course in gradeList:
        total += course[course.keys()[0]]
    return float(total) / items
        
server = MongoClient("149.89.150.100")
#server = MongoClient("127.0.0.1")
db = server.sadboizdb
c = db.students


for i in c.find():
    sdata = "Name: %s, ID: %s, Average: %s" % (i["name"], i["id"], avgGrades(i["grades"]))
    print sdata

