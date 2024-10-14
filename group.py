"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    "Jill":{
        "age":26,
        "job":"biologist",
        "relationships": {
            "Zalika":"friend",
            "John":"partner",
        }
    },
    "Zalika":{
        "age":28,
        "job":"artist",
        "relationships":{
            "Jill":"friend",
        }
    }, # type: ignore
    "John":{
        "age":27,
        "job":"writer",
        "relationships":{
            "Jill":"partner",
        }
    },
    "Nash":{
        "age":33,
        "job":"chef",
        "relationships":{
            "John":"cousin",
            "Zalika":"landlord",
        }
    }
}
print(my_group)


