# -*- coding: utf-8 -*-
import scrapy
from SeventeenK.mssql import mssql_helper
from SeventeenK.items import SeventeenkBookItem

class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['all.17k.com']
    start_urls = ['http://all.17k.com/']
    ms=mssql_helper()

    def parse(self, response):
        rt=self.ms.execute_query("select Id,Url from [17K_Category] where Level=3")
        for x in rt:
            pid=x[0]
            url=x[1]
            yield scrapy.Request(url,meta={'id':pid},callback=self.parse_page)
        pass
     #分页
    def parse_page(self, response):
        sPage=response.xpath("//*[@class='page']")[0].xpath("string(.)").extract()[0].strip()
        prefix=sPage.index("共")
        suffix=sPage.index("转")
        iPage=int(sPage[prefix+1:suffix-2])
        for i in range(iPage):
            url=response.url[:-6]
            url="{}{}.html".format(url,i+1)
            yield scrapy.Request(url,meta={'id':response.meta["id"]},callback=self.parse_book)
        pass

    #书
    def parse_book(self, response):
        selectors=response.xpath("//tbody/tr")
        print(selectors)
        category_id=response.meta["id"]
        for selector in selectors:
            if selectors.index(selector)>=1:
                item=SeventeenkBookItem()
                item["categoryId"]=category_id
                item["name"]=selector.xpath("./td[@class='td3']/span/a/text()").extract()[0].strip().encode('utf-8').decode('utf-8')
                item["url"]=selector.xpath("./td[@class='td3']/span/a/@href").extract()[0].strip().encode('utf-8').decode('utf-8')
                item["newestChapter"]=selector.xpath("./td[@class='td4']/a/text()").extract()[0].strip().encode('utf-8').decode('utf-8')
                item["size"]=selector.xpath("./td[@class='td5']/text()").extract()[0].strip().encode('utf-8').decode('utf-8')
                item["author"]=selector.xpath("./td[@class='td6']/a/text()").extract()[0].strip().encode('utf-8').decode('utf-8')
                item["updateTime"]=selector.xpath("./td[@class='td7']/text()").extract()[0].strip().encode('utf-8').decode('utf-8')
                status=selector.xpath("./td[@class='td8']/em/text()").extract()[0].strip().encode('utf-8').decode('utf-8')
                item["status"]=0 if status=="连载" else 1
                item["tag"]=1
                yield item
                pass
            pass
        pass
