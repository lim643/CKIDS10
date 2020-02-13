import requests
import time
from utils import utils

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
            time.sleep(.001)

    def scrape(self):
        for objects in self.response_data:
            for cell in objects['rows']:
                self.data_list.append(cell['cell'][1:])

    def output_data(self):
        return self.data_list

class google_scholar_scraper:
    def __init__(self):
        self.url = "null"
