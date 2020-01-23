class HTMLWriterPipeline(object):

    def open_spider(self, spider):
        print('start piplelin')
        # self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        print('close piplelin')

        # self.file.close()

    def process_item(self, item, spider):
        print('prcoess item')
        # line = json.dumps(dict(item)) + "\n"
        # self.file.write(line)
        # return item
