from scrape import wage_scraper
from utils import utils

queries = []
data = utils.read_csv(utils.file_path())

for item in data:
    queries.append(item)
    print(item)

scraper = wage_scraper(queries)
scraper.fetch()
scraper.scrape()
print(scraper.output_data())
