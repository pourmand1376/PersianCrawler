[![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/amirpourmand/datasets)

# Crawler
Open source crawler for Persian websites. Crawled websites to now:
- [Asriran](https://www.kaggle.com/datasets/amirpourmand/asriran-news)
- [Fa-Wikipedia](https://www.kaggle.com/datasets/amirpourmand/fa-wikipedia)
- [Tasnim](https://www.kaggle.com/datasets/amirpourmand/tasnimdataset)

### Asriran

```bash
asriran/run_asriran.sh
```

> You can change some paramters in this crawler. See `run_asriran.sh`.

### Fa-Wikipedia

Due to some problems in crawling, I splitted this job into two stages. First crawling all index pages and second use those pages for crawling. 
```bash
wikipedia/run_wikipedia.sh
```

### Tasnim News
This crawler saves [tasnim news](https://www.tasnimnews.com/) pages based on category. This is appopriate for text classification task as data is relatively balanced across all categories. I selected equal amount of page per category. 

> We have a parameter Called `Number_of_pages` in `tasnim.py` which controls how many pages we should crawl in each category. 

```bash
tasnim/run_tasnim.sh
```

Datasets are all available for download at [Kaggle](https://www.kaggle.com/amirpourmand/datasets).

CSS selectors are mostly extracted via [Copy Css Selector](https://chrome.google.com/webstore/detail/copy-css-selector/kemkenbgbgodoglfkkejbdcpojnodnkg?hl=en).




- https://stackoverflow.com/questions/73859249/attributeerror-module-openssl-ssl-has-no-attribute-sslv3-method
- https://stackoverflow.com/a/73867925/4201765