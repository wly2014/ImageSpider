# ImageSpider

## 如何使用

1. 将`ImageSpider\ImgInWebsite\spiders\ImgSpider.py`文件中的`allowed_domains = ["www.meizu.com"]`和`start_urls = ['http://www.meizu.com/']`中的地址换成自己想要爬取图片网站的地址。
2. 运行命令`scrapy crawl ImgSpider`
3. 本地生成一个`imgs.txt`文件，其中有全部图片的下载地址

## 更多

[使用scrapy爬取网站上的所有图片](http://blog.csdn.net/u014271114/article/details/53080447)