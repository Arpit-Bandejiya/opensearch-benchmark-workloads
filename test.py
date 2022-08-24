import json

my_dict = {'id': None}
with open('my_dict.json', 'w') as f:
    json.dump(my_dict, f)

if my_dict['id']:
    print("this is it")
print("obvi")
# elsewhere...

with open('my_dict.json') as f:
    my_dict = json.load(f)
    print(my_dict)