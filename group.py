"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = [
    {"name" : "Jill",
     "age" : 26,
     "job" : "biologist",
     "relationships":[
    {"name": "Zalika", "relation": "Friend"},
     {"name": "John", "relation": "Partner"}
     ]
    },


    {"name" : "Zalika",
     "age" : 28,
     "job" : "Artist",
     "relationships":[
     {"name": "Jill", "relation": "Friend"}
     ]
    },

    {"name" : "John",
     "age" : 27,
     "job" : "Writer",
     "relationships":[
     {"name": "Jills", "relation": "Partner"}
     ]
     },

    {"name" : "Nash",
     "age" : 34,
     "job" : "Chef",
     "relationships":[
     {"name": "John", "relation": "cousin"},
     {"name": "Zalika", "relation": "landlord"}

     ]
     }
    
]
