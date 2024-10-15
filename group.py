"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
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


print("Max age: ", max(x["age"] for x in group.values()) )

relations = sum(len(x["relations"]) for x in group.values())
average = relations /len(group) if len(group) > 0 else 0
print("The average: ", average)


print("Max age : ",  max(x["age"] for x in group.values() if len(x["relations"]) > 0) )

print("Max age with friend:",max((x["age"] for x in group.values() if "friend" in x["relations"].values())) )

