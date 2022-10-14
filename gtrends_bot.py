from pytrends.request import TrendReq
import warnings
warnings.filterwarnings('ignore')

def main():
    print(f"Bot for scrapping data from Google Trends (Author: Ahmad Rizky)")
    pytrends = TrendReq(hl='en-US') #, tz=360, timeout=(10,25), proxies=proxies, retries=2, backoff_factor=0.1, requests_args={'verify':False})

    kw_word = input("Please input a keyword: ")
    kw_list = [kw_word]
    pytrends.build_payload(
        kw_list,
        cat=0,
        timeframe='today 5-y',
        geo='',
        gprop=''
    )
    dataframe = pytrends.interest_over_time()
    dataframe = dataframe.reset_index()
    dataframe.to_json('gtrends_{}.json'.format(kw_word))
    print(" (+) Success export data to json file.")

if __name__ == '__main__':
    main()
