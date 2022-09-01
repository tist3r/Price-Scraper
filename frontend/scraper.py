from bs4 import BeautifulSoup
import requests
import re
import pickle
from os.path import exists

class Scraper:
    def __init__(self, url, selector, price_limit) -> None:
        self.url = url
        self.selector = selector
        self.price_lim = price_limit
        self.status = None

    def scrape(self):
        page = requests.get(self.url).content
        soup = BeautifulSoup(page, 'html.parser')

        #print(soup)

        print(Scraper.get_by_selector(soup, self.selector))
        return soup


    def get_by_selector(soup, selector):
        tag, tag_class = Scraper.parse_selector(selector)
        el = soup.find_all(tag, tag_class)
        
        if len(el) == 1:
            el_text = el[0].getText()
            print(el_text)

            return el_text

    
    def parse_selector(selector):
        tag_el = re.search('\<[^>]*>', selector).group(0)
        tag = tag_el[1:tag_el.find(' ')]

        #potentially no class tag
        tag_class = re.search('class=".*"', selector).group(0)[7:-1]
        
        return tag, tag_class


class ScraperManager:

    def __init__(self) -> None:
        self.active_scrapers = {}

    def add_scraper(self, name, scraper):
        if name not in self.active_scrapers.keys():
            self.active_scrapers[name] = scraper
            self.save_to_disk()

    def save_to_disk(self):
        with open('scraper_manager.pickle', 'wb') as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    def load_from_disk():
        if exists('scraper_manager.pickle'):

            with open('scraper_manager.pickle', 'rb') as f:
                data = pickle.load(f)
                return data
        else:
            return ScraperManager()



# selector = '<span class="rd-price-information__price"> 3400,00 € </span>'
# url = 'https://www.kaufland.de/product/411946076/?id_unit=385044576373&ref=spa_gallery_page_w1&mabref=klassische%20sofas'

# scraper = Scraper(url, selector)
# scraper.scrape()

