import scrapy
import re
from logger import logger

class AsriranSpider(scrapy.Spider):
    name= "Asriran"
    number_of_pages = 8313 

    main_url = "https://www.asriran.com"

    def __init__(self, from_page, to_page,from_date, to_date):
        self.start_urls = []

        from_page = int(from_page)
        to_page = int(to_page)

        for i in range(from_page, to_page):
            self.start_urls.append(
                f"https://www.asriran.com/fa/archive?rpp=100&p={i}&from_date={from_date}&to_date={to_date}"
            )
            
        logger.info('urls are appended')
        

    def parse(self, response):
        try:
            for news in response.css("body#archive div.inner-content a::attr(href)").getall():
                yield scrapy.Request(
                    self.main_url+news, 
                    callback=self.parse_news,
                )
        except Exception:
            logger.error("Parsing Error: ", exc_info=True)

    def parse_news(self, response):
        try: 
            item = {
                'title': response.css('body#news div.title > h1 > a::text').get().strip(),
                'shortlink': self.main_url+response.css('body#news div.short-link.row > a::attr(href)').get(),
                'time':  response.css('body#news div.news_nav.news_pdate_c.iconMobileN::text').getall()[1].strip(),
                'service': response.css('body#news div:nth-child(5) > div:nth-child(2) > div:nth-child(1) > div > a:nth-child(1)::text').get(0),
                'subgroup': response.css('body#news div:nth-child(5) > div:nth-child(2) > div:nth-child(1) > div > a:nth-child(2)::text').get(0),
                'abstract': ' '.join(response.css('body#news div.subtitle::text').getall()),
                'body': ' '.join(response.css('body#news div.body > *::text').getall()),
            }
            
            for key in item:
                item[key] = re.sub(' +', ' ', item[key]).strip()
            
            yield item

        except Exception:
            logger.error("Error", exc_info=True)

