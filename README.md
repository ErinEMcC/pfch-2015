# pfch-2015
This is a repo for a Pratt SILS/SI/MLS/LIS class, 'Programming for Cultural Heritage'

I found a digital archive of almost 5,000 vintage circus posters hosted at the Ringling Museum site. It is amazing.

Notes on the content
Metadata  - the date field is seriously lacking in content
          - just about zero attempt at a controlled vocabulary

Steps of python:
  BeautifulSoup implementation to scrape each individual poster's web page
  Luckily, site used an incremental url system which allows for ++1 in code
  HTML structured ....
  Structured resulting metadata fields to a long list of ~5g dictionaries 
  Print to a JSON file. Archive will break if too much traffic. Full scrape of the ~5g takes somewhere between 4-8 hours. 
  
  JSOR file reading
    Python to read through list of dictionaries and pull a key value (title) from each dictionary in the list. 
    Python with Regular Expression to pull all words from the above key value (title) list that appear before a colon
    
