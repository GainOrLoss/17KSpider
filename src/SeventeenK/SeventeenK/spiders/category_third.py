# -*- coding: utf-8 -*-
import scrapy
from SeventeenK.items import SeventeenkCategoryItem
from SeventeenK.mssql import mssql_helper

class CategoryThirdSpider(scrapy.Spider):
    name = 'category_third'
    allowed_domains = ['all.17k.com']
    start_urls = ['http://www.17k.com/']
    ms=mssql_helper()
    def parse(self, response):
        rt=self.ms.execute_query("select Id,Url from [17K_Category] where Level=2")
        for x in rt:
            pid=x[0]
            url=x[1]
            yield scrapy.Request(url,meta={'id':pid},callback=self.parse_third)
        pass

    def parse_third(self, response):
        pid=response.meta["id"]
        selectors=response.xpath("//*[@class='allzplb']/p/a")
        for sel_third in selectors:
            item_thid=SeventeenkCategoryItem()
            item_thid["name"]=sel_third.xpath("./text()").extract()[0].strip().encode('utf-8').decode('utf-8')
            item_thid["parentId"]=pid
            item_thid["url"]="http://all.17k.com{}".format(sel_third.xpath("./@href").extract()[0].encode('utf-8').decode('utf-8'))
            item_thid["level"]=3
            item_thid["status"]=0
            item["tag"]=0
            yield item_thid
            pass
        pass
