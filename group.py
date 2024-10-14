"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    'Jill': {
        'age': 26,
        'job': 'biologist',
        'connections': {
            'Zalika': 'friend',
            'John': 'partner'
        }
    },
    'Zalika': {
        'age': 28,
        'job': 'artist',
        'connections': {
            'Jill': 'friend',
            'Nash': 'tenant'
        }
    },
    'John': {
        'age': 27,
        'job': 'writer',
        'connections': {
            'Jill': 'partner',
            'Nash': 'cousin'
        }
    },
    'Nash': {
        'age': 34,
        'job': 'chef',
        'connections': {
            'John': 'cousin',
            'Zalika': 'landlord'
        }
    }
}

# Quick test - printing who knows who
for name1 in my_group.keys():
    if my_group[name1]['connections']:
        for name2 in my_group[name1]['connections']:
            print(f'{name1} knows {name2}')
