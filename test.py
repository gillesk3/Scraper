from gtts import gTTS
from bs4 import BeautifulSoup

import logging

filename = 'evil3.html'

HtmlFile = open(filename, 'r', encoding='utf-8')
source_code = HtmlFile.read()

soup = BeautifulSoup(source_code, 'html.parser')




def getParaText(para):

    if not para:
        return ''

    dept = para[0].find('p')

    if dept:
        return getParaText(dept)

    else:
        return para[0].get_text() + getParaText(para[1:])








paras = soup.find_all('p')
sampleText = ''


para = paras[2:3]
# print(para)
#
for x  in range(2):
    p = paras[x]
    # print(p.find('p'))
    sampleText += paras[x].get_text()

print(sampleText)
tts = gTTS(sampleText, lang='en')
tts.save('test.mp3')
