"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = [
    {
        "name": "Jill",
        "age": 26,
        "job": "a biologist",
        "connection": {"friend": ["Zalika"], "partner": ["John"]},
    },
    {
        "name": "Zalika",
        "age": 28,
        "job": "an artist",
        "connection": {"friend": ["Jill"]},
    },
    {"name": "John", "age": 27, "job": "a writer", "connection": {"partner": ["Jill"]}},
    {
        "name": "Nash",
        "age": 34,
        "job": "a chef",
        "connection": {"cousin": ["John"], "landlord": ["Zalika"]},
    },
]

def print_my_group():
    for row in my_group:
        connections = " and ".join([f"{', '.join(map(str, v))}'s {k}" for k, v in row["connection"].items() if v])
        print(f"{row['name']} is {row['age']}, {row['job']}, {connections}")
    print("\n")


def forget(person1, person2):
    # Remove person2 from person1's connections
    for item in my_group:
        if item['name'] == person1:
            for k, v in item['connection'].items():
                if person2 in v:
                    v.remove(person2)
    
    # Remove person1 from person2's connections
    for item in my_group:
        if item['name'] == person2:
            for k, v in item['connection'].items():
                if person1 in v:
                    v.remove(person1)

# def add_person(name, age, job, relations):
#     new_person = {
#         "name": name, 
#         "age": age, 
#         "job": job, 
#         "connection": relations
#     }

#     # Add the new person to the group
#     my_group.append(new_person)

def add_person(name, age, job, relations):
    new_person = {
        "name": name, 
        "age": age, 
        "job": job, 
        "connection": relations
    }
    
    # Add connections to corresponding person
    for relation_type, related_persons in relations.items():
        for related_person in related_persons:
            # Find the related person in my_group and add the new person to their connections
            for item in my_group:
                if item['name'] == related_person:
                    # If the relation type doesn't exist, create it
                    if relation_type not in item['connection']:
                        item['connection'][relation_type] = []
                    # Add the new person to their connection list
                    if name not in item['connection'][relation_type]:
                        item['connection'][relation_type].append(name)


    # Add the new person to the group
    my_group.append(new_person)

def average_age():
    ages = [item['age'] for item in my_group]
    avg_age = sum(ages)/len(ages)
    return avg_age


def test():
    print('below is the original group info')
    print_my_group()
    
    print('Now forgetting the connection between Jill and John')
    forget("Jill", "John")
    print_my_group()
    
    print('Now adding a new person')
    add_person('HanLu', 22, 'a student', {'friend': ['John'], 'cousin': ['Nash']})
    print_my_group()
    
    print('Now calculating the average age')
    avg_age = average_age()
    print(f"the average age of my group is {avg_age}.")
    
if __name__ == "__main__":
    test()