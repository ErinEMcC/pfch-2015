from bs4 import BeautifulSoup
import requests
import json
import time



url = ('http://www.circushistory.org/Routes/BarnesSells1937.htm')

route_page = requests.get(url)
if route_page.status_code != 200:
    print ("there was an error with", url)      

    route_html = route_page.text

    soup = BeautifulSoup(route_html, "html.parser") 
    
    all_shows = soup.find_all("td", attrs = {"valign": "top"})
    print (all_shows.text)



