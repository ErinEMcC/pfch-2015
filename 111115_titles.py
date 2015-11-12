from bs4 import BeautifulSoup
import requests
import json
import time


#setting up the list (to be filled with dictionaries)
all_titles = []

#THIS WILL CREATE THE LIST OF ALL URLS FOR INDV POSTERS
ids = range (0,4977,1)
for x in ids:
    url = ('http://emuseum.ringling.org/emuseum/view/objects/asitem/16579/'+str(x))

    poster_page = requests.get(url)
    if poster_page.status_code != 200:
        print ("there was an error with", url)
        time.sleep(3)    

    object_html = poster_page.text

    soup = BeautifulSoup(object_html, "html.parser") 
    
    #this step just removes (what I think is) an unnecessary extra div
    all_detail = soup.find_all("div", attrs = {"class": "paragraph"})
    for a_div in all_detail:
        all_text = a_div.text
        if 'Title' in all_text:
            a_title = all_text.replace('Title:' , '').strip()
            
    all_titles.append(a_title)

with open('scraped_postertitles.json', 'w') as f:
    f.write(json.dumps(all_titles))
