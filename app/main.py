from scrape import wage_scraper, google_scholar_scraper
from utils import utils
queries = []
data = utils.read_csv()

wage_data = utils.preprocess_wage(data)
scholar_data = utils.preprocess_scholar(data)

for item in wage_data:
    queries.append(item)

wage_scrape = wage_scraper(queries)
scholar_scrape = google_scholar_scraper(scholar_data)

wage_scrape.fetch()
wage_scrape.scrape()
scholar_scrape.scrape()
utils.write_csv(wage_scrape.output_data(), scholar_scrape.output_data())
