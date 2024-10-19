"""An example of how to represent a group of acquaintances in Python."""
import numpy as np

#For the relationship of each person, it is like: the front person is the “relationship” of the behind person. 
# A with relationship "rel": [B] means A is B's rel, while A with relation_from "rel": [B] means B is A's rel.
my_group = {
    "Jill":{"age":26,
            "job":"biologist",
            "relationship":{"friend":["Zalika"],"partner":["John"]},
            "relation_from":{"friend":["Zalika"],"partner":["John"]}
            },
    "Zalika":{"age":28,
              "job":"artist",
              "relationship":{"friend":["Jill"]},
              "relation_from":{"friend":["Jill"], "landlord":["Nash"]}
              },
    "John":{"age":27,
            "job":"writer",
            "relationship":{"partner":["Jill"], "cousin": ["Nash"]},
            "relation_from":{"partner":["Jill"], "cousin":["Nash"]}
            },
    "Nash":{"age":34,
            "job":"chef",
            "relationship":{"landlord":["Zalika"], "cousin":["John"]},
            "relation_from":{"cousin": ["John"]}
    }
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

