s = u'你好世界'
s = s.encode('utf-8')
s = s.decode('utf-8','strict')
print(s)