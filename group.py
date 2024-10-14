"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = [
    {
        "Name": "Jill",
        "Age": 26,
        "Job": "Biologist",
        "Connections": {"Zalika": "friend", 
                        "John": "partner"}
    },
    {
        "Name": "Zalika",
        "Age": 28,
        "Job": "Artist",
        "Connections": {"Jill": "friend", 
                        "Nash": "landlord"}
    },
    {
        "Name": "John",
        "Age": 27,
        "Job": "Writer",
        "Connections": {"Jill": "partner"}
    },
    {
        "Name": "Nash",
        "Age": 34,
        "Job": "Chef",
        "Connections": {"John": "cousin", 
                        "Zalika": "tennant"}
    }
]

import numpy as np

max_age = max(person["Age"] for person in my_group)
print(f"Maximum age: {max_age}")

avg_nb_relations = np.mean([len(person["Connections"]) for person in my_group])
print(f"Average number of relations: {avg_nb_relations}")

max_age_with_at_least_one_relation = max(person["Age"] for person in my_group if len(person["Connections"]) >= 1)
print(f"Maximum age of people who have at least one relation: {max_age_with_at_least_one_relation}")

max_age_with_at_least_one_friend = max(person["Age"] for person in my_group if sum(relation=="friend" for relation in person["Connections"].values()) >= 1)
print(f"Maximum age of people who have at least one friend {max_age_with_at_least_one_friend}")