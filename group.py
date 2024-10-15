"""An example of how to represent a group of acquaintances in Python."""

my_group = {
    'Jill' : 
    {
        'Age' : 26,
        'Job' : ['Biologist'],
        'Connections' : {'Friend' : 'Zalika', 'Partner' : 'John'}
    },
    'Zalika' : 
    {
        'Age' : 28,
        'Job' : ['Artist'],
        'Connections' : {'Friend' : 'Jill'}
    },
    'John' : 
    {
        'Age' : 27,
        'Job' : ['Writer'],
        'Connections' : {'Partner' : 'Jill'}
    },
    'Nash' : 
    {
        'Age' : 34,
        'Job' : ['Chef'],
        'Connections' : {'Cousin' : 'John', 'Landlord' : 'Zalika'}
    }
    
}

### Issue 7 - Summary data from group ###
def max_age(my_group=my_group,ages=[]):
    for name in my_group:
        ages.append(my_group[name]['Age'])
    return(max(ages))

def mean_relations(my_group=my_group,n_relations=0):
    for name in my_group:
        n_relations += len(my_group[name]['Connections'])
    return n_relations/len(name)

def max_age_with_relation(my_group=my_group,ages=[]):
    for name in my_group:
        if len(my_group[name]['Connections']) > 0:
            ages.append(my_group[name]['Age'])
    return(max(ages))

def max_age_with_friend(my_group=my_group,ages=[]):
    for name in my_group: 
        if 'Friend' in list(my_group[name]['Connections'].keys()):
            ages.append(my_group[name]['Age'])
    return max(ages)


print(max_age())
print(mean_relations())
print(max_age_with_relation())
print(max_age_with_friend())
