"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

# Jill is 26, a biologist and she is Zalika's friend and John's partner.
jill = {
    "name": "Jill",
    "age": 26,
    "job": "biologist",
    "connections": [
        {"name": "Zalinka", "connection": "friend"},
        {"name": "John", "connection": "partner"},
    ],
}

# Zalika is 28, an artist, and Jill's friend
zalinka = {
    "name": "Zalinka",
    "age": 28,
    "job": "artist",
    "connections": [
        {"name": "Jill", "connection": "friend"},
    ],
}

# John is 27, a writer, and Jill's partner.
john = {
    "name": "John",
    "age": 27,
    "job": "writer",
    "connections": [
        {"name": "Jill", "connection": "partner"},
    ],
}

# Nash is 34, a chef, John's cousin and Zalika's landlord.
nash = {
    "name": "Nash",
    "age": 34,
    "job": "chef",
    "connections": [
        {"name": "John", "connection": "counsin"},
        {"name": "Zalinka", "connection": "landlord"},
    ],
}

my_group = [jill, zalinka, john, nash]


def max_age(group):
    """Returns the maximum age of people in the group."""
    return max(person["age"] for person in group)


def average_relations(group):
    """Returns the average number of connections (relations) among members of the group."""
    total_connections = sum(len(person["connections"]) for person in group)
    return total_connections / len(group)


def max_age_with_relations(group):
    """Returns the maximum age of people in the group that have at least one connection."""
    people_with_relations = [person["age"] for person in group if person["connections"]]
    return max(people_with_relations) if people_with_relations else None


def max_age_with_friends(group):
    """Returns the maximum age of people in the group that have at least one friend."""
    people_with_friends = [
        person["age"]
        for person in group
        if any(
            connection["connection"] == "friend" for connection in person["connections"]
        )
    ]
    return max(people_with_friends) if people_with_friends else None


max_age_result = max_age(my_group)
average_relations_result = average_relations(my_group)
max_age_with_relations_result = max_age_with_relations(my_group)
max_age_with_friends_result = max_age_with_friends(my_group)

print(max_age_result)
print(average_relations_result)
print(max_age_with_relations_result)
print(max_age_with_friends_result)
