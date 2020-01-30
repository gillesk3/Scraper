from scrapy.exporters import BaseItemExporter
from util import Settings
import logging
import os

class HTMLItemExporter(BaseItemExporter):

    baseDir = 'ScrapedPages'

    def predendToFile(self,line):
        line =  (line.rstrip('\r\n') + '\n').encode('utf-8')
        self.file.seek(0, 0)
        content = self.file.read()
        self.file.seek(0, 0)
        content = line + content
        self.file.write(content)

    def __init__(self,filename= None,**kwargs):
        self.settings = Settings()
        if filename:
            self.filename = filename
        else: self.filename = self.settings.getFilename()

    def start_exporting(self):
        self.filePath = self.settings.getHTMLFilePath(self.filename)
        self.file =  open(self.filePath, 'wb+')
        logging.debug("opening file")

    def finish_exporting(self,spider):
        self.predendToFile(spider.tableOfContents)
        self.file.close()
        logging.debug("closing file")

    def export_item(self, item):
        self.file.write(item['Header'].encode('utf-8'))
        self.file.write(item['Content'].encode('utf-8'))
