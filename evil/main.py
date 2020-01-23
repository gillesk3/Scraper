import os
os.system("scrapy runspider serial_spider.py")
os.system("ebook-convert evil2.html evil2.mobi --authors 'Erratic Errata11' --title 'Evil 2' --max-toc-links 500")
print "******************"
