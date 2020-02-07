import requests
from bs4 import BeautifulSoup

class wage_scraper:
    def __init__(self, url):
        self.raw_data = 0
        self.clean_data = 0
        self.url = url

    def fetch(self):
        page = requests.get(self.url)
        if page.status_code == 200:
            self.raw_data = page.text
        else:
            return False
        return True

    def scrape(self):
        soup = BeautifulSoup(self.raw_data, 'html.parser')
        self.clean_data = soup.prettify()
        print(self.clean_data) # right now not correct since no input to website given

if __name__ == "__main__":
    url = 'https://ucannualwage.ucop.edu/wage/'
    scraper = wage_scraper(url)
    if scraper.fetch():
        scraper.scrape()
    else:
        print("Page was not downloaded successfully")
