from bs4 import BeautifulSoup
from urllib import parse
import  re
class HtmlParser(object):
    #获取页面中新的url
    def _get_new_urls(self, html_cont, soup):
        new_urls = set()
        #/view/123.html
        links = soup.find_all('a',href = re.compile(r"/item/?"))
        for link in links:
            new_url = link['href']
            ##print(new_url)
            #将url拼接补全
            new_full_url = 'http://baike.baidu.com'+new_url
            new_urls.add(new_full_url)
        return new_urls
    #获取所要爬取的信息
    def _get_new_data(self, page_url, soup):
        #定义字典
        res_data = {}
        #url
        res_data['url'] = page_url
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find('h1')
        #url-title
        res_data['title'] =title_node.get_text()
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div',class_="lemma-summary")
        #url-summary
        res_data['summary'] = summary_node.get_text()
        return res_data


    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(html_cont,soup)
        new_data = self._get_new_data(html_cont,soup)
        ##print(len(new_urls))
        return new_urls,new_data

