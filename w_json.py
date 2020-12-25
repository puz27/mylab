import json
import requests

with open('json_1.json') as f:
    file=json.load(f)
    print(file)

with open('json_2.json','w') as f:
    json.dump(file,f)

uri = 'https://portal5.cbr.ru/back/rapi2/Messages/?MinDateTime=$date&type=inbox'
user = '89avramenkoNV007750004231'
passw = ''

resp=requests.get(uri,auth=(user,passw))
print(resp.status_code)
print(resp.text)