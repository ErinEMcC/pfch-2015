from bs4 import BeautifulSoup
import requests
import json
import time


#setting up the list (to be filled with dictionaries)
all_posters = []

#THIS WILL CREATE THE LIST OF ALL URLS FOR INDV POSTERS
ids = range (0,4976,1)
for x in ids:
    url = ('http://emuseum.ringling.org/emuseum/view/objects/asitem/16579/'+str(x))

    poster_page = requests.get(url)
    if poster_page.status_code != 200:
        print ("there was an error with", url)
        time.sleep(1)    

    object_html = poster_page.text

    soup = BeautifulSoup(object_html, "html.parser")

    #Create variable for URLS of Poster IMAGES
    image = soup.find("p", attrs = {"class": "centeredtext"})
    if image == None:
        a_link = "Image not Available"
    else:
        for image_link in image:
            link_str = image.find ("a", attrs = {"onkeypress": "return Emuseum.onkeypressExecuteOnclick(event, this);"})
            a_link = ('http://emuseum.ringling.org'+str(link_str.get('href')))
            
    
    #this step just removes (what I think is) an unnecessary extra div
    all_detail = soup.find_all("div", attrs = {"class": "paragraph"})

    title = "no title"
    maker = "no maker"
    date = "no date"
    medium = "no_medium"
    dimensions = "no dimensions"
    credit = "no cred_line"
    obj_num = "no obj_num"
    description = "no description"

    
    #check if it has the 10 metadata fields
    if len(all_detail) > 0:
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

        #this is the a_link from the image source concatenation done above
        this_poster['img_url'] = a_link
        print (this_poster)
        print ("\n")

        
        #add it to the list created above or return message
        all_posters.append(this_poster)

        with open('scraped_circusposters.json', 'w') as f:
            f.write(json.dumps(all_posters, indent=4))


    else:
        print ("This page does not meet the element requirement of > 0 :", 'http://emuseum.ringling.org/emuseum/view/objects/asitem/16579/'+str(x))
        continue 
    

print (all_posters)
    

        
