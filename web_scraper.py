from bs4 import BeautifulSoup as bsoup
from womens_depts import womens_depts
from urllib.request import urlopen

def get_womens_data():
    soup_list = []
    for item in womens_depts:
        url = "http://www.jpeterman.com/Womens-%s?by=Departments"%item
        web_page = urlopen(url)
        soup = bsoup(web_page.read())
        soup_list.append(soup)
    return soup_list

def get_all_links(soup_list):
    all_urls =[]
    for item in soup_list:
        links = item.select('.prlst-itm-detail > a')
        for item in links:
            all_urls.append(item['href'])
    return all_urls


if __name__  ==  "__main__":
    list_page_soup = get_womens_data()
    print(get_all_links(list_page_soup))
