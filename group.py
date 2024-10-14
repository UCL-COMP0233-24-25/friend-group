"""An example of how to represent a group of acquaintances in Python."""

#For the relationship of each person, it is like: the front person is the “relationship” of the behind person. 
my_group = {
    "Jill":{"age":26,"job":"biologist","relationship":{"friend":["Zalika"],"partner":["John"]}},
    "Zalika":{"age":28,"job":"artist","relationship":{"friend":["Jill"]}},
    "John":{"age":27,"job":"writer","relationship":{"partner":["Jill"]}},
    "Nash":{"age":34,"job":"chef","relationship":{"landlord":["Zalika"]}},
}

def forget(person1, person2):
    
    if person1 not in my_group:
        print(f"{person1} is not in the group.")
        return
    if person2 not in my_group:
        print(f"{person2} is not in the group.")
        return

    def remove_relationship(person_a, person_b):
        to_remove = []
        for relationship, names in my_group[person_a]["relationship"].items():
            if person_b in names:
                my_group[person_a]["relationship"][relationship].remove(person_b)
                if not my_group[person_a]["relationship"][relationship]:
                    to_remove.append(relationship)
        for relationship in to_remove:
            del my_group[person_a]["relationship"][relationship]

    remove_relationship(person1, person2)
    remove_relationship(person2, person1)

    return

def add_person(name,age,job,relation):
    
    if name in my_group:
        print(f"{name} is already in my_group.")
        return
     
    my_group[name] = {'age':age,'job':job,'relationship':relation}

    for relationship, people in relation.items():
        for person in people:
            if person not in my_group:
                my_group[person] = {'relationship':{relationship:[name]}}
            else:
                if relationship in my_group[person]['relationship']:
                    my_group[person]['relationship'][relationship].extend([name])    
                else:
                    my_group[person]['relationship'][relationship] = [name]

    return

def average_age(group):
    
    import numpy as np
    
    n = len(my_group.keys())
    ages = np.zeros(n)
    for i, (person, info) in enumerate(my_group.items()):
        ages[i] = info['age']
    average_age = np.average(ages)

    return average_age