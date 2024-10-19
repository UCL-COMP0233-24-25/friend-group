"""An example of how to represent a group of acquaintances in Python and perform some analytical calculations on the group."""

# Define the group of acquaintances using dictionaries and lists

def add_reciprocal_relations(group):
    """
    Function to add reciprocal relationships in the group dictionary.
    For example, if person A is a landlord of person B, then person B is a tenant of person A.
    """
    for person_name, person_data in group.items():
        for relation_name, relation_type in person_data['relations'].items():
            if relation_type == 'cousin':
                # Cousins are bidirectional
                if person_name not in group[relation_name]['relations']:
                    group[relation_name]['relations'][person_name] = 'cousin'
            elif relation_type == 'landlord':
                # Landlord-tenant is a bidirectional relationship
                if person_name not in group[relation_name]['relations']:
                    group[relation_name]['relations'][person_name] = 'tenant'
            elif relation_type == 'tenant':
                # Tenant-landlord is a bidirectional relationship
                if person_name not in group[relation_name]['relations']:
                    group[relation_name]['relations'][person_name] = 'landlord'
            elif relation_type == 'friend':
                # Friend relationships are bidirectional
                if person_name not in group[relation_name]['relations']:
                    group[relation_name]['relations'][person_name] = 'friend'
            elif relation_type == 'partner':
                # Partner relationships are bidirectional
                if person_name not in group[relation_name]['relations']:
                    group[relation_name]['relations'][person_name] = 'partner'

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

# Adding reciprocal relations to the group
add_reciprocal_relations(group)

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
