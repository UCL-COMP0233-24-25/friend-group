"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

connections = ["friend","partner","landlord","cousin","tenant"]
my_group = {
    "Jill":{
        "age":26,
        "job":"biologist",
        "connections":{
            "Zalika":connections[0],
            "John":connections[1]
        }
    },
    "Zalika":{
        "age":28,
        "job":"artist",
        "connections":{
            "Jill":connections[0],
            "Nash":connections[4]
        }
    },
    "John":{
        "age":27,
        "job":"writer",
        "connections":{
            "Jill":connections[1],
            "Nash":connections[3]
        }
    },
    "Nash":{
        "age":34,
        "job":"chef",
        "connections":{
            "Zalika":connections[2],
            "John":connections[3]
        }
    }
    
}
