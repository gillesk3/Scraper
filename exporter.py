from scrapy.exporters import BaseItemExporter
from util import Settings
import logging

class HTMLItemExporter(BaseItemExporter):



    def predendToFile(self,line):
            self.file.seek(0, 0)
            content = self.file.read()
            self.file.seek(0, 0)
            self.file.write(line.rstrip('\r\n') + '\n' + content)

    def __init__(self,filename= None,**kwargs):
        self.settings = Settings()
        if filename:
            self.filename = filename
        else: self.filename = self.settings.getFilename()

    def start_exporting(self):
        self.file =  open(self.filename, 'w+')
        logging.debug("opening file")

    def finish_exporting(self,spider):
        self.predendToFile(spider.tableOfContents)
        self.file.close()
        logging.debug("closing file")

    def export_item(self, item):
        self.file.write(item['Header'])
        self.file.write(item['Content'])
