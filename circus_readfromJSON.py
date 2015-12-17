import json
import pprint
import re

##opening json file to read, parse 
with open('scraped_circusposters.json') as json_data:
     data = json.load(json_data)
     json_data.close()
     
     ##PRETTY PRINTING TO CHECK SITUATION
     ##pprint.pprint(data)

    ## gets all key values in list of dictionaries when key = title
     for i in (data):
         titles = (i['title'])

         ## regex for content before a colon ^[^:]+\s*
         ## 90% of the archive this is troupe name
         troupes = re.findall('^[^:]+\s*', titles)
         print (troupes)

         ## writes results back into separate json file        
         with open ('troupes.json', 'w') as f:
             f.write(json.dumps(troupes, indent=4))

         
         
         
         
         
