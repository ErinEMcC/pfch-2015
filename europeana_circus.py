import requests
import json
 
r = requests.get('http://www.europeana.eu/api/v2/search.json?wskey=JQ4CNwmGL&query=europeana_collectionName%3A2021603*&qf=YEAR%3A%5B1900+TO+1901%5D&start=1&rows=12&profile=standard')

print(r.status_code)
print ("\n")

print(r.text)
print ("\n")

#turn it into a python dictonary
#data = json.loads(r.text)
#print(data.keys())


