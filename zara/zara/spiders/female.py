# -*- coding: utf-8 -*-
import scrapy
import json
from zara.items import ZaraItem

class FemaleSpider(scrapy.Spider):
    name = "female"
    allowed_domains = ["zara.com"]
    # custom_settings = {
    #     "DEFAULT_REQUEST_HEADERS": {
    #         #  GET /tw/zt/%E6%B8%9B%E5%83%B9/%E5%A5%B3%E5%A3%AB/%E5%A4%96%E5%A5%97%E5%A4%A7%E8%A1%A3/%E6%9F%A5%E7%9C%8B%E5%85%A8%E9%83%A8-c791041.html?ajax=true HTTP/1.1
    #         # Host: www.zara.com
    #         'Connection': 'keep-alive',
    #         'Accept': 'application/json, text/javascript, */*; q=0.01',
    #         'X-Requested-With': 'XMLHttpRequest',
    #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
    #         'Referer': 'http://www.zara.com/tw/zt/%E6%B8%9B%E5%83%B9/%E5%A5%B3%E5%A3%AB/%E9%A3%9B%E8%A1%8C%E5%93%A1%E5%A4%96%E5%A5%97-c833537.html',
    #         'Accept-Encoding': 'gzip, deflate, sdch',
    #         'Accept-Language': 'en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4',
    #         'Cookie': 'storepath=tw/zt; optimizelyEndUserId=oeu1480556745722r0.15319725022287756; WC_cookiesMsg=1; optimizelySegments=%7B%22188049923%22%3A%22false%22%2C%22188080683%22%3A%22search%22%2C%22188117527%22%3A%22none%22%2C%22188127138%22%3A%22gc%22%2C%22236998896%22%3A%22true%22%7D; optimizelyBuckets=%7B%7D; web_version=STANDARD; _gat__cowise=1; socControl=http%3A%2F%2Fwww.zara.com; _ga=GA1.2.493037407.1480556747; JSESSIONID=0000RpWPYFXQ9eWE_4Zz7oQW2lJ:12aitdr2e; RT="sl=2&ss=1482568559542&tt=7239&obo=0&sh=1482568586584%3D2%3A0%3A7239%2C1482568566004%3D1%3A0%3A5398&dm=zara.com&si=bd5d0e46-0914-4119-90e5-376c8e55eaf4&bcn=%2F%2F36fb6d10.mpstat.us%2F&ld=1482568586585&nu=http%3A%2F%2Fwww.zara.com%2Ftw%2Fzt%2F%25E6%25B8%259B%25E5%2583%25B9%2F%25E5%25A5%25B3%25E5%25A3%25AB%2F%25E5%25A4%2596%25E5%25A5%2597%25E5%25A4%25A7%25E8%25A1%25A3%2F%25E6%259F%25A5%25E7%259C%258B%25E5%2585%25A8%25E9%2583%25A8-c791041.html&cl=1482568602945'
    #     }
    # }
    start_urls = ['http://www.zara.com/tw/zt/%E6%B8%9B%E5%83%B9/%E5%A5%B3%E5%A3%AB/%E5%A4%96%E5%A5%97%E5%A4%A7%E8%A1%A3/%E6%9F%A5%E7%9C%8B%E5%85%A8%E9%83%A8-c791041.html']

    big_class = ''

    def parse(self, response):
        cloth_class = response.xpath(
            '//*[@id="menu"]/ul/li[1]/ul/li[1]/ul/li/a/text()').extract()
        urls = response.xpath(
            '//*[@id="menu"]/ul/li[1]/ul/li[1]/ul/li/a/@href').extract()

        for _, (cloth, url) in enumerate(zip(cloth_class, urls)):
            if _ > 2 and _ < len(cloth_class) - 8:
                _url = response.urljoin(url[2:]) + '?ajax=true'
                print(_url)
                yield scrapy.Request(url=_url, meta={'cloth': cloth}, callback=self.parse_product)
            else:
                pass

    def parse_product(self, response):
        # print(response.body)
        data = json.loads(response.body)
        for _, i in enumerate(data["productGroups"]):
            for k in i["products"]:
                item = ZaraItem()
                item['cloth_class'] = response.meta['cloth']
                item['product_name'] = k["name"]
                raw_url = k["detail"]["colors"][0]["colorImageUrl"]
                item['product_img'] = raw_url.split(".jpg?timestamp")[
                                                    0] + '_1' + '.jpg?timestamp' + raw_url.split(".jpg?timestamp")[1]
                # print(url)
                # print(k["image"]["path"])
                item['product_price'] = k["price"] / 100
                yield item

        # product_name = response.xpath(
        #     '//*[@id="products"]/ul/li/div/a/text()').extract()
        # product_price = r
esponse.xpath(
        #     '//*[@id="products"]/ul/li/div/div[@class="price _product-price"]/span/@data-price').extract()
        # product_img = response.xpath(
        #     '////*[@id="products"]/ul/li[@class="product _product"]/a/img/@src').extract()
        # for _, (name, price, img) in enumerate(zip(product_name, product_price, product_img)):
        #     print(_, name, price, img)
        #     item = ZaraItem()
        #     item['cloth_class'] = response.meta['cloth']
        #     item['product_name'] = name
        #     item['product_price'] = price
        #     item['product_img'] = 'https:' + img
        #     yield item
