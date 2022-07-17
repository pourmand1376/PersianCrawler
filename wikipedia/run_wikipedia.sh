while true; do
    read -p "Do you want to build index.txt file? (This is required for the first time. Crawler uses index.txt as starting point) " yn
    case $yn in
        [Yy]* ) rm wikipedia/kaggle/index.txt
                scrapy runspider --set FEED_EXPORT_ENCODING=utf-8 wikipedia.py -o wikipedia/kaggle/wikipedia.csv -a gather_index_pages=True; exit;;
        [Nn]* ) echo "You chose not to build index.txt file. Going forwrd to crawl the wikipedia"; break;;
        * ) echo "Please answer yes or no.";;
    esac
done

while true; do
    read -p "Do you wish to crawl from scratch? " yn
    case $yn in
        [Yy]* ) rm wikipedia/kaggle/wikipedia.csv
                scrapy runspider --set FEED_EXPORT_ENCODING=utf-8 wikipedia.py -o wikipedia/kaggle/wikipedia.csv -a gather_index_pages=False; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done

