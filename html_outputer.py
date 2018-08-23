class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)
        pass
    def output_txt(self):
        fo = open('output_txt','wb+')
        for data in self.datas:
            fo.write(data['url'])
            fo.write(data['title'].encode('utf-8'))
            fo.write(data['summary'].encode('utf-8'))
        fo.close()

    def output_html(self):
        fout = open('output.html','w')

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"%data['url'])
            fout.write("<td>%s</td>"%data['title'].encode('utf-8'))
            fout.write("<td>%s</td>"%data['summary'].encode('utf-8'))
            print(data['summary'])
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        return  fout

