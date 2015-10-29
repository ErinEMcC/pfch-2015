#THIS WILL CREATE THE LIST OF ALL URLS FOR INDV POSTERS
#for x in range(4976):
#    url = 'http://emuseum.ringling.org/emuseum/view/objects/asitem/16579/'+str(x)
#    print (url

from bs4 import BeautifulSoup
import requests
import csv

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
    
    #this is the div inside the div - which is the same info, but cleaner
    #for details in all_detail:
        #data = details.find("div")
        
    #print ('\n')

    ##Tried using 'nextSibling' to lose the labels (which are inside a span
    ##inside the div) Only able to pull back the first few data points,
    ##stopping after "Maker:". Error msg reads: "AttributeError: 'NoneType'
    ##object has no attribute 'nextSibling'" Something to do with the html
    ##structure itself and not the code, but an try/except escapes the hitch.

with open("data/src-circus-posters.tsv", "w") as f:
        fieldnames = ("title", "date", "maker", "dimensions", "medium", "credit", "description", "object")

    output = csv.writer(f, delimiter="\t")
    output.writerow(fieldnames)

    for details in all_detail:
        label = details.find("span")
        try:
            print(label.nextSibling)
        except(AttributeError):
            print ("BLANK SPAN - SKIP")

        title = soup.find("label.nextSibling").em.a.encode_contents()

    
       
        output.writerow(fieldnames)







        #poster=[title, date, link, BLANK, description, id]
        #posters_data.append(poster)


#import csv

#with open ('filename.cv', 'wb') as file:
#           writer=csv.writer(file)
           #for row in posters_data:
            #   writer.writerow(row)
           

        

#time.sleep(10) - this should maybe go in somewhere(?) to pause between pulls.





        

     
