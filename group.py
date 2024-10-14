"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = [
    {
        "name": "Jill",
        "age": 26,
        "job": "Biologist",
        "connections": [
            {"name": "Zalika", "relationship": "friend"},
            {"name": "John", "relationship": "partner"}
        ]
    }, 
    {
        "name": "Zalika",
        "age": 28,
        "job": "Artist",
        "connections": [
            {"name": "Jill", "relationship": "friend"}
        ]
    }, 
    {
        "name": "John",
        "age": 27,
        "job": "Writer",
        "connections": [
            {"name": "Jill", "relationship": "partner"},
            {"name": "Nash", "relationship": "cousin"}
        ]
    }, 
    {
        "name": "Nash",
        "age": 34,
        "job": "Chef",
        "connections": [
            {"name": "John", "relationship": "cousin"},
            {"name": "Zalika", "relationship": "landlord"}
        ]
    }
]

def print_my_group():
    for people in my_group:
        print(f"{people['name']} is {people['age']}, a/an {people.get('job', 'No job')}, ", end='')
        connections = [f"{connection['name']}'s {connection['relationship']}" for connection in people['connections']]
        print(f"{' and '.join(connections)}")

print_my_group()