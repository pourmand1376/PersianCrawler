rm wikipedia/kaggle/wikipedia.csv
scrapy runspider --set FEED_EXPORT_ENCODING=utf-8 wikipedia.py -o wikipedia/kaggle/wikipedia.csv