from scrapy.crawler import CrawlerProcess
from scraper import Serial
from util import Settings
import os
import logging

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'ITEM_PIPELINES' : {
    'pipelines.HTMLWriterPipeline': 800}
})


settings = Settings()
htmlFile = settings.getFilename()
mobiFile = htmlFile.split('.')[0] + ".mobi"
authors = settings.getAuthors()
title = settings.getTitle()

convertQuery = 'ebook-convert {} {} --authors "{}" --title "{}" --max-toc-links 500'.format(htmlFile, mobiFile, authors, title)


process.crawl(Serial)
process.start() # the script will block here until the crawling is finished
logging.debug(convertQuery)
# os.system(convertQuery)
