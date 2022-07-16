import scrapy
import re
from logger import logger

class WikipediaSpider(scrapy.Spider):
    name= "Wikipedia"

    main_url = "https://fa.wikipedia.org/"

    def __init__(self):
        # همه صفحه ها
        # صفحه ایندکس ویکی پدیای فارسی
        self.start_urls = ["https://fa.wikipedia.org/w/index.php?title=%D9%88%DB%8C%DA%98%D9%87:%D8%AA%D9%85%D8%A7%D9%85_%D8%B5%D9%81%D8%AD%D9%87%E2%80%8C%D9%87%D8%A7"]
        

    def parse(self, response):
        try:
            next_page = response.css('div#mw-content-text > div:nth-child(2)> :contains("صفحهٔ بعد")::attr(href)').getall()
            if next_page:
                yield scrapy.Request(
                    self.main_url+next_page[0],
                    callback=self.parse,
                )

            for article in response.css('div#mw-content-text > div.mw-allpages-body a::attr(href)').getall():
                yield scrapy.Request(
                    self.main_url+article, 
                    callback=self.parse_news,
                )
        except Exception:
            logger.error("Parsing Error: ", exc_info=True)

    def parse_news(self, response):
        try: 
            item = {
                'title': response.css('#firstHeading *::text').get(),
                'content': ' '.join(response.css('div#mw-content-text > div.mw-parser-output > *:not(style):not(table)::text').getall()),
                'link': response.css('li#t-permalink > a::attr(href)').get(),
            }
            
            for key in item:
                item[key] = re.sub(' +', ' ', item[key]).strip()
            
            yield item

        except Exception:
            logger.error(f"Error {item}", exc_info=True)
