import requests
import scholarly
from utils import utils
import time
from bs4 import BeautifulSoup
import urllib.request

class wage_scraper:
    def __init__(self, post_data):
        self.url = 'https://ucannualwage.ucop.edu/wage/search.action'
        self.post_data = post_data
        self.response_data = []
        self.data_list = []

    def fetch(self):
        for post_object in self.post_data:
            page = requests.post(self.url, data = post_object)
            if page.status_code == 200:
                self.response_data.append(eval(page.text))
            else:
                print("error checking here")
            time.sleep(.002)

    def scrape(self):
        for objects in self.response_data:
            for cell in objects['rows']:
                self.data_list.append(cell['cell'][1:])

    def output_data(self):
        return self.data_list


class google_scholar_scraper:
    def __init__(self, post_data):
        self.post_data = post_data
        self.data_list = []
        self.url = 'https://scholar.google.com/citations?hl=en&user='

    def scrape(self):
        for post_object in self.post_data[1:]:
            if post_object:
                try:
                    obj = next(scholarly.search_author(post_object))
                    page = urllib.request.urlopen(self.url + obj.id)
                    soup = BeautifulSoup(page, 'html.parser')
                    index = soup.find_all("td", "gsc_rsb_std")
                    self.data_list.append([post_object.split(',')[0], index[2].string, index[4].string, index[0].string])
                except:
                    print("No Google Scholar Record")

    def output_data(self):
        return self.data_list
