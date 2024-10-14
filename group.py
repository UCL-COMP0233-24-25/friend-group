"""An example of how to represent a group of acquaintances in Python."""

#For the relationship of each person, it is like: the front person is the “relationship” of the behind person. 
my_group = {
    "Jill":{"age":26,"job":"biologist","realtionship":{"friend":["Zalika"],"partner":["John"]}},
    "Zalika":{"age":28,"job":"artist","realtionship":{"friend":["Jill"]}},
    "John":{"age":27,"job":"writer","realtionship":{"partner":["Jill"]}},
    "Nash":{"age":34,"job":"chef","realtionship":{"landlord":["Zalika"]}},
}
