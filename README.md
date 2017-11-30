# 17KSpider
##17K小说网定向爬虫
1.主站domain:http://www.17k.com/，分类domain:http://all.17k.com/lib/book.html,章节domain:http://www.17k.com/list/2724746.html;
2.采用技术：mssql,scrapy;
3.使用步骤：（1）根据sql脚本，建立相关数据库表
                      （2）进入主项目目录，开启命令行 键入 scrapy crawl category,scrapy crawl category_third,scrapy crawl book,scrapy crawl chapter