from scrapy.exceptions import DropItem
from exporter import HTMLItemExporter
import logging

class HTMLWriterPipeline(object):


    def open_spider(self, spider):
        self.exporter = HTMLItemExporter()
        self.exporter.start_exporting()
        # self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        self.exporter.finish_exporting(spider)

    def process_item(self, item, spider):
        if 'Content' not in item:
            raise DropItem("Not content found %s" % item)
        else:
            self.exporter.export_item(item)
            return item
