import scrapy

class TasnimSpider(scrapy.Spider):
    
    main_url = "https://www.tasnimnews.com"
    name = "Tasnim"
    base_urls=['https://www.tasnimnews.com/fa/service/1/', #سیاسی,
                'https://www.tasnimnews.com/fa/service/2/', #اجتماعی,
                'https://www.tasnimnews.com/fa/service/3/', #ورزشی,
                'https://www.tasnimnews.com/fa/service/4/', #فرهنگی هنری,
                'https://www.tasnimnews.com/fa/service/6/', #استان‌ها,
                'https://www.tasnimnews.com/fa/service/7/', #اقتصادی,
                'https://www.tasnimnews.com/fa/service/8/', #بین الملل,
                'https://www.tasnimnews.com/fa/service/9/', #رسانه ها,
                 ]

    number_of_pages=400
    def __init__(self):
        pages = [f"?page={i}" for i in range(1,self.number_of_pages)]
        self.start_urls = []
        for item in self.base_urls:
            for page in pages:
                self.start_urls.append(f"{item}{page}")

    def parse(self, response ):
        categories = {'https://www.tasnimnews.com/fa/service/1/':'سیاسی',
                    'https://www.tasnimnews.com/fa/service/2/':'اجتماعی',
                    'https://www.tasnimnews.com/fa/service/3/':'ورزشی',
                    'https://www.tasnimnews.com/fa/service/4/':'فرهنگی هنری',
                    'https://www.tasnimnews.com/fa/service/6/':'استان‌ها',
                    'https://www.tasnimnews.com/fa/service/7/':'اقتصادی',
                    'https://www.tasnimnews.com/fa/service/8/':'بین الملل',
                    'https://www.tasnimnews.com/fa/service/9/':'رسانه ها',}
        
        for item in categories.keys():
            if response.url.startswith(item):
                category = categories[item]

        for news in response.css('article.list-item a::attr(href)').getall():
            request=scrapy.Request(
                self.main_url+news, 
                callback=self.parse_news,
                cb_kwargs=dict(category=category))
            yield request 


    def parse_news(self, response,category):
        item = {
            'category': category,
            'title': response.css('article.single-news h1.title::text').get(),
            'abstract': response.css('article.single-news h3.lead::text').get(),
            'body': ' '.join(response.css('article.single-news div.story p::text').getall()),
            'time': response.css('article.single-news div._sticky ul.list-inline li.time::text').get()
        }
        
        yield item