"""An example of how to represent a group of acquaintances in Python."""



my_group =  {


    "Jill": {
        "age": 26,
        "job": "biologist",
        "relations": {
            "Zalika": "friend",
            "John": "partner"
        }
    },

    "Zalika": {
        "age": 28,
        "job": "artist",
        "relations": {
            "Jill": "friend"
        }
    },

    "John": {
        "age": 27,
        "job": "writer",
        "relations": {
            "Jill": "partner"
        }
    },

    "Nash": {
        "age": 34,
        "job": "chef",
        "relations": {
            "John": "cousin",
            "Zalika": "landlord"
        }
    }
}


#Maximum age:

max_age = max(person['age'] for person in my_group.values())

print(f"The max age of the person is: {max_age}")

#Average relations:

total = 0 

for person in my_group.values():

    total += len(person['relations'])


avg = total / len(my_group)

print(f"The avg number of relations is: {avg}")


#Max age of people in the group with atleast one relation:

max_age_new = 0

for person in my_group.values():

    if person['relations']:

        max_age_new = max(person['age'],max_age_new)

print(f"The max age with a person more than one relation: {max_age_new}")

#max age of person if they have more thann one friend 

max_age_friend = 0 

for person in my_group.values():

    if 'friend' in person['relations'].values():

        max_age_friend = max(max_age_friend, person['age'])

print(f"Max age with atleast one friend: {max_age_friend}")