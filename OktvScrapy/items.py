# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OktvscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    price = scrapy.Field()
    address = scrapy.Field()
    objectType = scrapy.Field()
    roomType = scrapy.Field()
    berthCount = scrapy.Field()
    floor = scrapy.Field()
