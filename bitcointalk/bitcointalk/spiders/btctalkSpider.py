# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


class BtctalkspiderSpider(scrapy.Spider):
    name = 'btctalkSpider'
    allowed_domains = ['bitcointalk.org']
    max_uid = 10

    def parse(self, response):
        urls = response.xpath("//a/@href").extract()
        for i in range(self.max_uid):
            # scrapy shell "https://bitcointalk.org/index.php?action=profile;u=1"
            yield Request('https://bitcointalk.org/index.php?action=profile;u=%d' % i, callback=self.parse_application)
    
    def parse_application(self, response):
        userName = response.xpath('//td[normalize-space(.)="Name:"]/following-sibling::td/text()').extract()


        yield {
            'userName': userName
        }
