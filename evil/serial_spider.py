import scrapy

class SerialSpider(scrapy.Spider):
    name = "Evil"
    #chapter Index
    chapter = 0

    # Table of contents
    toc = "<h1>Table of Contents</h1>"
    bookContent = ""
    start_urls = ["https://practicalguidetoevil.wordpress.com/2015/11/04/prologue-2/"]
    endUrl = 'https://practicalguidetoevil.wordpress.com/2017/02/08/prologue-3/'


    def parse(self, response):
        chapterTitle = response.xpath('//h1[@class="entry-title"]')
        # HTML Title for Table of content
        chapterTitleClean = chapterTitle.xpath('text()').extract().pop(0).encode('utf-8')
        chapterContent = response.xpath('//div[@class="entry-content"]/p').extract()
        # # Removes next chapter from top of content
        # chapterContent.pop(0)
        # # Removes next chapter from end of content
        # chapterContent.pop(-1)

        # Next chapter should be last in links list
        nextChapter = response.xpath('//div[@class="nav-next"]/a/@href').extract_first()


        self.bookContent += '<h1 id="chap#%d">%s</h1>' % (self.chapter, chapterTitleClean)
        self.toc += '<a href="#chap#%d">%s</a><br>' % (self.chapter, chapterTitleClean)
        self.bookContent = self.bookContent + '' .join(chapterContent).encode('utf-8')
        self.chapter += 1


        if nextChapter and nextChapter != self.endUrl:
        #if self.chapter < 10:
            url = nextChapter
            yield scrapy.Request(url, self.parse)
        else:
            filename = 'evil2.html'
            with open(filename, 'wb') as f:
                f.write(self.toc)
                f.write(self.bookContent)
            pass
