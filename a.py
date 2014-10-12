import json

user_data = [1,2,3,4,5]

with open('state.json', 'w') as fd:
    json.dump(user_data, fd)

with open('state.json', 'r') as fd:
    user_data2 = json.load(fd)

print user_data2
