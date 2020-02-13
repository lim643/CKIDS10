from scrape import wage_scraper
from utils import utils
import time

t0 = time.time()

queries = []
data = utils.read_csv(utils.file_path())
years = ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018"]

for item in data:
    for year in years:
        item['year'] = year
        queries.append(item)

scraper = wage_scraper(queries)
scraper.fetch()
scraper.scrape()

t1 = time.time()

print(scraper.output_data())
print('Scraper took %f' %(t1 - t0))





