import search_api
import pandas as pd
from multiprocessing.dummy import Pool as ThreadPool


query = 'строительные материалы москва'
pages_count = 1 #number of search pages
pool_number = 5 #number of pools


def main(url):
	res = search_api.get_contacts(url)
	if (res != set()) and (res != ()):
		D[url] = str(res).strip("[]").replace("'", "").replace(' ', '')




if __name__ == "__main__":
    D = {} #all data
    pool = ThreadPool(pool_number)
    pool.map(main, search_api.get_yandex_urls_by_sup(query=query, sup=pages_count))
    pd.Series(D).to_csv(query.replace(' ', '_') +'.csv')




