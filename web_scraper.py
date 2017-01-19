from bs4 import BeautifulSoup as bsoup
from womens_depts import womens_depts
from urllib.request import urlopen

def get_womens_data():
    for item in womens_depts:
        url = "http://www.jpeterman.com/Womens-%s?by=Departments"%item
        web_page = urlopen(url)
        soup = bsoup(web_page.read())

        print(soup)

get_womens_data()
