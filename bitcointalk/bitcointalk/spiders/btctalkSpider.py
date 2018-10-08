# -*- coding: utf-8 -*-
import scrapy


class BtctalkspiderSpider(scrapy.Spider):
    name = 'btctalkSpider'
    allowed_domains = ['https://bitcointalk.org/index.php?action=profile;u=1']
    start_urls = ['http://https://bitcointalk.org/index.php?action=profile;u=1/']

    def parse(self, response):
        pass
