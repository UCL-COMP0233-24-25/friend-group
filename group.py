"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
import numpy as np

my_group = {
    'Jill': {
        'age': 26,
        'job': 'biologist',
        'connections': {
            'Zalika': 'friend',
            'John': 'partner',
        }
    },
    'Zalika': {
        'age': 28,
        'job': 'artist',
        'connections': {
            'Jill': 'friend',
            'Nash': 'tenant'
        }
    },
    'John': {
        'age': 27,
        'job': 'writer',
        'connections': {
            'Jill': 'partner',
            'Nash': 'cousin'
        }
    },
    'Nash': {
        'age': 34,
        'job': 'chef',
        'connections': {
            'John': 'cousin',
            'Zalika': 'landlord'
        }
    },
    'Nobody': {
        'age': 40,
        'job': None,
        'connections': {}
    }
}

# Quick test - printing who knows who
# for name1 in my_group.keys():
#     if my_group[name1]['connections']:
#         for name2 in my_group[name1]['connections']:
#             print(f'{name1} knows {name2}')

### STRETCH GOALS ####
# Forget function
def forget(person_1, person_2):
    if person_1 in my_group and person_2 in my_group[person_1]["connections"]:
        my_group[person_1]["connections"].pop(person_2)
    if person_2 in my_group and person_1 in my_group[person_2]["connections"]:
        my_group[person_2]["connections"].pop(person_1)
    else:
        print("Error: check names.")

# Add Person
def add_person(name, age, job=None, relations=None):
    if not isinstance(name, str):
        print("Name must be string")
        return
    if not isinstance(age, int):
        print("Age must be integer")
        return
    if job and not isinstance(job, str):
        print("Job must be string")
        return
    if relations and not isinstance(relations, dict):
        print("Connections must be dict")
        return
    my_group[name] = {"age": age, "job": job, "connections": relations}

# Mean age
def average_age():
    ages = [my_group[person]["age"] for person in my_group.keys()] 
    return np.mean(ages)

# Homework Assignment
def homework():
    max_age = np.max([person["age"] for person in my_group.values()])
    print(max_age)
    mean_connections = np.mean([len(person["connections"]) for person in my_group.values()])
    print(mean_connections)
    max_age_with_connections = np.max([person["age"] for person in my_group.values() if person["connections"]])
    print(max_age_with_connections)
    max_age_with_friends = np.max([person["age"] for person in my_group.values() if "friend" in person["connections"].values()])
    print(max_age_with_friends)

homework()

# Reading + Writing (YAML)
import yaml
with open("data_structure.yaml", "w") as f:
    yaml.dump(my_group, stream=f)
with open("data_structure.yaml", "r") as f:
    loaded_data = yaml.safe_load(f)
print(loaded_data)

# Reading + Writing (JSON)
import json
with open("data_structure.json", "w") as f:
    json.dump(my_group, f, indent=4, sort_keys=False)
with open("data_structure.json", "r") as f:
    loaded_data = json.loads(f.read())
print(loaded_data)
