from __future__ import print_function

import requests, os
from urllib2 import urlopen
from bs4 import BeautifulSoup as bs
from time import sleep


base_url1 = "http://dl.upload8.in/files/"
base_url = "http://sv4avadl.uploadt.com/"
tv_url = "Serial/"
base_url2 = "http://fromv.ir/vip/Series/Ongoing/"
comics_url = "http://www.pinkasimov.com/Livres/Comics/"
anime_url1 = "https://storage.kanzaki.ru/ANIME___/"


def printLinks(url, slice_num = 0):
	print("You're at " + url)
	try:
		# soup = bs(requests.get(url).text)
		soup = bs(urlopen(url))
		count = 0
		for link in soup.find_all('a'):
			print(count,link.get('href')[slice_num:])
			count = count+1
		return str(url)

	except Exception as e:
		print("Oops! There seems to be a problem, but wait its gonna restart!")
		print(e)
		start()
		return 0

def getSeries(num):
	if num == 1:
		base_u = base_url2
		next_url = printLinks(base_u)
	elif num == 2:
		base_u = base_url
		next_url = printLinks(base_u+tv_url)
	elif num == 3:
		base_u = comics_url
		next_url = printLinks(base_u)
	elif num == 4:
		base_u = anime_url1
		next_url = printLinks(base_u)
	elif num == 0:
		base_u = raw_input("Enter base url: ")
		next_url = printLinks(base_u)
	else:
		base_u = base_url
	
	series_url = raw_input("Enter choice: ")
	getLinks(next_url+series_url)
	# printLinks(base_url + tv_url + series_url, 14+len(series_url))
	# season_url = raw_input("Enter choice of season: ")
	# printLinks(base_url + tv_url + series_url+season_url, 14+len(series_url)+len(season_url))
	# quality_url = raw_input("Enter choice of quality: ")
	# printLinks(base_url + tv_url + series_url+season_url+quality_url, 14+len(series_url)+len(season_url)+len(quality_url))
	# choice = raw_input("Hit 1 to download all!")

def getLinks(next_url, slice_bool=False):
	if(slice_bool):
		slice_num = len(next_url)-20
	else:
		slice_num = 0
	print("URL at getLinks: "+ next_url)
	next_url = printLinks(next_url)
	choice = raw_input("Enter choice: ")
	if choice == '1':
		print("Yay! Downloading....")
		downloadLinks(next_url)
	elif choice == '0':
		getLinks(next_url, False)
	else:
		getLinks(next_url+choice, True)

def startDelay(t):
	for i in range(0,t):
		print("Wait for another " + str((t-i)/60) + " minutes.", end='\r')
		sleep(1)

def downloadLinks(url):
	soup = bs(urlopen(url))
	choice = raw_input("Input line nums with commas: ")
	dlist = choice.split(',')
	print(dlist)
	links = list(soup.find_all('a'))
	delay = int(raw_input("Thank you, can you please specify delay time: "))
	idm_cmd = ".\IDMan.exe /n /d "
	for num in dlist:
		print(num, links[int(num)].get('href'))
		print(idm_cmd+links[int(num)].get('href'))
		os.system(idm_cmd+url+links[int(num)].get('href'))
		startDelay(delay*60)

def start():
	choice = int(raw_input("Enter 1 for "
	+ base_url2 
	+" \n and Enter 2 for http://sv4avadl.uploadt.com/\nEnter 3 for comics "
	+comics_url
	+"\nEnter 4 for anime"
	+anime_url1
	+"\nEnter 0 for adding custom base url"
	+"\nEnter: "))
	getSeries(choice)

print("Welcome! Press 1 to download and 0 to disable slicing...")
start()