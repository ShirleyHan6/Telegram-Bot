# -*- coding: utf-8 -*-
import urllib
import urllib.request
from bs4 import BeautifulSoup


def software(n,x):
    # main url&headers inicialize
    url = "https://phys.org/technology-news/software/"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
    # access the main url
    req = urllib.request.Request(url=url,headers=headers)  
    response = urllib.request.urlopen(req) 
    content = response.read().decode('utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    # get the titles and sub urls of the news
    titles = soup.find_all("article",limit = 5)
    sub_url = titles[n].h3.a['href']
    # format a piece of news
    if x == 0:
        one_news = 'Title:\n' + titles[n].h3.string +\
                   '\nRead more at: ' + sub_url + '\n' * 2
    else:
        # access the sub urls
        subreq = urllib.request.Request(url=sub_url,headers=headers)  
        subresponse = urllib.request.urlopen(subreq) 
        subcontent = subresponse.read().decode('utf-8')
        subsoup = BeautifulSoup(subcontent, 'html.parser')
        # delete unwanted text
        if subsoup.find(attrs = {"class":"image-block"}) != None:
            [s.extract() for s in subsoup.find_all(attrs = {"class":"image-block"})]
        [s.extract() for s in subsoup.find_all(attrs = {"class":"article-banner"})]
        [s.extract() for s in subsoup.find_all(attrs = {"class":"news-relevant"})]
        [s.extract() for s in subsoup.find_all("footer")]
        [s.extract() for s in subsoup.find_all("script")]
        # get the date and content of the news
        one_news_content = subsoup.find("article")
        date = subsoup.find("h5")
        # delete extra white space and while line
        one_news_content = "".join(line.strip() for line in one_news_content.text.split("\n"))
        date = "".join(string.strip() for string in date.string.split("\n"))
        # format a piece of news
        one_news = 'Title:\n' + titles[n].h3.string +\
                   '\nDate:\n' + date + \
                   '\nContent:\n' + one_news_content + '\n' * 3  
    # to make sure the text does not exceed the length limit for telebot
    if len(one_news)<4096:
        return str(one_news)
    else:
        return 'The news processed exceed the length limit,trying to process \
the next news...(as a result, the number of news will be less than 5 pieces)'

def electronics(n,x):
    # main url&headers inicialize
    url = "https://www.electronicsweekly.com/news/"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
    # access the main url
    req = urllib.request.Request(url=url,headers=headers)  
    response = urllib.request.urlopen(req) 
    content = response.read().decode('utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    # get the title and date of the news
    titlesanddates = soup.find_all("article",limit = 5)
    # get sub urls from the href content
    links = soup.find_all(attrs = {"class":"post-thumbnail"},limit = 5)
    sub_url = links[n].a['href']
    #format a piece of news
    if x == 0:
        one_news = 'Title:\n' + titlesanddates[n].h2.string +\
                   '\nRead more at:\n ' + sub_url + '\n' * 2
    else:
        # access the sub urls
        subreq = urllib.request.Request(url=sub_url,headers=headers)  
        subresponse = urllib.request.urlopen(subreq) 
        subcontent = subresponse.read().decode('utf-8')
        subsoup = BeautifulSoup(subcontent, 'html.parser')
        # remove unwanted text
        [s.extract() for s in subsoup.find_all("script")]
        if subsoup.find(attrs = {"class":"shortc-button"}) != None:
            [s.extract() for s in subsoup.find_all(attrs = {"class":"shortc-button"})]
        # get the text of the news artical
        sub_news_content = subsoup.find_all('div',class_ = 'post-inner')
        one_news_content = ''
        for sub in sub_news_content:
            one_news_content = one_news_content + sub.div.text
        one_news_content = "".join(line.strip() for line in one_news_content.split("\n"))
        # format a piece of news
        one_news = 'Title:\n' + titlesanddates[n].h2.string +\
                   '\nDate:\n' + titlesanddates[n].span.string +\
                   '\nContent:\n ' + one_news_content + '.' + '\n' * 3
    # to make sure the text does not exceed the length limit for telebot
    if len(one_news)<4096:
        return str(one_news)
    else:
        return 'The news processed exceed the length limit,trying to process \
the next news...(as a result, the number of news will be less than 5 pieces)'

def hardware(n,x):
    # main url&headers inicialize
    url = "http://www.tomshardware.co.uk/"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
    # access the main url
    req = urllib.request.Request(url=url,headers=headers)  
    response = urllib.request.urlopen(req) 
    content = response.read().decode('utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    # get the titles and sub urls of the news
    titlesandlinks = soup.find_all(attrs = {"class":"listing-item"},limit = 5)
    sub_url = url + titlesandlinks[n].a['href']
    # delete extra white space and while line
    titlesandlinks[n] = "".join(line.strip() for line in titlesandlinks[n].a.string.split("\n"))
    if x == 0:
        one_news = 'Title:\n' + titlesandlinks[n] +\
                   '\nRead more at: ' + sub_url + '\n' * 2
    else:
        # access the sub urls
        subreq = urllib.request.Request(url=sub_url,headers=headers)  
        subresponse = urllib.request.urlopen(subreq) 
        subcontent = subresponse.read().decode('utf-8')
        subsoup = BeautifulSoup(subcontent, 'html.parser')
        # delete unwanted text
        [s.extract() for s in subsoup.find_all("script")]
        [s.extract() for s in subsoup.find_all("style")]
        if subsoup.find_all(attrs = {"class":"carousel-single-css-title-cont"}) != None:
            [s.extract() for s in subsoup.find_all(attrs = {"class":"carousel-single-css-title-cont"})]
        if subsoup.find_all(attrs = {"class":"carousel-multi-css-item-caption"}) != None:
            [s.extract() for s in subsoup.find_all(attrs = {"class":"carousel-multi-css-item-caption"})]
        # get the date of the news
        date = subsoup.find("time")
        # get the content of the news
        one_news_content = subsoup.find(attrs = {"class":"content"})
        # delete extra white space and while line
        one_news_content = "".join(line.strip() for line in one_news_content.text.split("\n"))
        # format a piece of news
        one_news = 'Title:\n' + titlesandlinks[n] +\
                   '\nDate:\n' + date.string +\
                   '\nContent:\n' + one_news_content + '\n' * 3
    # to make sure the text does not exceed the length limit for telebot
    if len(one_news)<4096:
        return str(one_news)
    else:
        return 'The news processed exceed the length limit,trying to process \
the next news...(as a result, the number of news will be less than 5 pieces)'

def ProjectExample(n,kind):
    # main url&headers inicialize
    if kind == 'Arduino':
        url = "http://www.instructables.com/id/Arduino-Projects/"
    if kind == 'RaspberryPi':
        url = "http://www.instructables.com/id/Raspberry-Pi-Projects/"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
    # access the main url
    req = urllib.request.Request(url=url,headers=headers)  
    response = urllib.request.urlopen(req) 
    content = response.read().decode('utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    # get the titles and links of the project
    titlesandlinks = soup.find_all(attrs = {"class":"caption-inner"})
    # format one project example
    results = 'Title:\n ' + titlesandlinks[n].p.a.string + \
              '\nRead more at:\n'+ 'http://www.instructables.com'+ \
              titlesandlinks[n].p.a['href']
    return(str(results))


