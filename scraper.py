import scrapy
from scrapy.loader import ItemLoader
from items import Chapter
from util import Settings
import logging



class EvilSpider(scrapy.Spider):
    name = 'serial'
    settings = Settings()
    start_urls = settings.getStartUrl()
    endUrl = 'https://practicalguidetoevil.wordpress.com/2017/02/08/prologue-3/'
    chapterNumber = 0
    tableOfContents = "<h1>Table of Contents</h1>"

    def parse(self, response):
        chapter = ItemLoader(item=Chapter(), response=response)
        chapter.add_xpath('Title', '//h1[@class="entry-title"]/text()')
        chapter.add_xpath('Content',  '//div[@class="entry-content"]/p[count(a)=0 and not( contains(.,//a))]/text()')
        chapter.add_xpath('NextPage','//a[contains(.,"Next")]/@href')

        #response.xpath('//div[@class="entry-content"]/p[count(a)=0 and not( contains(.,//a))]')
        #response.xpath('//a[contains(.,"Next")]/@href').get()

        chapter.add_value('Number',self.chapterNumber)
        chapter = chapter.load_item()


        if 'prologue' in chapter['Title'].lower() and self.chapterNumber is not 0:
            return

        chapter['Header'] =   self.setHeader(chapter['Title'])
        self.tableOfContents += '<a href="#chap#%d">%s</a><br>' % (self.chapterNumber, chapter['Title'])

        yield chapter
        self.chapterNumber += 1
        #
        if 'NextPage' in chapter:
            if chapter['NextPage'] is not self.endUrl:
                yield scrapy.Request(chapter['NextPage'], self.parse)

    def setHeader(self,title):
        if 'chapter' in title.lower():
            title = title.split(':')[1]

        return '<h1 id="chap#{}">{}</h1>'.format(self.chapterNumber,  title)
