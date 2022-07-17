while true; do
    read -p "Do you wish to remove this run and run crawler again? " yn
    case $yn in
        [Yy]* ) rm asriran/kaggle/asriran.csv
        scrapy runspider --set FEED_EXPORT_ENCODING=utf-8 asriran.py -o asriran/kaggle/asriran.csv \
            -a from_page=1 -a to_page=8313 \
            -a from_date='1384/01/01' -a to_date='1401/04/24'; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done