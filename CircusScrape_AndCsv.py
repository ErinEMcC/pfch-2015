#THIS WILL CREATE THE LIST OF ALL URLS FOR INDV POSTERS
#for x in range(4976):
#    url = 'http://emuseum.ringling.org/emuseum/view/objects/asitem/16579/'+str(x)
#    print (url

from bs4 import BeautifulSoup
import requests
import csv

ids = range (0,1,1)
for x in ids:
    url = ('http://emuseum.ringling.org/emuseum/view/objects/asitem/16579/'+str(x))

    poster_page = requests.get(url)
    if poster_page.status_code != 200:
        print ("there was an error with", url)
            
    object_html = poster_page.text

    soup = BeautifulSoup(object_html, "html.parser")

    posters = []     

    #this step just removes (what I think is) an unnecessary extra div
    all_detail = soup.find_all("div", attrs = {"class": "paragraph"})

    a_poster = {}

    for details in all_detail:
        label = details.find("span")
        try:
            print (label.text)
        except AttributeError:
            continue 

        if label.text == 'Title':
            a_poster['Title'] = label.nextSibling

    print (a_poster)
