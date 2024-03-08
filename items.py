import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst
import logging


def serializeTitle(value):
    return value.replace('\\xa0', ' ')


def validContent(value):
    if 'Last Chapter' not in value and 'a href' not in value:
        return value


class Chapter(scrapy.Item):
    Number = scrapy.Field()
    Title = scrapy.Field(serializer=serializeTitle, output_processor=TakeFirst(), )
    Header = scrapy.Field(output_processor=TakeFirst(), )
    Content = scrapy.Field(input_processor=MapCompose(validContent), output_processor=Join(), )
    NextPage = scrapy.Field(output_processor=TakeFirst(), )
