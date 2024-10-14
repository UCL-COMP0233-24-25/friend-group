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