import json

with open('my_file.json', 'r') as f:
     loaded_json_string = f.read()
#print(loaded_json_string)

loaded_data = json.loads(loaded_json_string)
print(f"loaded_data = {loaded_data}")
print(f"type(loaded_data) = {type(loaded_data).__name__}")
print(f"type(loaded_data['foo']) = {type(loaded_data['Jill']).__name__}")

print(type(loaded_json_string))
