import time
import json
import requests
from bs4 import BeautifulSoup
from utils import utils

class ucla:
    def __init__(self, post_data):
        self.url = "http://www.directory.ucla.edu/search.php"
        self.post_data = post_data
        self.data_list = []

    def fetch(self):
        data = []
        for row in self.post_data:
            if row['Location'] == 'Los Angeles':
                data.append({'querytype': 'person', 'q': row['First'] + ' ' + row['Middle'] + ' ' + row['Last'], 'searchtype': 'basic'})
        self.post_data = data

    def scrape(self):
        for post_object in self.post_data:
            page = requests.post(self.url, data = post_object)
            if page.status_code == 200:
                soup = BeautifulSoup(page.text, 'html.parser')
                name = title = dept = ''
                for labels in soup.select('label'):
                    for label in labels:
                        if label == 'Name':
                            name = post_object['q']
                        if label == 'Title':
                            title = labels.find_next_sibling().text
                        if label == 'Department':
                            dept = labels.find_next_sibling().text

                if title != 'Student':
                    self.data_list.append({'Name': name, 'Title': title, 'Department': dept})
            time.sleep(1)

    def output_data(self):
        return self.data_list

class ucb:
    def __init__(self, post_data):
        self.url = 'https://www.berkeley.edu/directory/results?search-term='
        self.post_data = post_data
        self.data_list = []

    def fetch(self):
        data = []
        for row in self.post_data:
            if row['Location'] == 'Berkeley':
                data.append(row['First'] + '+' + row['Last'])
        self.post_data = data  

    def scrape(self):
        for post_object in self.post_data:
            url = self.url + post_object
            page = requests.get(url)
            print(page.text)
            if page.status_code == 200:
                soup = BeautifulSoup(page.text, 'html.parser')
                print(soup.prettify())
                break
            else:
                print('error checking')
                break
            time.sleep(1)

    def output_data(self):
        return self.data_list


class ucd:
    def __init__(self, post_data):
        self.url = 'http://directory.ucdavis.edu/search/directory_results.shtml?filter='
        self.post_data = post_data
        self.data_list = []

    def fetch(self):
        data = []
        for row in self.post_data:
            if row['Location'] == 'Davis':
                data.append(row['First'] + '%20' + row['Last'])
        self.post_data = data
 
    def scrape(self):
        for post_object in self.post_data:
            url = self.url + post_object
            page = requests.get(url)
            if page.status_code == 200:
                soup = BeautifulSoup(page.text, 'html.parser')
                name = title = dept = ''
                for labels in soup.select('th'):
                    for label in labels:
                        if str(label).rstrip() == 'Name:':
                            name = post_object.replace('%20', ' ')
                        if str(label).rstrip() == 'Title:':
                            title = labels.find_next_sibling().text
                        if str(label).rstrip() == 'Department:':
                            dept = labels.find_next_sibling().text

                self.data_list.append({'Name': name, 'Title': title, 'Department': dept})
            time.sleep(1)

    def output_data(self):
        return self.data_list

class ucr:
    def __init__(self, post_data):
        self.url = 'https://profiles.ucr.edu/api/user/search?name='
        self.post_data = post_data
        self.data_list = []

    def fetch(self):
        data = []
        for row in self.post_data:
            if row['Location'] == 'Riverside':
                data.append(row['First'] + '%20' + row['Last'])
        self.post_data = data

    def scrape(self):
        for post_object in self.post_data:
            url = self.url + post_object
            page = requests.get(url)
            if page.status_code == 200:
                if page.text == '[]':
                    continue
                page_object = json.loads(page.text[1:-1])
                self.data_list.append({'Name': post_object.replace('%20', ' '), 'Title': page_object['title'], 'Department': page_object['department']})

            time.sleep(1)

    def output_data(self):
        return self.data_list


class ucm:
    def __init__(self, post_data):
        self.url = 'https://www.ucmerced.edu/content/'
        self.post_data = post_data
        self.data_list = []

    def fetch(self):
        data = []
        for row in self.post_data:
            if row['Location'] == 'Merced':
                data.append(row['First'] + '-' + row['Last'])
        self.post_data = data

    def scrape(self):
        for post_object in self.post_data:
            url = self.url + post_object
            page = requests.get(url)
            if page.status_code == 200:
                soup = BeautifulSoup(page.text, 'html.parser')
                title = edu = ''
                for labels in soup.find_all('div', class_='field-label'):
                    for label in labels:
                        if str(label).rstrip() == 'Title:':
                            title = labels.find_next_sibling().text
                        if str(label).rstrip() == 'Education:':
                            edu = labels.find_next_sibling().text
                self.data_list.append({'Name': post_object.replace('-', ' '), 'Title': title, 'Education': edu})
            time.sleep(1)

    def output_data(self):
        return self.data_list


class uc_scraper:
    def __init__(self, queries):
        self.UCR = ucr(queries)
        self.UCM = ucm(queries)
        self.UCD = ucd(queries)
        self.UCLA = ucla(queries)
        self.data_list = []

    def scrape(self):
        self.UCM.fetch()
        self.UCM.scrape()
        for item in self.UCM.output_data():
            self.data_list.append(item)
        
        self.UCR.fetch()
        self.UCR.scrape()
        for item in self.UCR.output_data():
            self.data_list.append(item)

        self.UCD.fetch()
        self.UCD.scrape()
        for item in self.UCD.output_data():
            self.data_list.append(item)

        self.UCLA.fetch()
        self.UCLA.scrape()
        for item in self.UCLA.output_data():
            self.data_list.append(item)

    def output_data(self):
        return self.data_list

#def main():
#    data = utils.read_csv()
#    queries = utils.preprocess_directory(data)

#    ucm_scraper = ucm(queries)
#    ucm_scraper.fetch()
#    ucm_scraper.scrape()
#    print(ucm_scraper.output_data())

#    ucr_scraper = ucr(queries)
#    ucr_scraper.fetch()
#    ucr_scraper.scrape()
#    print(ucr_scraper.output_data())

#    ucd_scraper = ucd(queries)
#    ucd_scraper.fetch()
#    ucd_scraper.scrape()
#    print(ucd_scraper.output_data())

#    ucb_scraper = ucb(queries)
#    ucb_scraper.fetch()
#    ucb_scraper.scrape()


#    ucla_scraper = ucla(queries)
#    ucla_scraper.fetch()
#    ucla_scraper.scrape()
#    print(ucla_scraper.output_data())

