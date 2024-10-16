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


if __name__ == "__main__":
    print_my_group()

