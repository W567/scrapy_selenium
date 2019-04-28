# -*- coding: utf-8 -*-
import scrapy
from aqi.items import AqiItem

class AqiCrawlerSpider(scrapy.Spider):
    name = 'aqi_crawler'
    allowed_domains = ['aqistudy.cn']
    base_url = "https://www.aqistudy.cn/historydata/"

    def start_requests(self):
        urls = [
			'https://www.aqistudy.cn/historydata/monthdata.php?city=%E6%88%90%E9%83%BD',    #成都
            'https://www.aqistudy.cn/historydata/monthdata.php?city=%E4%B9%90%E5%B1%B1',    #乐山
            'https://www.aqistudy.cn/historydata/monthdata.php?city=%E7%9C%89%E5%B1%B1',   #眉山
            'https://www.aqistudy.cn/historydata/monthdata.php?city=%E8%87%AA%E8%B4%A1',  #自贡
            'https://www.aqistudy.cn/historydata/monthdata.php?city=%E8%B5%84%E9%98%B3',  #资阳
            'https://www.aqistudy.cn/historydata/monthdata.php?city=%E5%86%85%E6%B1%9F',  #内江
            'https://www.aqistudy.cn/historydata/monthdata.php?city=%E9%81%82%E5%AE%81',  #遂宁
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print("正在爬取城市月份")
        Url_list = response.xpath('//tr/td/a/@href').extract()

        for Url in Url_list[:]:
            link = self.base_url + Url
            print(link)
            yield scrapy.Request(url=link, callback=self.parse_day)

    def parse_day(self, response):
        print("正在爬取最终数据")
        node_list = response.xpath('//tr')
        node_list.pop(0)

        for node in node_list:
            item = AqiItem()
            item['city'] = response.xpath('/html/body/div[3]/div[1]/div[2]/div[2]/div[1]/h3/text()').extract_first()
            item['date'] = node.xpath('./td[1]/text()').extract_first()
            item['AQI'] = node.xpath('./td[2]/text()').extract_first()
            item['level'] = node.xpath('./td[3]//text()').extract_first()
            item['pm2_5'] = node.xpath('./td[4]/text()').extract_first()
            item['pm10'] = node.xpath('./td[5]/text()').extract_first()
            yield item
