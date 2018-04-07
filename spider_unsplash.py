# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# capture pictures on unsplash.com

import requests
from bs4 import BeautifulSoup
import re
import os

class beautifulPicture():
	def __init__(self):
		self.web_url = 'https://unsplash.com'
		self.headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0.2 Safari/602.3.12'}
		self.folder_path = '/Users/storm/Code/Python Workspace/spider/unsplash pics'

	def get_pics(self):
		print('start to get the web...\n')
		html = self.request(self.web_url)
		print('开始获取所有a标签\n')
		all_a = BeautifulSoup(html.text, 'lxml').find_all('a', class_="cV68d")
		print('开始创建文件夹')
		self.mkdir(self.folder_path)
		print('切换到创建的文件夹')
		os.chdir(self.folder_path)

		for a in all_a:
			img_str = a['style']
			print('a标签的内容是：', img_str)
			img_first_pos = img_str.index('"')+1
			img_second_pos = img_str.index('"', img_first_pos)
			img_url = img_str[img_first_pos: img_second_pos]
			img_width_pos = img_url.index('&w=')
			img_height_pos = img_url.index('&q=')
			img_width_height_str = img_url[img_width_pos: img_height_pos]
			print('图片宽高字符串：', img_width_height_str)
			img_final_url = img_url.replace(img_width_height_str, '')
			print('原版大图地址：', img_final_url)
			name_start_pos = img_final_url.index('com/')+ 4
			name_end_pos = img_final_url.index('?dpr')
			img_name = img_final_url[name_start_pos: name_end_pos]
			self.save_img(img_final_url, img_name)

	def save_img(self, img_url, img_name):
		print('开始请求图片地址，请耐心等待。。。')
		img = self.request(img_url)
		file_name = img_name+ '.jpg'
		print('开始保存图片。。。')
		f = open(file_name, 'ab')
		f.write(img.content)
		print(file_name, '保存成功')
		f.close()

	def mkdir(self, path):
		path = path.strip()
		isExists = os.path.exists(path)
		if not isExists:
			print('新建文件夹：', path)
			os.makedirs(path)
			print('创建成功')
		else:
			print('文件夹', path, '已经存在')

	def request(self, url):
		return requests.get(self.web_url, headers = self.headers)

beauty = beautifulPicture()
beauty.get_pics()


# url = 'https://unsplash.com'
# headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0.2 Safari/602.3.12'}
# html = requests.get(url, headers = headers)
# soup = BeautifulSoup(html.text, 'lxml')
# all_a = soup.find_all('a',class_="cV68d")  # html里的class字段加下划线，避免关键字冲突
# img_links = []
# for a in all_a:
# 	# print(a['style'])
# 	# img_url = re.search(r'url\("(.*?)"\)',a['style'],re.S).group(1)
# 	img_str = a['style']
# 	print('a标签的内容是：', img_str)
# 	url_first_pos = img_str.index('"')+1
# 	url_second_pos = img_str.index('"', url_first_pos)
# 	img_url = img_str[url_first_pos: url_second_pos]
# 	img_width_pos = img_url.index('&w=')
# 	img_height_pos = img_url.index('&q=')
# 	img_width_height_str = img_url[img_width_pos: img_height_pos]
# 	print('图片宽高字符串是：', img_width_height_str)
# 	img_final_url = img_url.replace(img_width_height_str, '')
# 	print('图片地址是：', img_final_url)
# 	# 截取网址后面，参数前面的字符串为文件名
# 	name_start_pos = img_final_url.index('com/')+4
# 	name_end_pos = img_final_url.index('?dpr=')
# 	img_name = img_final_url[name_start_pos: name_end_pos]
# 	print('图片名：', img_name)
# 	img_links.append(img_final_url)
# print(len(img_links))



