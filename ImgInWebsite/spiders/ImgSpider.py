# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from ImgInWebsite.items import ImgItem

class ImgSpider(scrapy.Spider):
    name = "ImgSpider"
    allowed_domains = ["www.meizu.com"]
    start_urls = ['http://www.meizu.com/']
    
    URL=[]
    IMG=[]

    def parse(self, response):
        allUrl=response.url
        print allUrl
        # 爬取图片连接
        s=allUrl.split('/')
        root='/'.join(s[0:3])
        # 下面的正则会匹配多个括号
        pattern=re.compile(r'((((https|http):\/\/)|\/)[0-9a-zA-Z\/\.@-_%]*?\.(jpg|png))')
        items=pattern.findall(response.text)
        for item in items:
            img=item[0]
            if img in self.IMG:
                continue
            else:
                self.IMG.append(img)
            
            if img.startswith('/'):
                img=root+img
            elif img.startswith('http') or img.startswith('www'):
                img=img
            else:
                # 当前url加上img
                # 严格还要判断allUrl是不是以'/'结尾
                if allUrl.endswith('/'):
                    img=allUrl+img
                else:
                    img='/'.join(allUrl.split('/')[0:-1])+'/'+img
            imgItem=ImgItem()
            imgItem['img_url']=img
            yield imgItem

        # 爬取继续爬取的网址
        urls=response.xpath('//a/@href').extract()

        for url in urls:
            if url in self.URL:
                continue
            else:
                self.URL.append(url)
            # 组合成完整的url
            if url.startswith('/'):
                url='/'.join(allUrl.split('/')[0:3])+url
            elif url.startswith('http') or url.startswith('www'):
                url=url
            else:
                # 相对路径
                # 还要判断allUrl是不是以'/'结尾
                if allUrl.endswith('/'):
                    url=allUrl+url
                else:
                    url='/'.join(allUrl.split('/')[0:-1])+'/'+url
            
            yield Request(url, callback=self.parse)