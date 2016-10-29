from grab import Grab
import re, os, logging

DIR = os.path.abspath(os.curdir) + '/'
logging.basicConfig(level=logging.DEBUG)

def get_yandex_urls_by_page_num(query, page=0):
    try:
        g = Grab()
        g.proxylist.load_file(DIR + 'proxy.txt')
        #g.setup(proxy_auto_change=False)
        g.go('http://yandex.ru/yandsearch?p=%s&text=%s' % (page, query))
        #print(g.response.body)
        return [x.attr('href') for x in g.doc.select('//a[@class="link organic__url link link_cropped_no"]')]
    except:
        print('get_yandex_urls_by_page_num error')
        return []

def get_yandex_urls_by_sup(query, sup=1):
    try:
        urls = []
        for i in range(0, sup):
            urls += get_yandex_urls_by_page_num(query=query, page=i)
        return set(urls)
    except:
        print('get_yandex_urls_by_sup error')
        return ()

def get_email_by_url(url):
    try:
        g = Grab()
        g.go(url)
        return set(re.findall(r'\b[\w.-]+?@\w+?\.\w+?\b', str(g.response.body)))
    except:
        print('get_email_by_url error')
        return ()




if __name__ == "__main__":
    pass







