"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

class persons:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.relation = {}

    def add_relation(self, add_name, add_relation):
        self.relation[add_name] = add_relation

Daniel = persons("Daniel", 24)
Shyam = persons("Shyam", 25)       

Shyam.add_relation("Daniel", "friend")
lists = Shyam.relation
print(lists)