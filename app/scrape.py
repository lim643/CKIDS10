import requests

class format_input:
    def __init__(self, data):
        self.data = data

    def clean_input(self):
        self.data = {
            "rows": "60",
            "page": "1",
            "sidx": "EAW_LST_NAM",
            "year": data['year'],
            "location": data['location'],
            "firstname": data['firstname'],
            "lastname": data['lastname']
        }

class wage_scraper:
    def __init__(self, url, post_data):
        self.post_data = post_data
        self.response_data = 0
        self.url = url

    def fetch(self):
        page = requests.post(self.url, data = self.post_data)
        if page.status_code == 200:
            self.response_data = page.text
        else:
            return False
        return True

    def scrape(self):
        print(self.response_data)

if __name__ == "__main__":
    data = {
        "rows": "60",
        "page": "1",
        "sidx": "EAW_LST_NAM",
        "year": "2016",
        "location": "Davis",
        "firstname": "sean",
        "lastname": "davis"
    }
    input = format_input(data)
    input.clean_input()

    url = 'https://ucannualwage.ucop.edu/wage/search.action'
    scraper = wage_scraper(url, input.data)
    if scraper.fetch():
        scraper.scrape()
    else:
        print("Page was not downloaded successfully")
