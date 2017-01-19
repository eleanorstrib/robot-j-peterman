from bs4 import BeautifulSoup as bsoup
from urllib.request import urlopen

url = "http://www.jpeterman.com/Women?by=Departments"
web_page = urlopen(url)
soup = bsoup(web_page.read())

print(soup)
