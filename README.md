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

```bash
wikipedia/run_wikipedia.sh
```

### Tasnim News
This crawler saves [tasnim news](https://www.tasnimnews.com/) pages based on category. This is appopriate for text classification task as data is relatively balanced across all categories. I selected equal amount of page per category. 

> We have a parameter Called `Number_of_pages` in `tasnim.py` which controls how many pages we should crawl in each category. 

```bash
tasnim/run_tasnim.sh
```

Dataset is available for download at [Kaggle](https://www.kaggle.com/amirpourmand/datasets)




