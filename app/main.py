from scrape import wage_scraper, google_scholar_scraper
from uc import uc_scraper
from utils import utils
import time

t0 = time.time()
queries = []
data = utils.read_csv()

wage_data = utils.preprocess_wage(data)
scholar_data = utils.preprocess_scholar(data)
uc_data = utils.preprocess_uc(data)

for item in wage_data:
    queries.append(item)

print("Fetching request")
wage_scrape = wage_scraper(queries)
scholar_scrape = google_scholar_scraper(scholar_data)
uc_scrape = uc_scraper(uc_data)
print("Data Acquireed")

print("Scraping Data")
print("Scraping UC Annual Wage Salary")
wage_scrape.fetch()
wage_scrape.scrape()
print("Scraping Google Scholar")
scholar_scrape.scrape()
print("Scraping UC Faculty Directory Sites")
uc_scrape.scrape()
print("Scrape Completed")

print("Writing to output file")
utils.write_csv(wage_scrape.output_data(), scholar_scrape.output_data(), uc_scrape.output_data())
print("New file output.csv created")
print('Total time taken: ', time.time() - t0)
