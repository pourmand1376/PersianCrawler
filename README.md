# TasnimNewsCrawler
A Crawler to save all [tasnim news](https://www.tasnimnews.com/) pages based on category. This is appopriate for text classification task. 

[![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/code/amirpourmand/text-classification-tasnim)

## Installation Guide

To start, you have to install scrapy using:

```bash
pip install scrapy
```

Then clone it and start crawling:
```bash
git clone https://github.com/pourmand1376/TasnimNewsCrawler/
cd TasnimNewsCrawler 
./run.sh
```

> We have also a parameter Called `Number_of_pages` which controls how many pages we should crawl in each category. 


Dataset is available for download at [Kaggle](https://www.kaggle.com/datasets/amirpourmand/tasnimdataset) or [github](https://github.com/pourmand1376/TasnimNewsCrawler/raw/main/tasnim.zip). 

Cite my dataset via:
```
@misc{ 
        amir_pourmand_2022,
        title={TasnimDataset},
        url={https://www.kaggle.com/dsv/3500080}, 
        DOI={10.34740/KAGGLE/DSV/3500080},
        publisher={Kaggle}, 
        author={Amir Pourmand},
        year={2022} 
    }
```


