"""An example of how to represent a group of acquaintances in Python."""


# Your code to go here...

class Group:
    def __init__(self):
        self.group = []

    def add_people(self, name, age, job):
        self.group.append({"name": name, "age": age, "job": job, "relationship": []})

    def add_relationship(self, name1, relationship, name2, both_side=True):
        for person in self.group:
            if person["name"] == name1:
                person["relationship"] += [name2, relationship]
            if person["name"] == name2 and both_side:
                person["relationship"] += [name1, relationship]

    def get_group(self):
        return self.group

    def get_max_age(self, relationship_require=False):
        max = -1
        for person in self.group:
            if not relationship_require or person["relationship"]:
                if max < person["age"]:
                    max = person["age"]

        return max

    def get_max_age_a_friend(self):
        max = -1
        for person in self.group:
            if "friend" in person["relationship"]:
                if max < person["age"]:
                    max = person["age"]

        return max

    def get_mean_age(self):
        sum_age = 0
        for person in self.group:
            sum_age += person["age"]

        return sum_age / len(self.group)


if __name__ == '__main__':
    group = Group()
    group.add_people("Jill", 24, "biologist")
    group.add_people("Zalika", 28, "artist")
    group.add_people("John", 27, "writer")
    group.add_people("Nash", 34, "chef")
    group.add_people("N", 100, "chef")

    group.add_relationship("Jill", "friend", "Zalika")
    group.add_relationship("Jill", "partner", "John")

    group.add_relationship("Nash", "cousin", "John", both_side=False)
    group.add_relationship("Nash", "landlord", "Zalika", both_side=False)

    print(group.get_group())
    print(group.get_max_age())
    print(group.get_mean_age())
    print(group.get_max_age(relationship_require=True))
    print(group.get_max_age_a_friend())