import scrapy
from scrapy.loader import ItemLoader
from items import Chapter


class Serial(scrapy.Spider):
    name = 'serial'
    start_urls = [
        'https://practicalguidetoevil.wordpress.com/2015/03/25/prologue/',
    ]
    chapterNumber = 0



    def parse(self, response):

        chapter = ItemLoader(item=Chapter(), response=response)
        chapter.add_xpath('Title', '//h1[@class="entry-title"]/text()')
        chapter.add_xpath('Content', '//div[@class="entry-content"]')
        chapter.add_xpath('NextPage','//div[@class="nav-nextt"]/a/@href')
        chapter.add_value('Number',self.chapterNumber)
        chapter = chapter.load_item()
        yield chapter
        if 'NextPage' in chapter:
            print('We have a page')

        # print(chapter)


        # title = response.xpath('//h1[@class="entry-title"]/text()').get()
        # content= res


        #
        # for quote in response.xpath('//div[@class="quote"]'):
        #     yield {
        #         'text': quote.xpath('./span[@class="text"]/text()').extract_first(),
        #         'author': quote.xpath('.//small[@class="author"]/text()').extract_first(),
        #         'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
        #     }
        #
        # next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))
