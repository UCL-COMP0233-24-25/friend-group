"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = [
    {
        "Name": "Jill",
        "Age": 26,
        "Job": "Biologist",
        "Connections": {"Friends": ["Zalika"], 
                        "Partner": "John"}
    },
    {
        "Name": "Zalika",
        "Age": 28,
        "Job": "Artist",
        "Connections": {"Friends": ["Jill"], 
                        "Landlord": "Nash"}
    },
    {
        "Name": "John",
        "Age": 27,
        "Job": "Writer",
        "Connections": {"Partner": "Jill"}
    },
    {
        "Name": "Nash",
        "Age": 34,
        "Job": "Chef",
        "Connections": {"Cousins": ["John"], 
                        "Tennants": ["Zalika"]}
    }
]

