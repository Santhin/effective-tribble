import scrapy
import json
import html_text

class XkomapiSpider(scrapy.Spider):
    name = 'xkomapi'
    allowed_domains = ['x-kom.pl']
    start_urls = ['http://x-kom.pl/']
    headers = {
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'X-API-Key': 'sJSgnQXySmp6pqNV'
    }
    url = "https://mobileapi.x-kom.pl/api/v1/xkom/products?productQuery.criteria.groupIds=2,4,7,5,6,8,64,12&productQuery.pagination.currentPage=1&productQuery.pagination.pageSize=100"
    def start_requests(self):
        yield scrapy.http.Request(url=self.url,
                                headers=self.headers,
                                callback=self.parse)

    def parse(self, response):
        data = json.loads(response.body)
        for product in [x['Id'] for x in data['Items']]:
            yield scrapy.http.Request(url=f"https://mobileapi.x-kom.pl/api/v1/xkom/products/{product}",
                                    headers=self.headers,
                                    callback=self.parse2,
                                    meta={"crawl_once" : True})
        maxNum = data['TotalPages']
        pageNum = 1
        while pageNum <= maxNum:
            pageNum+=1
            yield scrapy.http.Request(url=f'https://mobileapi.x-kom.pl/api/v1/xkom/products?productQuery.criteria.groupIds=2,4,7,5,6,8,64,12&productQuery.pagination.currentPage={pageNum}&productQuery.pagination.pageSize=100',
                                headers=self.headers,
                                callback=self.parse)

    def parse2(self, response):
        # response.request.meta["crawl_once"] = True
        data = json.loads(response.body)
        yield {
        'nazwa' : data['Name'],
        'cena' : data['Price'],
        'opis' : html_text.extract_text(data['ProductDescription'])
        }
