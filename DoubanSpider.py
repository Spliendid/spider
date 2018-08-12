import urllib.request as Req
from bs4 import BeautifulSoup
from urllib import parse
class Urldownload(object):
	"""docstring for ClassName"""
	def GetHtml(url):
		response = Req.urlopen(url)
		if response.getcode()!=200:
			return None
		return response.read()
class  Parse(object):
	"""docstring for  Parse"""
	def GetRating(htmlDoc):
		bs = BeautifulSoup(htmlDoc,'html.parser',from_encoding = 'utf-8')
		#<span class="rating_nums">5.4</span>
		link = bs.find('span',class_="rating_nums")
		if link==None:
			return 0
		return link.get_text()
class Main(object):
	"""docstring for ClassName"""
	def spider(name,year=''):
		url = "https://www.douban.com/search?q={}".format(parse.quote(name))
		doc =  Urldownload.GetHtml(url)
		return Parse.GetRating(doc)
		


