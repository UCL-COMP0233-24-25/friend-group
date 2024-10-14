"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

# Jill is 26, a biologist and she is Zalika's friend and John's partner.
jill = {
    "name": "Jill",
    "age": 26,
    "job": "biologist",
    "connections": [
        {
            "zalinka": zalinka,
            "connection": "friend"
        },
        {
            "john": john,
            "connection": "partner"

        }
    ]
}

# Zalika is 28, an artist, and Jill's friend
zalinka = {
    "name": "Zalinka",
    "age": 28,
    "job": "artist",
    "connections": [
        {
            "jill": jill,
            "connection": "friend"
        },
    ]
}

# John is 27, a writer, and Jill's partner.
john = {
    "name": "John",
    "age": 27,
    "job": "writer",
    "connections": [
        {
            "jill": jill,
            "connection": "partner"
        },
    ]
}

# Nash is 34, a chef, John's cousin and Zalika's landlord.
nash = {
    "name": "Nash",
    "age": 34,
    "job": "chef",
    "connections": [
        {
            "john": john,
            "connection": "counsin"
        },
        {
            "zalinka": zalinka,
            "connection": "landlord"
        },
    ]
}

my_group = [jill, zalinka, john, nash]
