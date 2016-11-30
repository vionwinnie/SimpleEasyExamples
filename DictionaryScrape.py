#this is an attempt to scrape a list of synonyms of words off of powerthesaurus.org#
#we used requests and bs4"

from bs4 import BeautifulSoup
import requests 

#
#http_proxy = 'proxy_link'
#https_proxy = 'proxy_link'
#
#proxy_dict = {
#            'https' : https_proxy,
#            'http' : http_proxy
#             }
#             
url = "https://www.powerthesaurus.org/hospitality/related"
r = requests.get(url,proxies=proxy_dict)

soup = BeautifulSoup(r.text)

titles = [h2.text for h2 in soup.findAll('td', attrs={'class': 'abbdef'})]

print titles
