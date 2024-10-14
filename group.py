"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = [
    {
        "name": "Jill",
        "job": "biologist",
        "age": 26,
        "friends": {"Zalika"},
        "partner": "John",
    },
    {
        "name": "Zalika",
        "job": "artist",
        "age": 28,
        "friends": {"Jill"},
        "landlord": "Nash",
        "partner": None,
    },
    {
        "name": "John",
        "job": "writer",
        "age": 27,
        "friends": {},
        "partner": "Jill",
    },
    {
        "name": "Nash",
        "job": "chef",
        "age": 34,
        "friends": {},
        "cousin": {"John"},
        "tenant": "Zalika",
        "partner": "Jill",
    },
]
