from cmd import Cmd

from urllib.error import URLError
from urllib.request import urlopen, Request, urlretrieve
import requests
import os
from subprocess import Popen, PIPE
import argparse
from pathlib import Path
from bs4 import BeautifulSoup as bs
import re
from tqdm import tqdm


DEFAULT_DOWNLOAD_PATHS = {
    "anime": str(Path.home().joinpath("Entertainment/Anime & Manga/New Folder/")),
    "movie": str(Path.home().joinpath("Entertainment/Movies/")),
    "other": str(Path.home().joinpath("Downloads/Persepolis/Others/"))
}

DEFAULT_CONNECTIONS = "6"

COMMON_BASE_URLS = {
    "anime": "https://storage.kanzaki.ru/ANIME___/",
    "anime1": "http://sr1.animelist1.ir/E/Anime/",
    "hollywood": "http://dl8.heyserver.in/film/",
    "bollywood": "http://103.91.144.230/ftpdata/Movies/Bollywood/",
    "tv": "http://dl8.heyserver.in/serial/",
    "comic": "http://www.pinkasimov.com/Livres/Comics/"
}

nextUrl = ""
downloadPath = ""

def openUrl(url):
    try:
        req = Request(url, headers={'User-Agent': "Magic Browser"})
        response = urlopen(req)
        return response
    except Exception as e:
        print("Error with URL: (%s), please set valid URL, try again!" % e)
        return None

def getLinksAsList(url):
    req = Request(url, headers={'User-Agent': "Magic Browser"})
    soup = bs(urlopen(req), features="lxml")
    linksList = list(soup.find_all('a'))
    return linksList

def printLinks(url):
    print("You're at " + url+"\n")
    try:
        req = Request(url, headers={'User-Agent': "Magic Browser"})
        soup = bs(urlopen(req), features="lxml")
        count = 0
        for link in soup.find_all('a'):
            print(count,link.get('href'))
            count = count+1
        return str(url)
    except Exception as e:
        print("Oops! There seems to be a problem, try again! :| ")
        print("Error:" , e)

def downloadUrl(url, path, hrefName):
    chunkSize = 1024
    req = requests.get(url, stream=True)
    filename = hrefName
    with open(path+"/"+filename, 'wb') as f:
        pbar = tqdm(unit="MB", total=int(req.headers['Content-Length']))
        for chunk in req.iter_content(chunk_size=chunkSize): 
            if chunk: # filter out keep-alive new chunks
                pbar.update (len(chunk))
                f.write(chunk)
    return filename

def downloadUrlWithAria2c(url, path):
    cmd = "aria2c "
    cmd = cmd + "--dir='%s' " %(path)
    cmd = cmd + "--max-connection-per-server=%s " %(DEFAULT_CONNECTIONS)
    cmd = cmd + "'%s'" %(url)
    process = Popen(cmd, bufsize=1024, shell=True, stderr=PIPE)
    process.wait()
    output = process.communicate()
    print("o",output)
    if(output[0]): 
        return output[0]
    return True

class DownloadPrompt(Cmd):

    def do_setBaseUrl(self, url):
        if(url):
            print("Verifying the URL....")
            urlResponse = openUrl(url)
            if(urlResponse):
                global nextUrl
                nextUrl = url
                print("URL set! Proceed to next step...")
        else:
            print("Use this cmd to set Base Url, requires just one argument: URL")

    def do_selectFromCommonBaseUrls(self, choice):
        if(choice):
            global nextUrl
            nextUrl = COMMON_BASE_URLS[choice]
        else:
            print("Choose from ", COMMON_BASE_URLS.keys())

    def do_setDownloadPath(self, path):
        global downloadPath
        downloadPath = str(Path.home().joinpath(path))
        print(downloadPath)
        if(not Path(downloadPath).exists()):
            print("The download path is not valid, exiting the pgm!") 

    def do_selectFromDefaultDownloadPaths(self, choice):
        if(choice):
            global downloadPath
            downloadPath = DEFAULT_DOWNLOAD_PATHS[choice]
        else:
            print("Choose from ", DEFAULT_DOWNLOAD_PATHS.keys())

    def do_setMaxConnections(self, num):
        if(num):
            global DEFAULT_CONNECTIONS
            DEFAULT_CONNECTIONS = num
        else:
            print("Set max connections per server like 4 or 6")

    def do_navigate(self, url):
        global nextUrl
        currentUrl = nextUrl + url
        nextUrl = printLinks(currentUrl)

    def do_downloadRange(self, line):
        if(len(line.split(','))!=2):
            print("Requires input of format: 'num1,num2'")
        elif(nextUrl=="" or downloadPath==""):
            print("Before Downloading, set the Download Path and URL first")
        else:
            try:
                x,y = [int(num) for num in line.split(',')]
                linksList = getLinksAsList(nextUrl)
                for i in range(x, y+1):
                    downloadLink = nextUrl+str(linksList[i].get("href"))
                    # resp = urlretrieve(downloadLink, downloadPath+"/"+str(linksList[i].get("href")))
                    # resp = downloadUrl(downloadLink, downloadPath, str(linksList[i].get("href")))
                    resp = downloadUrlWithAria2c(url=downloadLink, path=downloadPath)
                    if(resp is True):
                        print("\n", linksList[i].get("href"), " done!\n")
                    else:
                        print(resp)
            except Exception as e:
                print("Error: %s, give right inputs" %e)

    def do_EOF(self, line):
        print("Quitting! Good Bye :(\n")
        return True

    def do_quit(self, args):
        print("Quitting! Good Bye :(\n")
        raise SystemExit


def main():
    prompt = DownloadPrompt()
    prompt.prompt = '> '
    prompt.cmdloop("Default Download Paths Availabe: \n"+
        str(DEFAULT_DOWNLOAD_PATHS.keys())+
        "\nCommon base urls available: \n"+
        str(COMMON_BASE_URLS.keys())+
        "\nStarting Download Prompt...")


if __name__ == '__main__':
    main()
