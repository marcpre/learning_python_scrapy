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
            # https://bitcointalk.org/index.php?action=profile;u=1
            yield Request('https://bitcointalk.org/index.php?action=profile;u=%d' % i, callback=self.parse_application)
    
    def parse_application(self, response):
        subject_name = response.xpath('//title/text()').extract_first()
        subject_name = subject_name.split(' | ')
        subject_name = subject_name[0]

        yield {
            'subject_name': subject_name,
            'absolute_course_url': absolute_course_url
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