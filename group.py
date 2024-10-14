"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {"Jill":
            {"Job":"Biologist", "Age":"26", "Relations":[("Zalika","Friend"),("John","partner")]},
            "Zalika":
            {"Job":"Artist", "Age":"28", "Relations":[("Jill","Friend")]},    
            "John":
            {"Job":"Writer", "Age":"27", "Relations":[("Zalika","Partner")]},
            "Nash":
            {"Job":"Chef", "Age":"34", "Relations":[("John","Cousin"),("Zalika","Landlord")]}}
 
print(my_group["Jill"]["Relations"][0])