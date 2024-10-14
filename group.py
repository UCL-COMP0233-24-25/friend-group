"""An example of how to represent a group of acquaintances in Python."""

my_group = {
    {
        "name": "Jill",
        "job": "biologist",
        "age": 26,
        "relations": {
        "friends": {"Zalika"},
        "partner": "John",
        },
    },
    {
        "name": "Zalika",
        "job": "artist",
        "age": 28,
        "relations":{
        "friends": {"Jill"},
        "landlord": "Nash",
        "partner": None,
        }
    },
    {
        "name": "John",
        "job": "writer",
        "age": 27,
        "relations":
        {
        "friends": set(),
        "partner": "Jill",
        },
    },
    {
        "name": "Nash",
        "job": "chef",
        "age": 34,
        "relations":
        {
        "friends": set(),
        "cousin": {"John"},
        "tenant": "Zalika",
        "partner": "Jill",
        },
    },
}
