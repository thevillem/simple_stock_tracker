
import requests
import os
import datetime
import sys


class Stock:

    company_name = ''
    ticker = ''
    current = 0.00
    one_week = 0.00
    one_month = 0.00
    three_month = 0.00
    six_month = 0.00

    def set_company(self, name):
        self.company_name = name

    def get_company(self):
        return self.company_name

    def set_ticker(self, ticker):
        self.ticker = ticker

    def get_ticker(self):
        return self.ticker

    def set_current(self, current):
        self.current = current

    def get_current(self):
        return self.current

    def set_week(self, one_week):
        self.one_week = one_week

    def get_week(self):
        return self.one_week

    def set_month(self, one_month):
        self.one_month = one_month

    def get_month(self):
        return self.one_month

    def set_three_month(self, three_month):
        self.three_month = three_month

    def get_three_month(self):
        return self.three_month

    def set_six_month(self, six_month):
        self.six_month = six_month

    def get_six_month(self):
        return self.six_month


def get_stock_tickers():

    stocks = []

    stock = Stock()

    stock.company_name = 'Cisco Systems Inc'
    stock.ticker = 'CSCO'

    stocks.append(stock)

    return stocks


def get_stock_prices(stocks, api_key):

    for stock in stocks:

        try:
            results = requests.get('https://www.alphavantage.co/query?'
                        'function=TIME_SERIES_DAILY'
                        '&symbol=' + stock.ticker +
                        '&apikey=' + api_key)

            if results.status_code == 200:
                results = results.json()['Time Series (Daily)']
            else:
                print('Return code was: ' + str(results.status_code))
                sys.exit(1)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

        while True:
            i = 1
            while i < 5:
                yesterday = datetime.datetime.today() - datetime.timedelta(days=i)
                try:
                    stock.set_current(results[yesterday.strftime('%Y-%m-%d')]['4. close'])
                    i = 1
                    break

                except:
                    print('Seems like there is no stocks on ' + yesterday.strftime('%Y-%m-%d'))
                    i = i + 1

            while i < 5:
                one_week = datetime.datetime.today() - datetime.timedelta(days=i + 6)
                try:
                    stock.set_week(results[one_week.strftime('%Y-%m-%d')]['4. close'])
                    i = 1
                    break

                except:
                    print('Seems like there is no stocks on ' + one_week.strftime('%Y-%m-%d'))
                    i = i + 1

            while i < 5:
                one_month = datetime.datetime.today() - datetime.timedelta(days=i + 29)
                try:
                    stock.set_month(results[one_month.strftime('%Y-%m-%d')]['4. close'])
                    i = 1
                    break

                except:
                    print('Seems like there is no stocks on ' + one_month.strftime('%Y-%m-%d'))
                    i = i + 1

            while i < 5:
                three_month = datetime.datetime.today() - datetime.timedelta(days=i + 89)
                try:
                    stock.set_three_month(results[three_month.strftime('%Y-%m-%d')]['4. close'])
                    i = 1
                    break

                except:
                    print('Seems like there is no stocks on ' + three_month.strftime('%Y-%m-%d'))
                    i = i + 1


            ### Need to look for very last time of the list
            while i < 5:
                six_month = datetime.datetime.today() - datetime.timedelta(days=i + 179)
                try:
                    stock.set_six_month(results[six_month.strftime('%Y-%m-%d')]['4. close'])
                    i = 1
                    break

                except:
                    print('Seems like there is no stocks on ' + six_month.strftime('%Y-%m-%d'))
                    i = i + 1

            break


def get_api_key():

    if os.path.isfile('api.key'):
        f = open('api.key', 'r')
        api_key = f.readline()

        return str(api_key)
    else:
        print('File does not exist, exiting.')
        sys.exit(1)


def main():

    api_key = get_api_key()

    stocks = get_stock_tickers()

    get_stock_prices(stocks, api_key)

    for stock in stocks:
        print(stock.company_name)
        print(str(stock.get_current()))
        print(str(stock.get_week()))
        print(str(stock.get_month()))
        print(str(stock.get_three_month()))
        print(str(stock.get_six_month()))

if __name__ == '__main__':
    main()
