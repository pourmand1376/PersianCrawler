import scrapy
import re
from logger import logger


class IsnaSpider(scrapy.Spider):
    
    name = "Isna"
    start_urls = []
    custom_settings = {'AUTOTHROTTLE_ENABLED':True,
                        #'HTTPCACHE_ENABLED':True,  
                        # enabling http_cache quickly finished the storage!
                        #'CONCURRENT_REQUESTS':1000,
                        #'CONCURRENT_REQUESTS_PER_DOMAIN':1000,
                      }


    main_url = "https://www.isna.ir"
    
    def __init__(self ,from_year = 1378, to_year = 1401):
        # Set the range of values for the mn, dy, and yr parameters
        mn_range = range(1,32) 
        dy_range = range(1,13)
        yr_range = range(int(from_year),int(to_year)+1)
        pi_range= range(1,101)
        # Create an empty list to store the start URLs
        self.start_urls = []

        # Loop through the possible values for each parameter
        for mn in mn_range:
            for dy in dy_range:
                for yr in yr_range:
                    for pi in pi_range:
                        # Construct the URL using string formatting
                        url = f"https://www.isna.ir/archive?pi={pi}&ms=0&dy={dy}&mn={mn}&yr={yr}"
                        # Add the URL to the start_urls list
                        self.start_urls.append(url)

        # Print the start URLs
        logger.info('urls are appended')

    def handle_failure(self, failure):
        logger.warning("Error,", failure.request.url)
        yield scrapy.Request(
            url=failure.request.url,
            dont_filter=True,
            callback=self.parse,
            errback=self.handle_failure)

        
    def parse(self, response ):
        try:
            # we have a problem in isna which is unsolved. If you go to page 50, for example, it might show you some news from previous days! 
            # so acutally you should filter that out. 
            for news in response.css("div.items a::attr(href)").getall():
                if len(news.strip()) > 0:
                    yield scrapy.Request(
                        self.main_url+news,
                        callback=self.parse_news,
                    )
                    logger.info('added '+ self.main_url+news)
        except Exception:
            logger.error("Parsing Error: ", exc_info=True)

    def parse_news(self, response):
        try: 
            # I used pip install scrapy and scrapy shell to help me generate this content. 
            # scrapy shell
            # fetch(url)
            # then use reponse.css
            # also Copy CSS Selector was useful
            item = {
                'title': response.css('article#item h1::text').get(),
                'shortlink': response.css('input#short-url::attr(value)').get(),
                'time':  response.css('article#item li:nth-child(1) > span.text-meta::text').get(),
                'service': response.css('article#item li:nth-child(2) > span.text-meta::text').get(),
                'news_id': response.css('article#item li:nth-child(3) > span.text-meta::text').get(),
                'reporter': response.css('article#item li:nth-child(1) > strong::text').get(), 
                'managers': response.css('article#item li:nth-child(2) > strong::text').get(),
                'body': ' '.join(response.css('article#item div.item-body *::text').getall()),
            }
            
            # if I use strip on all of them I may get error. I have to check if it is not none. 
            for key in item:
                if item[key]:
                    item[key] = re.sub(' +', ' ', item[key]).strip()
            
            yield item

        except Exception:
            logger.error("Error", exc_info=True)
