"""An example of how to represent a group of acquaintances in Python."""
class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
        self.friends = []

    def add_friend(self,relationship, friend):
        self.friends.append({friend:relationship})

    def is_friends_with(self, friend):
        return friend in self.friends
    
    def __str__(self):
        relationships = []
        for friend in self.friends:
            for key, value in friend.items():
                relationships.append(f"{key}'s {value}")
        relationships_str = ' and '.join(relationships)
        print(f"{self.name} is {self.age}, a {self.job} and she is {relationships_str}.")
        return ""
    
## Jill is 26, a biologist and she is Zalika's friend and John's partner.
Jill = Person("Jill", 26, "biologist")
Jill.add_friend("friend", "Zalika")
Jill.add_friend("partner", "John")
str(Jill)


#Zalika is 28, an artist, and Jill's friend
Zalika = Person("Zalika", 28, "artist")
Zalika.add_friend("friend", "Jill")
str(Zalika)

#John is 27, a writer, and Jill's partner.
John = Person("John", 27, "writer")
John.add_friend("partner", "Jill")
str(John)

#Nash is 34, a chef, John's cousin and Zalika's landlord.
Nash = Person("Nash", 34, "chef")
Nash.add_friend("cousin", "John")
Nash.add_friend("landlord", "Zalika")
str(Nash)