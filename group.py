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

ages = []

print('the maximum age of people in the group:')
for person in my_group:
    ages.append(my_group[person]['age'])

print(max(ages))

relation_num = 0
person_num = 0
print('the average (mean) number of relations among members of the group:')
for person in my_group:
    relation_num += len(my_group[person]['connections'])
    person_num += 1

print(relation_num/person_num)

ages_with_relation = []
print('the maximum age of people in the group that have at least one relation:')
for person in my_group:
    if len(my_group[person]['connections']) != 0:
        ages_with_relation.append(my_group[person]['age'])
print(max(ages_with_relation))

print('[more advanced] the maximum age of people in the group '
      'that have at least one friend')

ages_with_friend = []
print('the maximum age of people in the group that have at least one friend:')
for person in my_group:
    if len(my_group[person]['connections']) != 0:
        connection =  my_group[person]['connections']
        if 'friend' in connection:
            ages_with_friend.append(my_group[person]['age'])

print(max(ages_with_friend))
