"""An example of how to represent a group of acquaintances in Python."""

my_group = {
    "Jill": {
        "age": 26,
        "profession": "biologist",
        "friend": "Zalika",
        "partner": "John"
    },
    "Zalika": {
        "age": 28,
        "profession": "artist",
        "friend": "Jill"
    },
    "John": {
        "age": 27,
        "profession": "writer",
        "partner": "Jill",
        "cousin": "Nash"
    },
    "Nash": {
        "age": 34,
        "profession": "chef",
        "cousin": "John",
        "landlord": "Zalika"
    }
}

# 1. The maximum age of people in the group
max_age = max(person["age"] for person in my_group.values())
print(f"The maximum age of people in the group: {max_age}")

# 2. The average (mean) number of relations among members of the group
# Relations: each key except "age" and "profession" is considered a relation
avg_relations = sum(len([k for k in person.keys() if k not in ["age", "profession"]]) for person in my_group.values()) / len(my_group)
print(f"The average number of relations among members: {avg_relations:.2f}")

# 3. The maximum age of people in the group that have at least one relation
# Relation is defined as having any key other than "age" and "profession"
max_age_with_relations = max(
    person["age"] for person in my_group.values()
    if any(k not in ["age", "profession"] for k in person.keys())
)
print(f"The maximum age of people with at least one relation: {max_age_with_relations}")

# 4. [Advanced] The maximum age of people in the group that have at least one friend
# A friend is defined by the key "friend" in the dictionary
max_age_with_friend = max(
    person["age"] for person in my_group.values()
    if "friend" in person
)
print(f"The maximum age of people with at least one friend: {max_age_with_friend}")
