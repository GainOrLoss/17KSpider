# 17K小说网定向爬虫

## 免责声明：
> 本项目旨在学习Scrapy爬虫框架和使用Mssqlserver数据库，不可使用于商业和个人其他意图。若使用不当，均由个人承担。

## 相关介绍
- [主站domain](http://www.17k.com/)，
  [分类domain](http://all.17k.com/lib/book.html),
  [章节domain](http://www.17k.com/list/2724746.html);
- 采用技术：mssql,scrapy;
- 使用步骤：（1）根据sql脚本，建立相关数据库表
           （2）进入主项目目录，开启命令行 键入 scrapy crawl category,scrapy crawl category_third,scrapy crawl book,scrapy 