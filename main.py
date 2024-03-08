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


# htmlFileName = 'testing.html'
# authors = ''
# title = ''
book = 'evil1'


settings = Settings()
htmlFileName = settings.getFilename()
htmlFilePath = Settings().getHTMLFilePath(htmlFileName)
mobiFileName =  htmlFileName.split('.')[0] + ".epub"
bookDir = Settings().getBookDir()
mobiFilePath = os.path.join(bookDir,mobiFileName)
authors = settings.getAuthors()
cover = settings.getCover()
title = settings.getTitle()
#startPage = settings.getStartUrl()
book =settings.getBook()
endPage = settings.configData[book]['end']
startPage = [settings.configData[book]['start']]

convertQuery = f'ebook-convert {htmlFilePath} {mobiFilePath} --authors "{authors}" --cover {cover} --title "{title}" --max-toc-links 500'

#process.crawl(EvilSpider, start_urls=startPage,filename=htmlFileName, endUrl=endPage )
#process.start() # the script will block here until the crawling is finished
# logging.debug(convertQuery)
os.system(convertQuery)
