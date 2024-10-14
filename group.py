"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

connections = ["friend", "partner", "landlord", "cousin", "tenant"]
my_group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "connections": {"Zalika": connections[0], "John": connections[1]},
    },
    "Zalika": {
        "age": 28,
        "job": "artist",
        "connections": {"Jill": connections[0], "Nash": connections[4]},
    },
    "John": {
        "age": 27,
        "job": "writer",
        "connections": {"Jill": connections[1], "Nash": connections[3]},
    },
    "Nash": {
        "age": 34,
        "job": "chef",
        "connections": {"Zalika": connections[2], "John": connections[3]},
    },
}


import numpy as np
#The maximum age of people in the group.
max_age = max(person['age'] for person in my_group.values())
print(f"maximum age: {max_age}")

#The average number of relations each person has.
mean_relations = np.mean([len(person['connections']) for person in my_group.values()])
print(f"average number of relations: {int(mean_relations)}")

# Finding the maximum age of people who have at least one relation
max_age_with_ge_one_relation = max(person['age'] for person in my_group.values() if person['connections'])
print(f"maximum age of people who have at least one relation: {max_age_with_ge_one_relation}")

# Finding the maximum age of people who have at least one friend
max_age_with_ge_one_friend = max([person['age'] for person in my_group.values() if list(person['connections'].values()).count("friend")>=1])
print(f"maximum age of people who have at least one friend {max_age_with_ge_one_friend}")