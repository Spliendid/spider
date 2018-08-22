import html_downloader
import html_outputer
import html_parser
import url_manager

class SpiderMain (object):
    def __init__(self):
        self.urls = url_manager.UrlManager ()
        self.downloader = html_downloader.HtmlDownloader ()
        self.outputer = html_outputer.HtmlOutputer()
        self.parser = html_parser.HtmlParser()

    def craw(self,root_url):
        # 添加入口url
        self.urls.add_new_url (root_url)
        count = 1
        # 如果有新的URL就执行循环
        while self.urls.has_new_url ():
            # 获取 new url
            new_url = self.urls.get_new_url ()
            print ('craw %d : %s' % (count, new_url))
            # 下载urldoc
            html_cont = self.downloader.download(root_url)
            # 解析urldoc
            new_urls, new_data = self.parser.parse(new_url, html_cont)
            ##print(new_urls)
            # 添加新的url地址
            self.urls.add_new_urls(new_urls)
            # 添加输出内容
            self.outputer.collect_data (new_data)
            if count >= 20:
                break
            count = count + 1
        self.outputer.output_html ()


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.html"
    obj_spider = SpiderMain ()
    obj_spider.craw(root_url)
