import json

class Settings:

    filename = 'config.json'
    configData = None

    def __init__(self,filename=None):
        if filename:
            self.filename = filename
        with open(self.filename) as f:
            self.configData = json.load(f)

    def saveSetting(self,key,value):
        with open(self.filename) as json_file:
            json_decoded = json.load(json_file)

        json_decoded[key] = value

        with open(self.filename, 'w') as json_file:
            json.dump(json_decoded, json_file)


    def getFilename(self):
        filename = ''
        if 'filename' in self.configData:
            filename = self.configData['filename']
        if filename is '':
            logging.error('No Output File Given!')
            return 'unknown.html'
        return filename

    def getStartUrl(self):
        startPage = ''
        if 'startingPage' in self.configData:
            startPage = self.configData['startingPage']
        if startPage is '':
            logging.error('No Starting URL Given!')
        return startPage

    def getTitle(self):
        title = ''
        if 'title' in self.configData:
            title = self.configData['title']
        if title is '':
            logging.error('No Title Given!')
        return title

    def getAuthors(self):
        authors = ''
        if 'authors' in self.configData:
            authors = self.configData['authors']
        if authors is '':
            logging.error('No Authors Given!')
        return authors
