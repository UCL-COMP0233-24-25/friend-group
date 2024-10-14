"""An example of how to represent a group of acquaintances in Python."""

my_group = [
    {"name": "Jill", "age": 26, "job": "biologist", "connections": {"friends": ["Zalika"], "partner": "John"}},
    {"name": "Zalika", "age": 28, "job": "artist", "connections": {"friends": ["Jill"], "landlord": "Nash"}},
    {"name": "John", "age": 27, "job": "writer", "connections": {"partner": "Jill"}},
    {"name": "Nash", "age": 34, "job": "chef", "connections": {"cousins": ["John"], "tennants": ["Zalika"]}},
]

#note people cannot have the same name (add surname or number for duplicates)

def one_way_connection(name, related_to, relationship):
    for person in my_group:
        if person["name"] == name:
            if relationship not in person["connections"]:
                person["connections"][relationship] = [related_to]
            else:
                person["connections"][relationship].append(related_to)

#relationship1 -> adds to name1 and vice versa
def two_way_connection(name1, name2, relationship1, relationship2):
    one_way_connection(name1, name2, relationship1)
    one_way_connection(name2, name1, relationship2)

#removes connection between people
def forget(name1, name2):
    for person in my_group:
        if person["name"] == name1:
            for relationship in person["connections"]:
                if name2 in person["connections"][relationship]:
                    person["connections"][relationship].remove(name2)
        if person["name"] == name2:
            for relationship in person["connections"]:
                if name1 in person["connections"][relationship]:
                    person["connections"][relationship].remove(name1)

#use previous connection func to add connections
def add_person(name, age, job):
    my_group.append({"name": name, "age": age, "job": job, "connections": {}})
add_person("Tom", 30, "engineer")
one_way_connection("Tom", "Jill", "friends")
print(my_group)

def average_age():
    total_age = 0
    for person in my_group:
        total_age += person["age"]
    return total_age/len(my_group)
print(average_age())