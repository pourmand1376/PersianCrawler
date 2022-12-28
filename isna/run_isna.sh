while true; do
    read -p "Do you wish to remove this run and run crawler again? " yn
    case $yn in
        [Yy]* ) rm isna/kaggle/isna.csv
                scrapy runspider --set FEED_EXPORT_ENCODING=utf-8 isna.py -o isna/kaggle/isna.csv  -a from_year=1378 -a to_year=1401 ; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done

