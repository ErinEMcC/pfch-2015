#THIS WILL CREATE THE LIST OF ALL URLS FOR INDV POSTERS
#for x in range(4976):
#    url = 'http://emuseum.ringling.org/emuseum/view/objects/asitem/16579/'+str(x)
#    print (url

from bs4 import BeautifulSoup
import requests
import csv

all_posters = []

ids = range (0,3,1)
for x in ids:
    url = ('http://emuseum.ringling.org/emuseum/view/objects/asitem/16579/'+str(x))

    poster_page = requests.get(url)
    if poster_page.status_code != 200:
        print ("there was an error with", url)
            
    object_html = poster_page.text

    soup = BeautifulSoup(object_html, "html.parser")

    poster_details = {}

    
    #this step just removes (what I think is) an unnecessary extra div
    all_detail = soup.find_all("div", attrs = {"class": "paragraph"})
    
    #check if it has the 10 metadata fields
    if len(all_detail) == 10:
        #loop through for text inside the div
        for a_div in all_detail:
            all_text = a_div.text

            #keyword check to identify data field
            if 'Title:' in all_text:
                #create the variable for that field 
                #find/replace for the 'label' span, then trim white space
                title = all_text.replace('Title:' , '').strip()

            #keyword check to identify data field
            if 'Maker:' in all_text:
                #create the variable for that field
                #find/replace for the 'label' span, then trim white space
                maker = all_text.replace('Maker:' , '').strip()

            #keyword check to identify data field
            if 'Date:' in all_text:
                #create the variable for that field
                #find/replace for the 'label' span, then trim white space
                date = all_text.replace('Date:' , '').strip()

            #keyword check to identify data field
            if 'Medium:' in all_text:
                #create the variable for that field
                #find/replace for the 'label' span, then trim white space
                medium = all_text.replace('Medium:' , '').strip()

            #keyword check to identify data field
            if 'Dimensions:' in all_text:
                #create the variable for that field
                #find/replace for the 'label' span, then trim white space
                dimensions = all_text.replace('Dimensions:' , '').strip()

            #keyword check to identify data field
            if 'Credit Line:' in all_text:
                #create the variable for that field
                #find/replace for the 'label' span, then trim white space
                credit = all_text.replace('Credit line:' , '').strip()

            #keyword check to identify data field
            if 'Object Number:' in all_text:
                #create the variable for that field
                #find/replace for the 'label' span, then trim white space
                obj_num = all_text.replace('Object Number:' , '').strip()

            #keyword check to identify data field
            if 'Description:' in all_text:
                #create the variable for that field
                #find/replace for the 'label' span, then trim white space
                description = all_text.replace('Description:' , '').strip()


        #create / define a dictionary
        this_poster = {}

        #all the fields as dictionary keys, with the variables from above
        this_poster['title'] = title
        this_poster['maker'] = maker
        this_poster['date'] = date
        this_poster['mediuum'] = medium
        this_poster['dimensions'] = dimensions
        this_poster['credit'] = credit
        this_poster['obj_num'] = obj_num
        this_poster['description'] = description

        #this is the x from the url defined at the beginning
        this_poster['web_id'] = x
        

        print (this_poster)

        #add it to the list created above or return message
        all_posters.append(this_poster)

    else:
        print ("This page does not meet the element requirement of 10:", 'http://emuseum.ringling.org/emuseum/view/objects/asitem/16579/'+str(x))

print (all_posters)

    
#time.sleep(10) - this should maybe go in somewhere(?) to pause between pulls.
        
