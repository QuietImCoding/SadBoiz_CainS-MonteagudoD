from pymongo import MongoClient

server = MongoClient("149.89.150.100")

db = server.sadboiz



# Opens and reads file into stringthing
file=open("peeps.csv", "r")
stringthing = file.read()

# Splits the string into an array called splitString
splitString = str.split(stringthing, "\r\n")

dict = {}

# Loops through array line by line
for line in splitString:
    if "id" not in line:
        if len(line)>0 and line[0]=='"':
            line = line[1:]
            dict[float(line[line.index('"')+2:])]=line[0:line.index('"')]
        elif len(line)>0 and splitString.index(line)!=0:
    #print line
            dict[float(line[line.index(',')+1:])]=line[0:line.index(',')]
    
print dict
