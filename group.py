"""An example of how to represent a group of acquaintances in Python."""

#For the relationship of each person, it is like: the front person is the “relationship” of the behind person. 
my_group = {
    "Jill":{"age":26,"job":"biologist","relationship":{"friend":["Zalika"],"partner":["John"]}},
    "Zalika":{"age":28,"job":"artist","relationship":{"friend":["Jill"]}},
    "John":{"age":27,"job":"writer","relationship":{"partner":["Jill"]}},
    "Nash":{"age":34,"job":"chef","relationship":{"landlord":["Zalika"]}},
}

def forget(person1,person2):
    if person1 not in my_group:
        print(f"{person1} is not in the group.")
        return
    if person2 not in my_group:
        print(f"{person2} is not in the group.")
        return
    to_remove_1 = []
    to_remove_2 = []
    for relationship, names in my_group[person1]["relationship"].items():
        if person2 in names:
            my_group[person1]["relationship"][relationship].remove(person2)
            if my_group[person1]["relationship"][relationship] == []:
                to_remove_1.append(relationship)
    for relationship, names in my_group[person2]["relationship"].items():
        if person1 in names:
            my_group[person2]["relationship"][relationship].remove(person1)
            if my_group[person2]["relationship"][relationship] == []:
                to_remove_2.append(relationship)

    for key in to_remove_1:
        del(my_group[person1]['relationship'][key])
    
    for key in to_remove_2:
        del(my_group[person2]['relationship'][key])
    
    return
