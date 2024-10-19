"""An example of how to represent a group of acquaintances in Python."""

import numpy as np

def max_age(Group):
    ages = [Group[person]["age"] for person in Group]
    return max(ages)

def average_relations(Group):
    relations = [len(Group[person]["connections"]) for person in Group]
    return np.mean(relations)

def max_age_one_relation(Group):
    ages = [Group[person]["age"] for person in Group if len(Group[person]["connections"]) > 0]
    return max(ages)

def max_age_one_friend(Group):

    ages = []

    for data in Group.values():
        for connection in data["connections"].keys():
            if connection == "Friend":
                ages.append(data["age"])
                break
            
    return max(ages)

#A function taking in the data for one person and ammending the inputted dictionary with a nested dictionary containing thier data.
def add_to_group(Group,Name,Age,Job="",Connections={}): #Connections is a list of 2 element tuples
    Group[Name] = {"age": Age, "job": Job, "connections":{Relationship[0]:Relationship[1] for Relationship in Connections}}
    return None

#Implimenting instances of a group network using the 'add_to_group' function for the provided data.
my_group = {}
add_to_group(my_group,"Jill",26,"Biologist",Connections=[("Friend","Zalika"),("Partner","John")])
add_to_group(my_group, "Zalika",28,"Artist",Connections=[("Friend","Jill")])
add_to_group(my_group, "John",27,"Writer", Connections=[("Partner", "Jill")])
add_to_group(my_group, "Nash",34,"Chef",Connections=[("Cousin","John"),("Landlord","Zalika")])

print(my_group)

print(max_age(my_group))
print(average_relations(my_group))
print(max_age_one_relation(my_group))
print(max_age_one_friend(my_group))