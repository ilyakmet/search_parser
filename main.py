import search_api
import pandas as pd

query = 'строительные материалы киров'




if __name__ == "__main__":
    pd.Series({x:str(search_api.get_email_by_url(x)).strip('{}').replace("'", "") for x in search_api.get_yandex_urls_by_sup(query=query, sup=10)}).to_csv(query +'.csv')







