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
        times = []
        for post_object in self.post_data:
            t0 = time.time()
            page = requests.post(self.url, data = post_object)
            t1 = time.time()
            times.append(t1 - t0)
            print("query time: ", t1 - t0)
            if page.status_code == 200:
                self.response_data.append(eval(page.text))
            else:
                print("error checking here")
            time.sleep(.001)
        print("average query time: ", sum(times) / len(times))

    def scrape(self):
        for objects in self.response_data:
            for cell in objects['rows']:
                self.data_list.append(cell['cell'][1:])

    def output_data(self):
        return self.data_list

class google_scholar_scraper:
    def __init__(self):
        self.url = "null"
