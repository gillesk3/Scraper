import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst




class Chapter(scrapy.Item):
    Number = scrapy.Field()
    Title = scrapy.Field(output_processor=TakeFirst(),)
    Content = scrapy.Field(output_processor=Join(),)
    NextPage = scrapy.Field(output_processor=TakeFirst(),)
