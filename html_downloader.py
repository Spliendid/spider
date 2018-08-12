import urllib.request as Req
class HtmlDownloader(object):
    def download(self, root_url):
        if root_url is None:
            return
        response = Req.urlopen(root_url)
        if response.getcode()!=200:
        	return None
        return response.read()
