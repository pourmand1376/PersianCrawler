import scrapy
from pathlib import Path
from logger import logger
import json
from trafilatura import  extract

class TarjomanSpider(scrapy.Spider):
    name = "Tarjoman"

    custom_settings = {'AUTOTHROTTLE_ENABLED': True,
                       'HTTPCACHE_ENABLED': True,
                       'CONCURRENT_REQUESTS': 100,
                       'CONCURRENT_REQUESTS_PER_DOMAIN': 100,
                       }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = []
        if Path('tarjoman/index.txt').exists():
            text = Path('tarjoman/index.txt').read_text(encoding='utf-8')
            items = json.loads(text)
            self.start_urls = items

            logger.info(f'{len(self.start_urls)} urls fetched.')

    def parse(self, response, **kwargs):
        try:
            item = {'title': response.css('main#app h1::text').get().strip(),
                    'author': response.css('main#app div.module-header > a::text').get().strip(),
                    'text': "\n\n".join(response.css('main#app div.post-content * ::text').getall()),
                    'url': response.css('.shorturl-text::text').get()}
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