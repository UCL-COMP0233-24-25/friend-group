"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

sergi_rel = {"friends": ["Angadh", "Jonathan"], "partner":''}

angadh_rel = {"friends": ["Sergi", "Jonathan"], "partner":''}

jonathan_rel = {"friends": ["Sergi", "Angadh"], "partner": 'Tiffany'}

tiffany_rel = {"friends": "", "partner": "Jonathan"}

my_group = [{"name": "Sergi" , "age": 22 , "job": "student" , "relationship": sergi_rel},
            {"name": "Angadh" , "age": 22 , "job": "student" , "relationship": angadh_rel},
            {"name": "Jonathan" , "age": 22 , "job": "student" , "relationship": jonathan_rel},
            {"name": "Tiffany" , "age": 24 , "job": "Analyst" , "relationship": tiffany_rel}]


# Jill is 26, a biologist and she is Zalika's friend and John's partner.
for row in my_group:
    print(f'{row["name"]} is {row["age"]}, (s)he is a {row["job"]} and he is friends with {row["relationship"]["friends"]} and in a romantic relationship with {row["relationship"]["partner"]}')