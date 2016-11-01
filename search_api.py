from grab import Grab
import re, os, logging


mail_regex = r'\b[\w.-]+?@\w+?\.\w+?\b'
phone_regex = r'\b[8-9]{0,2}[\-\(\)\d\s]{9,18}\b'


DIR = os.path.abspath(os.curdir) + '/'
logging.basicConfig(level=logging.DEBUG)


def get_yandex_urls_by_page_num(query, page=0):
    try:
        g = Grab()
        #g.proxylist.load_file(DIR + 'proxy.txt') #for proxy
        g.go('http://yandex.ru/yandsearch?p=%s&text=%s' % (page, query))
        #print(g.response.body)
        return [x.attr('href') for x in g.doc.select('//a[@class="link organic__url link link_cropped_no"]')]
    except:
        print('get_yandex_urls_by_page_num error', page)
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
        return set(re.findall(mail_regex, str(g.response.body)))
    except:
        print('get_email_by_url error')
        return ()

def get_phone_by_url(url):
    try:
        g = Grab()
        g.go(url)
        return set(re.findall(phone_regex, str(g.response.body)))
    except:
        print('get_phone_by_url error')
        return ()

def get_contacts(url):
    try:
        return list(get_email_by_url(url)) +  list(get_phone_by_url(url))
    except:
        print('get_contacts error')
        return ()




if __name__ == "__main__":
    pass







