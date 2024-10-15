"""An example of how to represent a group of acquaintances in Python."""

my_group = [
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
        "relations": {
            "friends": {"Jill"},
            "landlord": "Nash",
            "partner": None,
        },
    },
    {
        "name": "John",
        "job": "writer",
        "age": 27,
        "relations": {
            "friends": set(),
            "partner": "Jill",
        },
    },
    {
        "name": "Nash",
        "job": "chef",
        "age": 34,
        "relations": {
            "friends": set(),
            "cousin": {"John"},
            "tenant": "Zalika",
            "partner": None,
        },
    },
]

if __name__== "__main__":   
    max_age = max([person["age"] for person in my_group])
    no_of_relations = (sum([len(person["relations"]) for person in my_group])/len([len(person["relations"]) for person in my_group]))
    max_age_relations = max([person["age"] for person in my_group if len(person["relations"])>1])
    # max([person["age"] for person in my_group if "friend" in person["relations"].keys()])

