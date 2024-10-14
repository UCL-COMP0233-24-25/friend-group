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
    },
    "Bill":{
        "age":35,
        "job":"chef",
        "relationships":{}
    }
}
# print(my_group)


# Exercise 7 

# Print max age
def get_max_age(dict):
    '''Input a dictionary {"name" :{"age":_}, ...}
    Return: max age of person in group and their name'''
    max_age=0
    for name in dict:
        age = dict[name]["age"]
        if age > max_age:
            max_age = age
            oldest_person = name
    return max_age, oldest_person

print(f'Max age of person in group and their name: {get_max_age(my_group)}.')


# Average number of relations

def get_average_number_relations(dict):
    '''Input: dictionary {"name" :{"relationships":{"relation_name":"relaiton",...},...},...}
    Output: mean number of relationships per person in group'''
    number_relations=0
    number_poeple =0
    for name in dict:
        number_relations += len(dict[name]["relationships"])
        number_poeple +=1
    return number_relations/number_poeple

print(f"Average number of relationships per person in group {get_average_number_relations(my_group)}.")


# Make age of people in group that have at least one relation

def max_age_of_social_people(dict):
    '''Input a dictionary {"name" :{"age":_}, ...}
    Return: max age of person in group and their name, if they have at least one person in relationships'''
    max_age=0
    for name in dict:
        age = dict[name]["age"]
        if len(dict[name]["relationships"])>0:
            if age > max_age:
                max_age = age
                oldest_person = name
    return max_age, oldest_person

print(f'Max age of person - with at least one relationship - in group and their name: {max_age_of_social_people(my_group)}.')


# Make age of people in group that have at least one friend

def max_age_of_friended_people(dict):
    '''Input a dictionary {"name" :{"age":_}, ...}
    Return: max age of person in group and their name, if they have at least one person in relationships'''
    max_age=0
    for name in dict:
        age = dict[name]["age"]
        if 'friend' in dict[name]["relationships"].values():
            if age > max_age:
                max_age = age
                oldest_person = name
    return max_age, oldest_person

print(f'Max age of person - with at least one friend - in group and their name: {max_age_of_friended_people(my_group)}.')
