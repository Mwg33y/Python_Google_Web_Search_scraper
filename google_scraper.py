# A google search web scraper

#pip install beautifulsoup4
#pip install lxml
#pip install requests
#pip install googlesearch



from googlesearch import search


import bs4
import requests


# the search query
query =  input('Enter your search query here: ')


# a list of search query results
my_results_list = []


# 'tld' is
# 'lang' is
# 'num' is Number of results per page
# 'start'  First result to retrieve
# 'stop' Last result to retrieve
# 'pause' max time lapse between HTTP requests before moving on to another search result

for i in search(query, tld = 'com', lang = 'en', num = 10, start = 0, stop = None,  pause = 2.0):
    my_results_list.append(i)
    print(i)


    if len(my_results_list) == 10 :
        break


leng = len(my_results_list)
count = 0

while count < (leng):
    result = requests.get(my_results_list[count].format())
    soup = bs4.BeautifulSoup(result.text, 'html.parser')
    count = count + 1
    #print(my_results_list[0])
    #print(len(soup))

    for ele in soup.select('p'):
        print(ele.text)