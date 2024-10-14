"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group =[{ "name": "Jenny", "age": 22, "job": "Student"}, 
        { "name": "Jason", "age": 22, "job": "Student"},
        ]

for row in my_group:
   print (f"{row['name']} is {row['age']},a {row['job']}")