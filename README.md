# learning_python_scrapy

## Scrapy Shell

`scrapy shell 'http://quotes.toscrape.com/'`

## Write to csv

`scrapy crawl quotes -o items.csv`

`scrapy crawl quotes -o items.json`

`scrapy crawl quotes -o items.xml`

## Runspider command

Use it to create a quick crawler and run it straight as a script:

`~/workspace (master) $ scrapy runspider quotes.py`

## Start Crawler

`scrapy crawl books`

## Pass argument to scrapy

`scrapy crawl books -a category="http://books.toscrape.com/catalogue/category/books/philosophy_7/index.html"`

## Export to Excel

### Install openpyxl
`sudo pip install openpyxl`


## Create project

`scrapy startproject testproject`

`scrapy genspider testspider "www.example.com"`



--> 20/050