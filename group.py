"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    "Jill":{
        "age":26,
        "job":"biologist",
        "relationships": {
            "Zalika":"friend",
            "John":"partner",
        }
    },
    "Zalika":{
        "age":28,
        "job":"artist",
        "relationships":{
            "Jill":"friend",
        }
    }, # type: ignore
    "John":{
        "age":27,
        "job":"writer",
        "relationships":{
            "Jill":"partner",
        }
    },
    "Nash":{
        "age":33,
        "job":"chef",
        "relationships":{
            "John":"cousin",
            "Zalika":"landlord",
        }
    }
}
print(my_group)

""" functions to act on the group of people"""

def average_age(group):
    """Compute the average age of the group's members."""
    all_ages = [person["age"] for person in group.values()]
    return sum(all_ages) / len(group)


def forget(group, person1, person2):
    """Remove the connection between two people."""
    group[person1]["relationships"].pop(person2, None)
    group[person2]["relationships"].pop(person1, None)


def add_person(group, new_person):
    """Add a new person with the given characteristics to the group.
        name in dictionary format: name, age, job, relations"""
    group[new_person] = new_person

"""testing if all code runs as it should"""

assert len(my_group) == 4, "Group should have 4 members"
assert average_age(my_group) == 28.5, "Average age of the group is incorrect!"
forget(my_group, "Nash", "John")
assert len(my_group["Nash"]["relationships"]) == 1, "Nash should only have one relation"
print("All assertions have passed!")