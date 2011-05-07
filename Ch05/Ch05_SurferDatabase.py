import sqlite3

def find_details(competitionid):

    db = sqlite3.connect("surfersDB.sdb")
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute("select * from surfers")
    rows = cursor.fetchall()
    for row in rows:
        if row['id'] == competitionid:
            s = {}
            s['id'] = str(row['id'])
            s['name'] = str(row['name'])
            s['country'] = str(row['country'])
            s['average'] = str(row['average'])
            s['board'] = str(row['board'])
            s['age'] = str(row['age'])
            cursor.close()
            return(s)
    cursor.close()

    return({})

competitionid = int(input("Enter the id of the surfer: "))
surfer = find_details(competitionid)
if surfer:
    print("ID:          " + surfer['id'])
    print("Name:        " + surfer['name'])
    print("Country:     " + surfer['country'])
    print("Average:     " + surfer['average'])
    print("Board type:  " + surfer['board'])
    print("Age:         " + surfer['age'])
