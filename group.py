"""An example of how to represent a group of acquaintances in Python."""

#For the relationship of each person, it is like: the front person is the “relationship” of the behind person. 
my_group = {
    "Jill":{"age":26,"job":"biologist","relationship":{"friend":["Zalika"],"partner":["John"]}},
    "Zalika":{"age":28,"job":"artist","relationship":{"friend":["Jill"]}},
    "John":{"age":27,"job":"writer","relationship":{"partner":["Jill"]}},
    "Nash":{"age":34,"job":"chef","relationship":{"landlord":["Zalika"]}},
}

import numpy as np
import json
import yaml

try:
    my_group
except NameError:
    print("Error: my_group is not defined!")
else:
    print("my_group exists and is ready to use.")

try:
    max_age = np.max([my_group[person]['age'] for person in my_group])
    print('the maximum age of people in the group is',max_age)
except Exception as e:
    print('Error occurs when calculating.')

try:
    average_relation = np.average([len(my_group[person]['relationship']) for person in my_group])
    print('the average (mean) number of relations among members of the group is',average_relation)
except Exception as e:
    print('Error occurs when calculating.')

try:
    con_age1 = np.max([my_group[person]['age'] for person in my_group if len(my_group[person]['relationship']) >= 1 ])
    print('the maximum age of people in the group that have at least one relation is',con_age1)
except Exception as e:
    print('Error occurs when calculating.')

try:
    con_age2 = np.max([my_group[person]['age'] for person in my_group if 'friend' in my_group[person]['relationship'] and len(my_group[person]['relationship']['friend']) >= 1 ])
    print('the maximum age of people in the group that have at least one friend is', con_age2)  
except Exception as e:
    print('Error occurs when calculating.')

#save my_group as JSON file:
with open('my_group.json','w') as f:
    json.dump(my_group,f)

#read my_group.json file:
with open('my_group.json','r') as f:
    group_json = json.load(f) #also can use group_json = f.read()
print(group_json)

#save my_group as YAML file:
with open('my_group.yaml','w') as f:
    yaml.dump(my_group,stream = f)

#read my_group.yaml file:
with open('my_group.yaml','r') as f:
    group_yaml = yaml.safe_load(f) #also can use group_json = f.read()
print(group_yaml)
