from scrapy.crawler import CrawlerProcess
from scraper import Serial

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'ITEM_PIPELINES' : {
    'pipelines.HTMLWriterPipeline': 800}
})

process.crawl(Serial)
process.start() # the script will block here until the crawling is finished
