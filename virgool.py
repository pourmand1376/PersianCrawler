import scrapy
from pathlib import Path
from logger import logger
import re

class VirgoolSpider(scrapy.Spider):
    name = "Virgool"
    number_of_pages = 30000

    custom_settings = {'AUTOTHROTTLE_ENABLED': True,
                       'HTTPCACHE_ENABLED': True,
                       'CONCURRENT_REQUESTS': 100,
                       'CONCURRENT_REQUESTS_PER_DOMAIN': 100,
                       }
    def __init__(self, gather_index_pages=False, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = []
        self.gather_index_pages = gather_index_pages
        if not self.gather_index_pages:
            self.start_urls = Path('virgool/index.txt').read_text().split('\n')
        else:
            for i in range(0, self.number_of_pages + 1):
                self.start_urls.append(
                    f"https://virgool.io/?page={i}"
                )

        logger.info('urls are appended')

    def parse(self, response, **kwargs):
        try:
            if self.gather_index_pages:
                for item in range(1, 20):
                    url = response.css(f'main#app article:nth-child({item}) > div > a::attr(href)').get()
                    if url:
                        with Path('virgool/index.txt').open("a") as f:
                            f.write(url + '\n')
            else:
                item = {'title': response.css('main#app h1::text').get(),
                        'author': response.css('main#app div.module-header > a::text').get(),
                        'text': "\n\n".join(response.css('main#app div.post-content * ::text').getall()),
                        'url': response.css('.shorturl-text::text').get()}
                # if I use strip on all of them I may get error. I have to check if it is not none.
                for key in item:
                    if item[key]:
                        item[key] = re.sub(' +', ' ', item[key]).strip()

                return item
        except Exception:
            logger.error("Parsing Error: ", exc_info=True)

    def handle_error(self, failure):
        logger.warning("Error,", failure.request.url)
        yield scrapy.Request(
            url=failure.request.url,
            dont_filter=True,
            callback=self.parse,
            errback=self.handle_error)
