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
    floorsInTheHouse = scrapy.Field()
    kitchen = scrapy.Field()
    roomCount = scrapy.Field()
    toilet = scrapy.Field()
    area = scrapy.Field()

    repairYear = scrapy.Field()
    isItaNewBuildingOrNot = scrapy.Field()
    timeForComing = scrapy.Field()
    timeForLeaving = scrapy.Field()
    keysAreGiven = scrapy.Field()
    checkDocuments = scrapy.Field()
    linenChangingEveryNDays = scrapy.Field()
    cleaningEveryNDays = scrapy.Field()
    livingWithOwners = scrapy.Field()
    existingIdentificationDocuments = scrapy.Field()
    peopleUnder21yo = scrapy.Field()
    withKids = scrapy.Field()
    withAnimals = scrapy.Field()
    smoking = scrapy.Field()
    massEvents = scrapy.Field()

    advantages = scrapy.Field()

