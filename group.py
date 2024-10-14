"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
week3_group=[{
"name":"Jill","age":26,"job":"biologist"   
,"connections":[{"name":"Zalika","relationship":"friend"},{"name":"John","relationship":"partner"}]},

{
"name":"Zalika","age":28,"job":"artist"   
,"connections":[{"name":"Jill","relationship":"friend"}]},

{
"name":"John","age":27,"job":"writer"   
,"connections":[{"name":"Jill","relationship":"partner"}]},

{"name":"Nash","age":34,"job":"chef"   
,"connections":[{"name":"John","relationship":"cousin"},{"name":"Zalika","relationship":"landlord"}]}
]
# my_group =

#Code for Maximum Age
max_age = max([x["age"] for x in week3_group])
#Code for Average number of connections
ave_connections = sum(len(x["connections"]) for x in week3_group) / len(week3_group)
#Code for max age of people in the group that have at least 1 relation
maxage1= max([x["age"] for x in week3_group if len(x["connections"])>0])