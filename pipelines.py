class HTMLWriterPipeline(object):

    def open_spider(self, spider):
        print('*** OPEN ***')
        # self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        print('*** CLOSED ***')

        # self.file.close()

    def process_item(self, item, spider):

        print(item['Title'])
        print('NextPage' in item)
        # print(item['Number'] is None)
        # print('*** PROCESSED ***')
            # self.db[self.collection_name].insert_one(dict(item))
            # return item
