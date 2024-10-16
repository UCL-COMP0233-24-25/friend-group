"""An example of how to represent a group of acquaintances in Python."""

# Creates a dictionary of dictionaries...

my_group = {"Jill":
            {"Job":"Biologist", "Age":26, "Relations":{"Zalika":"Friend", "John":"partner"}},
            "Zalika":
            {"Job":"Artist", "Age":28, "Relations":{"Jill":"Friend"}},    
            "John":
            {"Job":"Writer", "Age":27, "Relations":{"Zalika":"Partner"}},
            "Nash":
            {"Job":"Chef", "Age":34, "Relations":{"John":"Cousin","Zalika":"Landlord"}},
            "Steve":
            {"Job":"Toy", "Age":40, "Relations":{"John":"Friend","Nash":"Owner"}}}

# to access use my_group["Jill"].values() will give values or my_group["Jill"]["Relations"][0]
# ruff from command palette, ctrl shift p and format document will tidy up your code
x=0
i=0
z=0
p=0
w=0
for y in my_group:
    i+=1
    if my_group[y]["Age"] > x:
        x = my_group[y]["Age"]

    z+= len(my_group[y]["Relations"])

    if len(my_group[y]["Relations"]):
        if my_group[y]["Age"] > p:
            p= my_group[y]["Age"]

    if len(my_group[y]["Relations"]):
        for a in my_group[y]["Relations"].values():
            if a == "Friend":
                if my_group[y]["Age"] > w:
                    w = my_group[y]["Age"]


print(x) # max age
print(z/i) # mean number of relations
print(p) # max age of people with at least one relation
print(w) # max age of people that have a friend

