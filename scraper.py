import scrapy
from scrapy.loader import ItemLoader
from items import Chapter


class Serial(scrapy.Spider):
    name = 'serial'
    start_urls = [
        'https://practicalguidetoevil.wordpress.com/2015/03/25/prologue/',
    ]
    endUrl = 'https://practicalguidetoevil.wordpress.com/2017/02/08/prologue-3/'
    chapterNumber = 0
    tableOfContents = "<h1>Table of Contents</h1>"



    def parse(self, response):

        chapter = ItemLoader(item=Chapter(), response=response)
        chapter.add_xpath('Title', '//h1[@class="entry-title"]/text()')

        chapter.add_xpath('Content', '//div[@class="entry-content"]/p')
        chapter.add_xpath('NextPage','//div[@class="nav-next"]/a/@href')
        chapter.add_value('Number',self.chapterNumber)
        chapter = chapter.load_item()
        self.chapterNumber += 1
        self.tableOfContents += '<a href="#chap#%d">%s</a><br>' % (self.chapterNumber, chapter['Title'])
        chapterHeader =   '<h1 id="chap#%d">%s</h1>' % (self.chapterNumber,  chapter['Title'])
        chapter['Content'] =  chapterHeader+ chapter['Content']

        yield chapter

        if 'NextPage' in chapter :
            if chapter['NextPage'] is not self.endUrl:
                yield scrapy.Request(chapter['NextPage'], self.parse)
