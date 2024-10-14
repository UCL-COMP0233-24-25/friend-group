"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

# Define the group of acquaintances using dictionaries and lists

# Function to add reciprocal connections
# Define the group of people
group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "relations": {
            "Zalika": "friend",
            "John": "partner"
        }
    },
    "Zalika": {
        "age": 28,
        "job": "artist",
        "relations": {
            "Jill": "friend"
        }
    },
    "John": {
        "age": 27,
        "job": "writer",
        "relations": {
            "Jill": "partner"
        }
    },
    "Nash": {
        "age": 34,
        "job": "chef",
        "relations": {
            "John": "cousin",
            "Zalika": "landlord"
        }
    }
}

# Calculating the maximum age of people in the group
max_age = max(person["age"] for person in group.values())

# Calculating the average number of relations among members of the group
mean_relations = sum(len(person["relations"]) for person in group.values()) / len(group)

# Calculating the maximum age of people with at least one relation
max_age_with_relations = max(person["age"] for person in group.values() if len(person["relations"]) > 0)

# [Advanced] Calculating the maximum age of people with at least one friend
max_age_with_friend = max(
    (person["age"] for person in group.values() if "friend" in person["relations"].values()), default=None
)

# Display results
print(f"The maximum age of people in the group: {max_age}")
print(f"The average (mean) number of relations among members of the group: {mean_relations}")
print(f"The maximum age of people with at least one relation: {max_age_with_relations}")
print(f"The maximum age of people with at least one friend: {max_age_with_friend}")
