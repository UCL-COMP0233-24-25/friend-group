"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

class persons:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.relation = {}

    def add_relation(self, add_name, add_age, add_relation, job = None):
        self.relation[add_name] = [add_age, add_relation, job]


Shyam = persons("Shyam", 25)       

Shyam.add_relation("Daniel", 25, "friend", "doctor")
Shyam.add_relation("John", 26, "boss")
lists = Shyam.relation
print(lists)