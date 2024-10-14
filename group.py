"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = [
    {
        "name": "Jill",
        "age": 26,
        "job": "Biologist",
        "relations": [
            {"name": "Zalika", "relationship": "friend"},
            {"name": "John", "relationship": "partner"}
        ]
    }, 
    {
        "name": "Zalika",
        "age": 28,
        "job": "Artist",
        "relations": [
            {"name": "Jill", "relationship": "friend"}
        ]
    }, 
    {
        "name": "John",
        "age": 27,
        "job": "Writer",
        "relations": [
            {"name": "Jill", "relationship": "partner"},
            {"name": "Nash", "relationship": "cousin"}
        ]
    }, 
    {
        "name": "Nash",
        "age": 34,
        "job": "Chef",
        "relations": [
            {"name": "John", "relationship": "cousin"},
            {"name": "Zalika", "relationship": "landlord"}
        ]
    }
]

def print_my_group():
    for people in my_group:
        print(f"{people['name']} is {people['age']}, a/an {people.get('job', 'No job')}, ", end='')
        relations = [f"{connection['name']}'s {connection['relationship']}" for connection in people['relations']]
        print(f"{' and '.join(relations)}")

def forget(person1, person2):
    for person in my_group:
        if person["name"] == person1:
            person["relations"] = [c for c in person["relations"] if c["name"] != person2]
        if person["name"] == person2:
            person["relations"] = [c for c in person["relations"] if c["name"] != person1]

def add_person(name, age, job, relations):
    new_person = {
            "name": name,
            "age": int(age),
            "job": job,
            "relations": relations
    }
    my_group.append(new_person)

def avg_age():
    total_ages = 0
    for person in my_group:
        total_ages += person['age']
    average_age = total_ages / len(my_group)
    print(f"The average age of my group is {average_age}")

"""print_my_group()
forget("Jill", "John")
add_person("Jiasheng", 24, "HPC Engineer", [{"name": "Jill", "relationship": "friend"}])
print_my_group()
avg_age()
"""
