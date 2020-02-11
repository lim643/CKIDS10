from scrape import wage_scraper
from utils import utils

queries = []
data1 = {
    "year": "2015",
    "location": "Davis",
    "firstname": "Sean",
    "lastname": "Davis"
}

data2 = {
    "year": "2016",
    "location": "Davis",
    "firstname": "Sean",
    "lastname": "Davis"
}

data3 = {
    "year": "2017",
    "location": "Davis",
    "firstname": "Sean",
    "lastname": "Davis"
}

queries.append(utils.preprocess(data1))
queries.append(utils.preprocess(data2))
queries.append(utils.preprocess(data3))

scraper = wage_scraper(queries)
scraper.fetch()
scraper.scrape()
print(scraper.output_data())
