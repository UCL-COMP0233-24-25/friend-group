"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = Daniel, Shyam

class persons:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.relation = {}

    def add_relation(self, add_name, add_relation):
        self.relation[add_name] = add_relation

Daniel = persons{name=Daniel, age=23}

Shyam = persons{name=Shyam, age=}        