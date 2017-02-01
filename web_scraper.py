from collections import defaultdict
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

def create_dict(all_urls):
    text_dict = defaultdict(list)
    for item in all_urls:
        web_page = urlopen(item)
        soup = bsoup(web_page.read())
        # title = soup.find_all('div', attrs={'class':'story-title'})
        # for item in title:
        #     text_dict['title'].append(item.text.strip())
        full_story = soup.find('div', attrs={'id':'product-story'})
        stories = full_story.find_all('p')
        parsed = ' '.join([item.text for item in stories])
        # text_dict['story'].extend(parsed)
        print(parsed)
        # text_dict['story'].append(item.text for item in full_story)
    # print (text_dict)
    return text_dict

def main():
    list_page_soup = get_womens_data()
    all_urls = get_all_links(list_page_soup)
    print(all_urls)
    create_dict(all_urls)

if __name__  ==  "__main__":
    main()
