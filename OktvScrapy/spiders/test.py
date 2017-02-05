import scrapy
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from OktvScrapy.items import OktvscrapyItem
from bs4 import BeautifulSoup
from termcolor import colored
from urllib.parse import urljoin
import re

DEBUG = True

def Debug():
    for i in range(10):
        print(colored(
            '-----------------------------------------------------------------------------------------------> Look over here, boy',
            color='red'))

class MySpider(BaseSpider):
    name='betty'
    allowed_domains = ['oktv.ua']
    start_urls = ['http://oktv.ua/kievskaya-oblast/kiev']

    #combination of XPath and Beautiful soup makes life easier
    def parseAppartment(self, response):
        sel = Selector(response)

        app = OktvscrapyItem()

        app['price'] = sel.xpath("//span[@class='price_stable']/text()").extract()[0]
        app['address'] = sel.xpath("//h1[@class='h1-apart']/text()").extract()[0]



        Debug()

        marks = sel.xpath("//mark/text()").extract()
        app['objectType']=marks[0]
        app['roomType'] = marks[1]
        app['berthCount'] = marks[2]

        print(marks)

        Debug()

        for key in app:
            if type(app[key]) is str:
                app[key] = app[key].lstrip().rstrip()
        # with open('log.html', 'w') as f:
        #     print(sel.xpath('//html').extract(), file=f)
        return app

    def parse(self, response):
        sel = Selector(response)

        appartments = sel.xpath("//div[@class='object_v_spiske']//a[@class='btn btn_blue pull-right']/@href").extract()

        print(appartments)

        for link in appartments:
            appLink = urljoin(response.url, link)
            return scrapy.Request(appLink, callback=self.parseAppartment)



        # for i in links:
        #     href = i.extract()
        #     if 'international' in href:
        #         yield scrapy.Request(href, callback=self.parse_race)