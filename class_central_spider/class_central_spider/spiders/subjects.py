# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

class SubjectsSpider(scrapy.Spider):
    name = 'subjects'
    allowed_domains = ['classcentral.com']
    start_urls = ['http://class-central.com/subjects']

    def __init__(self, subject=None):
        self.subject = subject

    def parse(self, response):
        if self.subject:
            subject_url = response.xpath('//*[contains(@title, "' + self.subject + '")]/@href').extract_first()
            yield Request(response.urljoin(subject_url), callback=self.parse_subject)
        else:
            self.logger.info("Scraping all subjects.")
            subjects = response.xpath('//*[@class="show-all-subjects view-all-courses"]/@href').extract()
            for subject in subjects:
                yield Request(response.urljoin(subject), callback=self.parse_subject)

    def parse_subject(self, response):
        pass