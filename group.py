"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {}

Jill = {'name':'Jill', 'age':'26', 'job':'biologist',
            'connections':{'friend':['Zalika'],
                           'partner':['John']}
            }

Zalika = {'name':'Zalika', 'age':'28', 'job':'biologist',
            'connections':{'friend':['Jill']}
            }

John = {'name':'Jhon', 'age':'27', 'job':'writer',
            'connections':{'partner':['Jill']}
            }

Nash = {'name':'Nash', 'age':'34', 'job':'chef',
            'connections':{'cousin':['Jhon'],
                           'landlord':['Zalika']}
            }

my_group['Jill'] = Jill
my_group['Zalika'] = Zalika
my_group['John'] = John
my_group['Nash'] = Nash
print(my_group)