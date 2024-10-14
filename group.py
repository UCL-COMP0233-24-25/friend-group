"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

'''
additonal features
class persons:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.relation = {}

    def add_relation(self, add_name, add_age, add_relation, job = None):
        self.relation[add_name] = [add_age, add_relation, job]


Shyam = persons("Shyam", 25)       

Shyam.add_relation("Daniel", 25, "friend", "doctor")
Shyam.add_relation("John", 26, "boss")
lists = Shyam.relation
print(lists)
'''

group = {
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

def max_age(group):
    max_age = 0
    for person in group:
        if group[person]["age"] > max_age:
            max_age = group[person]["age"]
    return max_age

def avg_no_of_relations(group):
    total_relations = 0
    for person in group:
        total_relations += len(group[person]["relations"])
    return total_relations/len(group)

def max_age_person_with_one_relation(group):
    max_age = 0
    for person in group:
        if len(group[person]["relations"]) >= 1:
            if group[person]["age"] > max_age:
                max_age = group[person]["age"]
    return max_age

def max_age_of_person_with_friend(group):
    max_age = 0
    for person in group:
        if "friend" in group[person]["relations"].values():
            if group[person]["age"] > max_age:
                max_age = group[person]["age"]
    return max_age
