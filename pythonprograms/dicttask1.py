
theaters = [
    {
        "name": "T1",
        "screens":
            [
                {"screen_number": 1, "seats": {"A1": False, "A2": False, "B1": True}}
            ]
    },  
    {
        "name": "T2",
        "screens":
            [
                {"screen_number": 1, "seats": {"A1": True, "A2": True}}
            ]
    },
]




########## show the availability
theater_name = "T2"
screen_no = 1

found = False
for t in theaters:
    for sc in t["screens"]:
        for sid, booked in sc["seats"].items():
            if t["name"] == theater_name and sc["screen_number"] == screen_no and \
                                                              booked == False:
                print(sid, end=" ")
                found = True

if found == False:
    print("(none)")
else:
    print("")



################# book seat
theater_name = "T1"
screen_no = 1
seat_id = "A2"

for t in theaters:
    for sc in t["screens"]:
        if t["name"] == theater_name and sc["screen_number"] == screen_no:
            sc["seats"][seat_id] = True

print("Booked " + seat_id + " at " + theater_name + " - Screen " + str(screen_no) + ".")






## cancel a screen
theater_name = "T1"
screen_no = 2

for t in theaters:
    if t["name"] == theater_name:
        new_screens = []
        for sc in t["screens"]:
            if sc["screen_number"] != screen_no:
                new_screens.append(sc)
        t["screens"] = new_screens

print("Removed screen " + str(screen_no) + " from " + theater_name + ".")
print(theaters)
