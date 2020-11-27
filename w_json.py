import json

with open('json_1.json') as f:
    file=json.load(f)
    print(file)

with open('json_2.json','w') as f:
    json.dump(file,f)



