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

def writeHTMLToLogFile(sel):
    with open('log.html', 'w') as f:
        print(sel.xpath('//html').extract(), file=f)

class MySpider(BaseSpider):
    name='oktv'
    allowed_domains = ['oktv.ua']
    start_urls = ['http://oktv.ua/search?group_addr=%D0%9A%D0%B8%D0%B5%D0%B2&start=12']

    def parseAppartment(self, response):
        sel = Selector(response)

        app = OktvscrapyItem()

        app['url']=response.url
        app['price'] = sel.xpath("//span[@class='price_stable']/text()").extract()[0]
        app['address'] = sel.xpath("//h1[@class='h1-apart']/text()").extract()[0]

        marks = sel.xpath("//mark/text()").extract()
        app['objectType'] = marks[0]
        app['roomType'] = marks[1]
        app['berthCount'] = marks[2]
        app['floor'] = marks[4]
        app['floorsInTheHouse'] = marks[5]
        app['roomCount'] = marks[6]
        app['kitchen'] = marks[8]
        app['toilet'] = marks[9]
        app['area'] = marks[10]
        app['repairYear'] = marks[11]
        app['isItaNewBuildingOrNot'] = marks[12]
        app['timeForComing'] = marks[13]
        app['timeForLeaving'] = marks[14]
        app['keysAreGiven'] = marks[15]
        app['checkDocuments'] = marks[16]
        # Some of appartments have these qualities , others don't
        # app['linenChangingEveryNDays'] = marks[17]
        # app['cleaningEveryNDays'] = marks[18]
        # app['livingWithOwners'] = marks[19]
        # app['existingIdentificationDocuments'] = marks[20]
        # app['peopleUnder21yo'] = marks[21]
        # app['withKids'] = marks[22]
        # app['withAnimals'] = marks[23]
        # app['smoking'] = marks[24]
        # app['massEvents'] = marks[25]

        advs = sel.xpath("//div[@class='col-xs-12 ydobstva']//p/text()").extract()
        # Make it look a bit prettier
        app['advantages'] = [x.lstrip().rstrip().replace('\t', '')[2:] for x in advs]

        app['freeDates'] = []
        freeDays = sel.xpath("//div[contains(@class,'day') and (not(contains(@class, 'bron'))) and (not(contains(@class, 'week'))) and (not(contains(@class, 'today')))]").extract()
        for day in freeDays:
            date = re.findall(r'data-time-default="(\d{2}.\d{2}.\d{4})"', day)[0]
            price = re.findall(r'data-price-sum="(\d+)"', day)[0]
            app['freeDates'].append({
                'date': date,
                'price': price + 'UAH'
            })
        if DEBUG:
            Debug()
            #Suspicious code goes here

            Debug()

        for key in app:
            if type(app[key]) is str:
                app[key] = app[key].lstrip().rstrip()
        return app

    def parse(self, response):
        sel = Selector(response)

        appartments = sel.xpath("//div[@class='object_v_spiske']//a[@class='btn btn_blue pull-right']/@href").extract()

        print(appartments)

        for link in appartments:
            appLink = urljoin(response.url, link)
            yield scrapy.Request(appLink, callback=self.parseAppartment)
            break

        pages = sel.xpath("//ul[@class='pagination ok']//a/@href").extract()
        pages = [urljoin(response.url, x) for x in pages]
        pos = pages.index(response.url)
        if pos+1<len(pages):
            nextPage = pages[pos+1]
            yield scrapy.Request(nextPage)
