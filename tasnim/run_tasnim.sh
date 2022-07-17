while true; do
    read -p "Do you wish to remove this run and run crawler again? " yn
    case $yn in
        [Yy]* ) rm tasnim/kaggle/tasnim.csv
                scrapy runspider --set FEED_EXPORT_ENCODING=utf-8 tasnim.py -o tasnim/kaggle/tasnim.csv ; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done

