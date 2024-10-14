"""An example of how to represent a group of acquaintances in Python."""
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
