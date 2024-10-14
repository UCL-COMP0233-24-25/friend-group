"""An example of how to represent a group of acquaintances in Python."""

# For the relationship of each person, it is like: the front person is the “relationship” of the behind person.
# The bi_relation using the opposite key value for fast search.
my_group = {
    "Jill":{"age":26,
            "job":"biologist",
            "relationship":{"friend":["Zalika"],"partner":["John"]},
            "bi_relation": {"Zalika": ["friend"],
                            "John": ["partner"]}},
    "Zalika":{"age":28,
              "job":"artist",
              "relationship":{"friend":["Jill"]},
              "bi_relation": {"Jill": ["friend"]}},
    "John":{"age":27,
            "job":"writer",
            "relationship":{"partner":["Jill"]},
            "bi_relation":{"Jill": ["partner"]}},
    "Nash":{"age":34,
            "job":"chef",
            "relationship":{"landlord":["Zalika"]},
            "bi_relation":{"Zalika": ["landlord"]}},
}

"""
Remove any relation between person1 and person2.
"""
def forget(person1, person2):
    if person1 not in my_group:
        print(f"{person1} is not in the group.")
        return
    if person2 not in my_group:
        print(f"{person2} is not in the group.")
        return

    "Using to remove relation one side."
    def remove_relationship_by_person(person_a, person_b):
        if person_b in my_group[person_a]["bi_relation"]:
            relation_list = my_group[person_a]["bi_relation"][person_b] # get all the relations
            del my_group[person_a]["bi_relation"][person_b]
            to_remove = []
            for relation in relation_list:
                my_group[person_a]["relationship"][relation].remove(person_b)
                if len(my_group[person_a]["relationship"][relation]) == 0:
                    to_remove.append(relation)
            for relation in to_remove:
                del my_group[person_a]["relationship"][relation]

    remove_relationship_by_person(person1, person2)
    remove_relationship_by_person(person2, person1)

    return

"""
Add a new person into my_group
The relation should be in format with "relationship" part, not "bi_relation"
"""
def add_person(new_name, age, job=None, relations=None):
    
    if relations is None:
        relations = {}
    if new_name in my_group:
        print(f"{new_name} is already in my_group.")
        return

    def spawn_bi_relation(_relations):
        bi_relation = {}
        for relation in _relations:
            names = _relations[relation]
            for _name in names:
                re_list = []
                if _name in bi_relation:
                    re_list = bi_relation[_name]
                re_list.append(relation)
                bi_relation[_name] = re_list
        return bi_relation
     
    my_group[new_name] = {'age':age, 'job':job, 'relationship':relations, 'bi_relation': spawn_bi_relation(relations)}

    def add_relation(target, new_person, relation):
        # process relationship
        lst = []
        if relation in my_group[target]['relationship']:
            lst = my_group[target]['relationship'][relation]
        lst.append(new_person)
        my_group[target]['relationship'][relation] = lst

        # process bi_relationship
        lst = []
        if new_person in my_group[target]['bi_relation']:
            lst = my_group[target]['bi_relation'][new_person]
        lst.append(relation)
        my_group[target]['bi_relation'][new_person] = lst

    for relation in relations:
        names = relations[relation]
        for name in names:
            add_relation(name, new_name, relation)

    return


def average_age():
    
    import numpy as np
    
    n = len(my_group.keys())
    ages = np.zeros(n)
    for i, (person, info) in enumerate(my_group.items()):
        ages[i] = info['age']
    average_age = np.average(ages)

    return average_age

def better_print():
    for name in my_group:
        print(f"Name: {name}")
        print(f"Age: {my_group[name]['age']}")
        if my_group[name]['job'] is not None:
            print(f"Job: {my_group[name]['job']}")
        else:
            print(f"No Job")

        if not my_group[name]['relationship'] == {}:
            print(f"Relations:")
            for relation in my_group[name]['relationship']:
                print(f"\t{relation}:", end=" ")
                names = my_group[name]['relationship'][relation]
                for i in range(len(names)):
                    print(f"{names[i]}", end = "")
                    if i < len(names)-1:
                        print(", ", end = "")
                    else:
                        print("")

        print("")


if __name__ == "__main__":
    better_print()
    print("---------------------------------------------")

    # test for add person
    add_person("Li", 999, relations={'friend': ['John','Jill'], 'fellow': ['Zalika']})
    better_print()
    print("---------------------------------------------")

    # test for forget relation
    forget("Li", "Jill")
    better_print()
    print("---------------------------------------------")
    forget("Nash", "Zalika")
    better_print()
