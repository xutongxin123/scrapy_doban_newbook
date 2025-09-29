# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    bookname = scrapy.Field()
    author = scrapy.Field()
    publisher = scrapy.Field()
    producer = scrapy.Field()
    original_title = scrapy.Field()
    translation_name = scrapy.Field()
    publication_year = scrapy.Field()
    page_number = scrapy.Field()
    price = scrapy.Field()
    binding = scrapy.Field()
    isbn = scrapy.Field()

