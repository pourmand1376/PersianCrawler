while true; do
    echo "Please put your extracted urls into tarjoman/index.txt"
    read -p "Do you wish to remove this run and run crawler again? " yn
    case $yn in
        [Yy]* ) rm tarjoman/kaggle/tarjoman.csv
                scrapy runspider --set FEED_EXPORT_ENCODING=utf-8 tarjoman.py -o tarjoman/kaggle/tarjoman.csv ; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done

