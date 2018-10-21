# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from douban.items import DoubanItem
from bs4 import BeautifulSoup

class Doubantop250Spider(CrawlSpider):
    name = 'doubanTop250'
    #allowed_domains = ['movie.douban.com/']
    start_urls = ['http://movie.douban.com/top250/']

    rules = (
        Rule(LinkExtractor(allow=r'subject/\d+/',restrict_css = '.hd > a[class = ""]'), callback='parse_item', follow=True),
        #Rule(LinkExtractor(restrict_xpaths='//span[@class = "next"]//a[contains(.,"后页")]'))
        Rule(LinkExtractor(restrict_css='.next a'))
    )

    def parse_item(self, response):
        item = DoubanItem()
        item['movie'] = response.css('span[property="v:itemreviewed"]::text').extract_first()
        item['score'] = response.css('strong[class="ll rating_num"]::text').extract_first()
        item['vote'] = response.css('.rating_people>span::text').extract_first()
        item['runtime'] = response.css('span[property="v:runtime"]::text').extract_first()
        item['ReleaseDate'] = response.css('span[property="v:initialReleaseDate"]::text').extract_first()

        soup = BeautifulSoup(response.text,'lxml')
        info = soup.select_one('div[id="info"]').text
        item['director'] = re.findall(r'(导演:.*?)\n',info)[0]
        item['writer'] = re.findall(r'(编剧:.*?)\n', info)[0]
        item['actor'] = re.findall(r'(主演:.*?)\n',info)[0]
        item['types'] = re.findall(r'(类型:.*?)\n', info)[0]
        item['region'] = re.findall(r'(制片国家/地区:.*?)\n', info)[0]
        item['lang'] = re.findall(r'(语言:.*?)\n', info)[0]
        item['alias'] = re.findall(r'(又名:.*?)\n', info)[0]
        item['IMDb'] = re.findall(r'(IMDb链接:.*?)\n', info)[0]
        yield item


