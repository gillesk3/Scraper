from scrapy.exceptions import DropItem
class HTMLWriterPipeline(object):

    filename = 'evil2.html'

    # def line_prepender(filename, line):
    #     with open(filename, 'r+') as f:
    #         content = f.read()
    #         f.seek(0, 0)
    #         f.write(line.rstrip('\r\n') + '\n' + content)

    def predendToFile(self,line):
            self.file.seek(0, 0)
            content = self.file.read()
            self.file.seek(0, 0)
            self.file.write(line.rstrip('\r\n') + '\n' + content)


    def open_spider(self, spider):

        self.file =  open(self.filename, 'w+')
        print('*** OPEN ***')
        # self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        self.predendToFile(spider.tableOfContents)
        self.file.close()
        print('*** CLOSED ***')

    def process_item(self, item, spider):

        if 'Content' not in item:
            raise DropItem("Not content found %s" % item)
        else:
            self.file.write(item['Content'])
            return item


        # print(item['Number'] is None)
        # print('*** PROCESSED ***')
            # self.db[self.collection_name].insert_one(dict(item))
            # return item
