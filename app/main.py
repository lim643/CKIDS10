from scrape import wage_scraper
from utils import utils

queries = []
data = utils.preprocess_wage(utils.read_csv())

for item in data:
    queries.append(item)

scraper = wage_scraper(queries)
scraper.fetch()
scraper.scrape()
print(scraper.output_data())
