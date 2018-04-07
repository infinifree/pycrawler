# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# capture url of android apps in apk.hiapk.com
# step 1: locate a web page which has 10 apps' link
# step 2: get download link 
# step 3: turn to the next page, repeat step 2
# step 4: when all pages are captured, save all the links as a txt file

import requests
import re
import sys

class spider(object):
	def __ini__(self):
		print('Spider is on your order...')

	def getpage(self,url):
		return requests.get(url).text

	def turnpage(self,current_page):
		page_index = int(re.search('pi=(\d+)',current_page).group(1))
		next_page_index = page_index+1
		next_page = re.sub('pi=(\d+)','pi=%s'%next_page_index,current_page)
		return next_page

#	def getallapps(self,page):
#		return re.findall('(<li class="list_item">.*?</li>)',page,re.S)

	def getapplinks(self,page):
		appbox = re.findall('(<li class="list_item">.*?</li>)',page,re.S)
		applinks = []
		for s in appbox:
			info_link = re.search('<a href="(.*?)">',s,re.S).group(1)
			down_link = info_link.replace('appinfo','appdown')
			applinks.append(down_link)
			print(down_link)
		#print(applinks)
		return applinks

	def saveapplinks(self,applinks):
		f = open('links.txt','a')
		base_url = 'http://apk.hiapk.com'
		for s in applinks:
			f.write(base_url+s+'\n')
		f.close()


if __name__ == '__main__':
	myspider = spider()
	url = 'http://apk.hiapk.com/apps?sort=5&pi=1'
	total_page = 21
	applinks = []
	for i in range(1,total_page+1):
		print('正在处理页面🏂：\n'+url)
		applinks = applinks+myspider.getapplinks(myspider.getpage(url))
		url = myspider.turnpage(url)
	myspider.saveapplinks(applinks)
	print('well done! 😀 😀 😀')

