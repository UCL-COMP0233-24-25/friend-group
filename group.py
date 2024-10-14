"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    "Jill": {
        "age": 26,
        "job": "Biologist",
        "connections": {
            "friend": ["Zalika"],
            "partner": ["John"]
        }
    },
    "Zalika": {
        "age": 28,
        "job": "Artist",
        "connections": {
            "friend": ["Jill"]
        }
    },
    "John": {
        "age": 27,
        "job": "Writer",
        "connections": {
            "partner": ["Jill"],
            "cousin": ["Nash"]
        }
    },
    "Nash": {
        "age": 34,
        "job": "Chef",
        "connections": {
            "cousin": ["John"],
            "landlord": ["Zalika"]
        }
    }
}

# Print out the data structure
for person, info in my_group.items():
    print(f"{person}:")
    print(f"  Age: {info['age']}")
    print(f"  Job: {info['job']}")
    print(f"  Connections: {info['connections']}\n")