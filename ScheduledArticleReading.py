'''
A code to scrape articles from The Atlantic

Code by Vivek Pothina

'''
from threading import Timer as timer
from bs4 import BeautifulSoup as bs
from urllib2 import urlopen
from re import findall
from random import choice
from subprocess import Popen

base_url = "https://www.theatlantic.com"
re_pattern = r"(\/international\/archive\/20)[\d][\d]\/[\d][\d]\/"
file_name = "Article.txt"
minutes = 60*2
count = 0
page_url = "?page="

def getData():
    i = choice([2,3,4])
    article_links = []
    try:
        soup = bs(urlopen(base_url+"/international/"), "lxml")
        soup_extra = bs(urlopen(base_url+"/international/"+page_url+str(i)), "lxml")
    except Exception as e:
        print(e)
        return None
    a_tags = soup.find_all("a")
    a_tags_extra = soup_extra.find_all("a")
    article_links = []
    for a in a_tags:
        if(findall(pattern=re_pattern, string=str(a.get('href')))):
            article_links.append(str(a.get('href')))
    for a in a_tags_extra:
        if(findall(pattern=re_pattern, string=str(a.get('href')))):
            article_links.append(str(a.get('href')))
    return article_links

def getArticle():
    global count
    print("Fetching Article " + str(count) + " ........")
    count = count + 1
    # print(base_url+"/international/")
    article_links = getData()
    if not article_links:
        t1 = timer(60*minutes, getArticle)
        t1.start()
    article_link = choice(article_links)
    # print(article_link)
    # print(base_url+article_link)
    article_soup = bs(urlopen(base_url+article_link), "lxml")

    p_tags = article_soup.find_all("p")
    with open(file_name, "w") as file:
        header = findall(pattern=">(.*)<", string=str(article_soup.find_all("h1")))
        file.write(header[0].encode('utf-8') + "\n\n")
        for p in p_tags:
            txt = p.getText().encode('utf-8')
            file.write(txt + "\n")

    Popen(['start', 'Article.txt'], shell= True)
    t = timer(60*minutes, getArticle)
    t.start()

getArticle()