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


for row in my_group:  
    connections = " and ".join([f"{v[0]}'s {k}" for k, v in row['connection'].items()])
    print(f"{row['name']} is {row['age']}, {row['job']}, {connections}")




