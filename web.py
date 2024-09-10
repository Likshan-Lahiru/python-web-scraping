import requests
from bs4 import BeautifulSoup

#define the scrapping site
url = 'https://example.com/'

#send a get request for hosted server
response = requests.get(url)


#check the status of request 
#if response.status_code == 200:
#        print(response.text)
#else:
#      print("error..")






# Parsing the HTML
soup = BeautifulSoup(response.content, 'html.parser')     
titile = soup.title.string


#content = soup.find_all('div')

print( titile)