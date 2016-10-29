from grab import Grab
import logging, os

DIR = os.path.abspath(os.curdir) + '/'
logging.basicConfig(level=logging.DEBUG)



g = Grab()
g.proxylist.load_file(DIR + 'proxy.txt')
#g.setup(proxy_auto_change=False)
#g.proxylist.get_next_proxy()

def connect_test():
	try:
		g.go('http://yandex.ru/yandsearch?p=0&text=python')
		print(len(g.doc.select('//a[@class="link organic__url link link_cropped_no"]')))
		#print(g.response.body)
	except:
		print('error')
		return 'error'


count = 0

while count <= 3:
	connect_test()
	count += 1



