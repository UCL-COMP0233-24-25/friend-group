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
# print(my_group)


# Exercise 7 

# Print max age
def get_max_age(dict):
    '''Input a dictionary {"name" :{"age":_}}
    Return: max age of person in group and their name'''
    max_age=0
    for name in dict:
        age = dict[name]["age"]
        if age > max_age:
            max_age = age
            oldest_person = name
    return max_age, oldest_person

print(get_max_age(my_group))


# 
