"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {"Jill":
            {"Job":"Biologist", "Age":"26", "Relations":[("Zalika","Friend"),("John","Partner")]},
            "Zalika":
            {"Job":"Artist", "Age":"28", "Relations":[("Jill","Friend")]},    
            "John":
            {"Job":"Writer", "Age":"27", "Relations":[("Zalika","Partner")]},
            "Nash":
            {"Job":"Chef", "Age":"34", "Relations":[("John","Cousin"),("Zalika","Landlord")]}}
 

def age_relation_info(group=my_group):
    age_vec = []
    age_relat_vec = []
    age_friend_vec = []
    relation_vec = []
    for key in group:
        age_vec.append(int(group[key]["Age"]))
        if group[key]["Relations"]:
            relation_vec.append(len(group[key]["Relations"]))
            age_relat_vec.append(int(group[key]["Age"]))
            for relation in group[key]["Relations"]:
                if "Friend" in relation:
                    age_friend_vec.append(int(group[key]["Age"]))

    return(
        f"Max Age: {max(age_vec)};  Average Relations: {sum(relation_vec)/len(group)};  Max Age with >=1 Relation: {max(age_relat_vec)};  Max Age with >=1 Friend: {max(age_friend_vec)}"
    )

age_relation_info()
