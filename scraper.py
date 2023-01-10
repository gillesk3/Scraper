import scrapy
from scrapy.loader import ItemLoader
from items import Chapter
from util import Settings
import logging



class EvilSpider(scrapy.Spider):
    name = 'serial'
    settings = Settings()
    endUrl = ''
    chapterNumber = 0
    tableOfContents = "<h1>Table of Contents</h1>"



    def __init__(self, category='', **kwargs):
        if 'start_urls' in kwargs:
            self.start_urls = kwargs['start_urls']
        if 'filename' in kwargs:
            self.filename = kwargs['filename']
        if 'enendUrl' in kwargs:
            self.endUrl = kwargs['enendUrl']

        super().__init__(**kwargs)  # python3

    def parse(self, response):
        chapter = ItemLoader(item=Chapter(), response=response)
        chapter.add_xpath('Title', '//h1[@class="entry-title"]/text()')
        # chapter.add_xpath('Content',  '//div[@class="entry-content"]/p[count(a)=0 and not( contains(.,//a))]/text()')
        chapter.add_xpath('Content',  '//div[@class="entry-content"]/p')
        chapter.add_xpath('NextPage','//a[@rel="next"]/@href')

        chapter.add_value('Number',self.chapterNumber)
        chapter = chapter.load_item()


        if 'prologue' in chapter['Title'].lower() and self.chapterNumber != 0:
            return

        chapter['Header'] =   self.setHeader(chapter['Title'])
        self.tableOfContents += '<a href="#chap#%d">%s</a><br>' % (self.chapterNumber, chapter['Title'])

        yield chapter
        self.chapterNumber += 1

        if 'NextPage' in chapter:
            if chapter['NextPage'] is not self.endUrl:
                yield scrapy.Request(chapter['NextPage'], self.parse)
        else:
            print('no next page')


    def setHeader(self,title):
        if 'chapter' in title.lower():
            title = title.split(':')[1]

        return '<h1 id="chap#{}">{}</h1>'.format(self.chapterNumber,  title)
