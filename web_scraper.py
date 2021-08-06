# normal link scraper
from bs4 import BeautifulSoup
import requests

#search = input("Enter search term: ")
search = 'python'
url = 'https://www.bing.com/search?q={}&setlang=en-us'.format(search)
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
r = requests.get(url,headers=headers)
#r.text
print(r.url)

# parse html contents of the requested page and turning into BeautifulSoup Object
soup = BeautifulSoup(r.text, 'html.parser')

# print(soup.prettify()) # prints out all the html contents
results = soup.find("ol", {"id": "b_results"})  # finding the 'ol's from the html which has a 'id': b_results
results.text 

links = results.findAll("li", {"class": "b_algo"})
# kind of filtering the whole html content and savinf in a list of content that we want

for item in links:
    #item = links[0]
    item_text = item.find("a").text  # extracting text from all the links in the list
    item_href = item.find("a").attrs["href"]  # extracting links, .attrs specifies special attributes
    if item_text and item_href:
        
        item_summary = item.find("a").parent.parent.find("p")  # parent content in the html of the selected item

        print(item_text)
        print(item_href)
        #print(item_summary.text)
