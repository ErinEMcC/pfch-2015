import json
import pprint
import re

##opening json file to read, parse 
with open('scraped_circusposters.json') as json_data:
     data = json.load(json_data)
     json_data.close()
     
     ##PRETTY PRINTING TO CHECK SITUATION
     ##pprint.pprint(data)

poster_troupes = {}
all_troupes = []

     ## gets all key values in list of dictionaries when key = title
for row in (data):
    titles = (row['title'])

    ## regex for content before a colon ^[^:]+\s*
    ## in ~95% of the archive this is troupe name
    troupes = re.findall('^[^:]+\s*', titles)

    #add troupes (with duplicates) to the list        
    all_troupes.append(troupes)

    for a_troupe in all_troupes:
        if a_troupe not in poster_troupes:
            poster_troupes[a_troupe] = 0
        poster_troupes[a_troupe] = poster_troupes[a_troupe] +1

pprint.pprint (poster_troupes)


         

## writes results back into separate json file        
##with open ('troupes.json', 'w') as f:
##    f.write(json.dumps(all_troupes, indent=4))

         
         
         
         
         
