import json

def print_description(dict):
    relationships = []
    for key, value in dict["Relationships"].items():
        relationships.append(f"{value}'s {key.lower()}")
    relationships_str = " and ".join(relationships)
    if dict["Job"][0] in ["A", "E", "I", "O", "U"]:
        j = "an"
    else:
        j = "a"
    print(
        f"{dict["Name"]} is {dict["Age"]}, {j} {dict["Job"].lower()}, and {relationships_str}."
    )

def max_age(people):
    maximum = 0
    for person in people:
        if person["Age"] > maximum:
            maximum = person["Age"]
    return maximum

def avg_relationships(people):
    num_relations = []
    for person in people:
        num_relations.append(len(person["Relationships"]))
    avg = sum(num_relations) / len(people)
    return avg

#fn for max age in group
#avg number of relationships
#max age of people in group that have at least 1 relationship


Jill = {
    "Name": "Jill",
    "Age": 26,
    "Job": "Biologist",
    "Relationships": {"Friend": "Zalika", "Partner": "John"},
}

Zalika = {
    "Name": "Zalika",
    "Age": 28,
    "Job": "Artist",
    "Relationships": {"Friend": "Jill"},
}

John = {
    "Name": "John",
    "Age": 27,
    "Job": "Writer",
    "Relationships": {"Partner": "Jill"},
}

Nash = {
    "Name": "Nash",
    "Age": 34,
    "Job": "Chef",
    "Relationships": {"Cousin": "John", "Landlord": "Zalika"},
}

People = [Jill, Zalika, John, Nash]

for i in People:
    print_description(i)

print(max_age(People))
print(avg_relationships(People))

with open('people.json', 'w') as f:
    json.dump(People, f, indent=4)