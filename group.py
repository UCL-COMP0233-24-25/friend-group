"""An example of how to represent a group of acquaintances in Python."""
import numpy as np

#For the relationship of each person, it is like: the front person is the “relationship” of the behind person. 
my_group = {
    "Jill":{"age":26,"job":"biologist","relationship":{"friend":["Zalika"],"partner":["John"]}},
    "Zalika":{"age":28,"job":"artist","relationship":{"friend":["Jill"]}},
    "John":{"age":27,"job":"writer","relationship":{"partner":["Jill"]}},
    "Nash":{"age":34,"job":"chef","relationship":{"landlord":["Zalika"]}},
}


# Max Age
print("Max age:", end=" ")
print(np.max([my_group[person]["age"] for person in my_group]))

# Average Relation
print("Average relationship", end=" ")
print(np.mean([len(my_group[person]["relationship"]) for person in my_group]))

# Max age with at least one relation
print("Max age with at least one relation:", end=" ")
print(np.max([my_group[person]["age"] for person in my_group if len([my_group[person]["relationship"]])>=1]))

# the maximum age of people in the group that have at least one friend
print("Max age with at least one friend:", end=" ")
print(np.max([my_group[person]["age"] for person in my_group if 'friend' in my_group[person]["relationship"]]))

