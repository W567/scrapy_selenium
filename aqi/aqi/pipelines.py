# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import json
from datetime import datetime


class AqiPipeline(object):
    def open_spider(self, spider):
        self.file = open("result.json", "w")

    def process_item(self, item, spider):
        content = json.dumps(dict(item)) + "\n"
        self.file.write(content)
        return item

    def close_spider(self, spider):
        self.file.close()
