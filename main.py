from scrapy.crawler import CrawlerProcess
from scraper import EvilSpider
from util import Settings
import os
import logging


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'ITEM_PIPELINES' : {
    'pipelines.HTMLWriterPipeline': 800}
})

settings = Settings()
htmlFileName = settings.getFilename()
htmlFilePath = settings.getHTMLFilePath(htmlFileName)
mobiFileName =  htmlFileName.split('.')[0] + ".mobi"
bookDir = settings.getBookDir()
mobiFilePath = os.path.join(bookDir,mobiFileName)
authors = settings.getAuthors()
title = settings.getTitle()

convertQuery = 'ebook-convert {} {} --authors "{}" --title "{}" --max-toc-links 500'.format(htmlFilePath, mobiFilePath, authors, title)


process.crawl(EvilSpider)
process.start() # the script will block here until the crawling is finished
# logging.debug(convertQuery)
os.system(convertQuery)
