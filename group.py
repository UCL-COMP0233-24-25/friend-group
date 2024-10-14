"""An example of how to represent a group of acquaintances in Python."""

# Creates a dictionary of dictionaries...

my_group = {"Jill":
            {"Job":"Biologist", "Age":"26", "Relations":[("Zalika","Friend"),("John","partner")]},
            "Zalika":
            {"Job":"Artist", "Age":"28", "Relations":[("Jill","Friend")]},    
            "John":
            {"Job":"Writer", "Age":"27", "Relations":[("Zalika","Partner")]},
            "Nash":
            {"Job":"Chef", "Age":"34", "Relations":[("John","Cousin"),("Zalika","Landlord")]}}
 
 # to access use my_group["Jill"].values() will give values or my_group["Jill"]["Relations"][0]

print(my_group["Jill"]["Relations"][0])