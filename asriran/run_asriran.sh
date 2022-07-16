rm asriran/kaggle/asriran.csv
scrapy runspider --set FEED_EXPORT_ENCODING=utf-8 asriran.py -o asriran/kaggle/asriran.csv \
    -a from_page=1 -a to_page=8313 \
    -a from_date='1384/01/01' -a to_date='1401/04/24'