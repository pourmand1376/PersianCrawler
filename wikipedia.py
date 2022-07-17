from asyncio import gather
import scrapy
import re
from logger import logger

import logging
from scrapy.utils.log import configure_logging 
from pathlib import Path

class WikipediaSpider(scrapy.Spider):
    name= "Wikipedia"

    main_url = "https://fa.wikipedia.org/"

    custom_settings = {'AUTOTHROTTLE_ENABLED':True,
                        'HTTPCACHE_ENABLED':True, 
                        'CONCURRENT_REQUESTS':30,
                        'CONCURRENT_REQUESTS_PER_DOMAIN':30,
                        },


    configure_logging(install_root_handler=False)
    logging.basicConfig(
        filename='log.txt',
        format='%(levelname)s: %(message)s',
        level=logging.INFO
    )

    def __init__(self, gather_index_pages=False):
        # همه صفحه ها
        # صفحه ایندکس ویکی پدیای فارسی
        self.start_urls = ["https://fa.wikipedia.org/w/index.php?title=%D9%88%DB%8C%DA%98%D9%87:%D8%AA%D9%85%D8%A7%D9%85_%D8%B5%D9%81%D8%AD%D9%87%E2%80%8C%D9%87%D8%A7"]
        self.gather_index_pages = gather_index_pages
        if not self.gather_index_pages:
            self.start_urls=Path('index.txt').read_text().split('\n')

    def parse(self, response):
        try:
            next_page = response.css('div#mw-content-text > div:nth-child(2)> :contains("صفحهٔ بعد")::attr(href)').getall()
            if self.gather_index_pages and next_page:
                logger.info(f"Next page {next_page}")
                
                with Path('wikipedia/kaggle/index.txt').open("a") as f:
                    f.write(self.main_url+next_page[0]+'\n')

                yield scrapy.Request(
                    self.main_url+next_page[0],
                    callback=self.parse,
                    dont_filter=True,
                    errback=self.handle_failure,
                )
                
            if not self.gather_index_pages:
                for article in response.css('div#mw-content-text > div.mw-allpages-body a::attr(href)').getall():
                    yield scrapy.Request(
                        self.main_url+article, 
                        callback=self.parse_news,
                    )
        except Exception:
            logger.error("Parsing Error: ", exc_info=True)

    def handle_failure(self, failure):
        logger.warning("Error,", failure.request.url)
        yield scrapy.Request(
            url=failure.request.url,
            dont_filter=True,
            callback=self.parse,
            errback=self.handle_failure)

    def parse_news(self, response):
        try: 
            item = {
                'title': response.css('#firstHeading *::text').get(),
                'content': ' '.join(response.css('div#mw-content-text > div.mw-parser-output > *:not(style):not(table)::text').getall()),
                'link': self.main_url+response.css('li#t-permalink > a::attr(href)').get(),
            }
            
            for key in item:
                item[key] = re.sub(' +', ' ', item[key]).strip()
            
            yield item

        except Exception:
            logger.error(f"Error {item}", exc_info=True)
