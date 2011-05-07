def find_details(competitionid):

    surfers_f = open("surfing_data.csv")

    for each_line in surfers_f:
        s = {}
        (s['id'], s['name'], s['country'], s['average'], s['board'], s['age']) = each_line.split(";")

        if competitionid == int(s['id']):
            return(s)

        surfers_f.close()

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
