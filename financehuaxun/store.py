#encoding: utf-8
from pymongo import MongoClient
from scrapy.conf import settings
client = MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
News_huaxunDB = client[settings['MONGODB_DB']]
collect_huaxun_161212 = News_huaxunDB[settings['MONGODB_COLLECTION']]