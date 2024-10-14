"""An example of how to represent a group of acquaintances in Python."""

#For the relationship of each person, it is like: the front person is the “relationship” of the behind person. 
my_group = {
    "Jill":{"age":26,"job":"biologist","relationship":{"friend":["Zalika"],"partner":["John"]}},
    "Zalika":{"age":28,"job":"artist","relationship":{"friend":["Jill"]}},
    "John":{"age":27,"job":"writer","relationship":{"partner":["Jill"]}},
    "Nash":{"age":34,"job":"chef","relationship":{"landlord":["Zalika"]}},
}

import numpy as np

max_age = np.max([my_group[person]['age'] for person in my_group])
print('the maximum age of people in the group is',max_age)

average_rel = np.average([len(my_group[person]['relationship']) for person in my_group])
print('the average (mean) number of relations among members of the group is',average_rel)

max_con_age = np.max([my_group[person]['age'] for person in my_group if len(my_group[person]['relationship']) >= 1 ])
print('the maximum age of people in the group that have at least one relation is',max_con_age)

max_fricon_age = np.max([my_group[person]['age'] for person in my_group if 'friend' in my_group[person]['relationship'] and len(my_group[person]['relationship']['friend']) >= 1 ])
print('the maximum age of people in the group that have at least one friend is', max_fricon_age)