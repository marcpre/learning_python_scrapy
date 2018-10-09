# -*- coding: utf-8 -*-
import scrapy


class TablespiderSpider(scrapy.Spider):
    name = 'tableSpider'
    allowed_domains = ['js.sbrfeeds.com/index.php/future?iframeid=iframe-odds-widget-8661192703983387&timezone=16&theme=future&markettypeid=311&version=2.0&odds-type=US&books=19,1096,93,169,1275,999996,139&trackers=1477329448899.xml&event-id=3484282']
    start_urls = ['https://js.sbrfeeds.com/index.php/future?iframeid=iframe-odds-widget-8661192703983387&timezone=16&theme=future&markettypeid=311&version=2.0&odds-type=US&books=19,1096,93,169,1275,999996,139&trackers=1477329448899.xml&event-id=3484282']

    def parse(self, response):
        rows = response.xpath('//*[@class="side side-over side-fav"]|//*[@class="side side-under side-fav"]')
        rows.xpath("//*[@class='team']")
