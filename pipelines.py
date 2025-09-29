# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookPipeline:
    def __init__(self):
        self.client = pymongo.MongoClient(host='localhost')
        self.db = self.client['game']
        self.col = self.db['one']
    def process_item(self, item, spider):

        res = self.col.insert_one(dict(item))
        print(res)
        return item

    def __del__(self):
        print('end')
