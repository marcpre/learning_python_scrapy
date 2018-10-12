# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


class BtctalkspiderSpider(scrapy.Spider):
    name = 'btctalkSpider'
    allowed_domains = ['bitcointalk.org']
    max_uid = 400

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
#
#    def start_requests(self):
#        for i in range(self.max_cid):
#            yield Request('http://www.saylor.org/site/syllabus.php?cid=%d' % i,
#                    callback=self.parse_syllabi)

#    def parse_syllabi(self, response):
#        syllabi = SyllabiItem()
#        syllabi['url'] = response.url
#        syllabi['body'] = response.body

#        return syllabi