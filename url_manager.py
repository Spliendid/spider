class UrlManager(object):

    def __init__(self):
        self.new_urls = set()#定义空的集
        self.old_urls = set()#定义空的集
    def add_new_url(self, root_url):
        if root_url is None:
            return
        if root_url not in self.new_urls and root_url not in self.old_urls:
            self.new_urls.add(root_url)
        pass
    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return  len(self.new_urls)!=0


    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
        pass