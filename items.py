import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst
import logging

def serializeTitle(value):
    a = a
    print('*** IN SERIAILZER')
    return value.replace('\\xa0', ' ')



class Chapter(scrapy.Item):
    Number = scrapy.Field()
    Title = scrapy.Field(serializer=serializeTitle,output_processor=TakeFirst(),)
    Header = scrapy.Field(output_processor=TakeFirst(),)
    Content = scrapy.Field(output_processor=Join(),)
    NextPage = scrapy.Field(output_processor=TakeFirst(),)
