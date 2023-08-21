from logger import logger
import scrapy
import logging
from scrapy.utils.log import configure_logging
from pathlib import Path

class EnsaniSpider(scrapy.Spider):
    name= "Ensani"

    start_urls = []
    custom_settings = {'AUTOTHROTTLE_ENABLED':True,
                        'HTTPCACHE_ENABLED':True,
                        'CONCURRENT_REQUESTS':30,
                        'CONCURRENT_REQUESTS_PER_DOMAIN':30,
                      }

    configure_logging(install_root_handler=False)
    logging.basicConfig(
        filename='log.txt',
        format='%(levelname)s: %(message)s',
        level=logging.INFO
    )

    def __init__(self, **kwargs):
        # همه صفحه ها
        super().__init__(**kwargs)
        try:
            self.start_urls = []
            end_page = 21141
            for i in range(1,end_page+1):
                url = f"https://ensani.ir/fa/article/field/3363?ArticleSearch%5BpageSize%5D=20&ArticleSearch%5BscientificRank%5D=&ArticleSearch%5BjournalId%5D=&ArticleSearch%5Byear%5D=&ArticleSearch%5Blanguage%5D=1&ArticleSearch%5Btitle%5D=&ArticleSearch%5BsortBy%5D=&page={i}"
                self.start_urls.append(url)
            logger.info('urls are appended')

        except Exception:
            logger.error('error', exc_info=True)

    def parse(self, response, **kwargs):
        try:
            abstract_array=response.css('div.well.collapse *::text')
            for item in abstract_array:
                output = {'text': item.get()}
                yield output
        except Exception:
            logger.error("Parsing Error: ", exc_info=True)

    def handle_error(self, failure):
        logger.warning("Error,", failure.request.url)
        yield scrapy.Request(
            url=failure.request.url,
            dont_filter=True,
            callback=self.parse,
            errback=self.handle_error)