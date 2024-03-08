import json
import os
import logging
class Settings:

    filename = 'config.json'
    configData = None
    book = ''

    def __init__(self,filename=None):
        if filename:
            self.filename = filename
        with open(self.filename) as f:
            self.configData = json.load(f)
            self.book = self.getBook()

    def saveSetting(self,key,value):
        with open(self.filename) as json_file:
            json_decoded = json.load(json_file)

        json_decoded[key] = value

        with open(self.filename, 'w') as json_file:
            json.dump(json_decoded, json_file)


    def getFilename(self):
        filename = ''
        if 'filename' in  self.configData[self.book]:
            filename =  self.configData[self.book]['filename']
        if filename is '':
            logging.error('No Output File Given!')
            return 'unknown.html'
        return filename

    def getStartUrl(self):
        startPages = []
        if 'startingPage' in self.configData:
            startPage = self.configData['startingPage']
            if type(startPage) is list:
                startPages =  startPage
            elif startPage is '':
                logging.error('No Starting URL Given!')
                return startPages
            else:
                startPages.append(startPage)
        if not startPages:
            logging.error('No Starting URL Given!')
        return startPages

    def getTitle(self):
        title = ''
        if 'title' in self.configData[self.book]:
            title = self.configData[self.book]['title']
        if title is '':
            logging.error('No Title Given!')
        return title

    def getCover(self):
        cover = ''
        if 'cover' in self.configData[self.book]:
            cover = self.configData[self.book]['cover']
        if cover is '':
            logging.error('No Cover Given!')
        return cover

    def getBook(self):
        if 'book' in self.configData:
            book = self.configData['book']
            return book
        raise ValueError("No book set")

    def getAuthors(self):
        authors = ''
        if 'authors' in self.configData[self.book]:
            authors = self.configData[self.book]['authors']
        if authors is '':
            logging.error('No Authors Given!')
        return authors

    @staticmethod
    def getBookDir():
        bookDir = 'Books'
        dirPath = os.path.join(os.path.dirname(__file__),bookDir)
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)
        return dirPath

    def getBookDir(self):
        bookDir = ''
        if 'bookDir' in self.configData:
            bookDir = self.configData['bookDir']
        if bookDir is '':
            logging.error('No Book Dir Given!')
            bookDir = 'Books'

        dirPath = os.path.join(os.path.dirname(__file__),bookDir)
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)
        return dirPath


    def getHtmlDir(self):
        htmlDir = ''
        if 'htmlDir' in self.configData:
            htmlDir = self.configData['htmlDir']
        if htmlDir is '':
            logging.error('No html Dir Given!')
            htmlDir = 'ScrapedPages'
        return htmlDir

    def getHTMLFilePath(self,fileName):
        htmlDir = self.getHtmlDir()
        dirPath = os.path.join(os.path.dirname(__file__),htmlDir)
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)

        return os.path.join(dirPath,fileName)

    @staticmethod
    def getHTMLFilePath(fileName):
        htmlDir = 'ScrapedPages'
        dirPath = os.path.join(os.path.dirname(__file__),htmlDir)
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)

        return os.path.join(dirPath,fileName)
