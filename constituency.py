import json

with open('test.json', 'r') as f:
    test_dict = json.load(f)

for test in test_dict:
    const = (test['candidate']['name'])
    print(const)
