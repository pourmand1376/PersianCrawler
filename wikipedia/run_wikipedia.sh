while true; do
    read -p "Do you wish to remove this run and run crawler again? " yn
    case $yn in
        [Yy]* ) rm wikipedia/kaggle/wikipedia.csv
                scrapy runspider --set FEED_EXPORT_ENCODING=utf-8 wikipedia.py -o wikipedia/kaggle/wikipedia.csv -a gather_index_pages=True; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done