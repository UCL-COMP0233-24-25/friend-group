"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = [
    {
        'name': 'Jill',
        'age': 26,
        'job':'a biologist',
        'connection': {
            'friend': ['Zalika'],
            'partner': ['John']
        }
    },
    {
        'name': 'Zalika',
        'age': 28,
        'job':'an artist',
        'connection': {
            'friend' : ['Jill']
            }
    },
    {
        'name': 'John',
        'age': 27,
        'job':'a writer',
        'connection': {
            'partner' : ['Jill']
            }
    },
    {
        'name': 'Nash',
        'age': 34,
        'job':'a chef',
        'connection': {
            'cousin' : ['John'], 
            'landlord' : ['Zalika']
            }
    }
]

def print_my_group():
    for row in my_group:
        connections = " and ".join([f"{', '.join(map(str, v))}'s {k}" for k, v in row["connection"].items() if v])
        print(f"{row['name']} is {row['age']}, {row['job']}, {connections}")
    print("\n")



# the maximum age of people in the group
max_age = max([v['age'] for v in my_group])
print(f'the maximum age of people in the group is {max_age}')

# the average (mean) number of relations among members of the group
relations_count = [len(person['connection']) for person in my_group]
avg_relations = sum(relations_count) / len(relations_count)
print(f'The average (mean) number of relations among members of the group is {avg_relations:.2f}')

# the maximum age of people in the group that have at least one relation
_max_age = max([v['age'] for v in my_group if len(v['connection']) > 0])
print(f'the maximum age of people in the group that have at least one relation is {_max_age}')

# [more advanced] the maximum age of people in the group that have at least one friend
_max_age_ = max([v['age'] for v in my_group if 'friend' in v['connection'] and v['connection']['friend']])
print(f'the maximum age of people in the group that have at least one friend is {_max_age_}')