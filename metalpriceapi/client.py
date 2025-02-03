import requests

class Client(object):
    base_url = 'https://api.metalpriceapi.com/v1'

    def _removeEmpty(self, params):
        return {key:value for key,value in params.items() if value != ''}

    def __init__(self, api_key):
        self.client = requests.Session()
        self.client.params.update({'api_key': api_key})

    def fetchSymbols(self):
        response = self.client.get(f'{self.base_url}/symbols')
        return response.json()

    def fetchLive(self, base='', currencies=[]):
        params = self._removeEmpty({
            'base': base,
            'currencies': ','.join(currencies)
        })
        response = self.client.get(f'{self.base_url}/latest', params=params)
        return response.json()

    def fetchHistorical(self, date, base='', currencies=[]):
        params = self._removeEmpty({
            'base': base,
            'currencies': ','.join(currencies)
        })
        response = self.client.get(f'{self.base_url}/{date}', params=params)
        return response.json()

    def fetchOHLC(self, base='', currency='', date='', unit='', dateType=''):
        params = self._removeEmpty({
            'base': base,
            'currency': currency,
            'date': date,
            'unit': unit,
            'dateType': dateType
        })
        response = self.client.get(f'{self.base_url}/ohlc', params=params)
        return response.json()

    def convert(self, to_currency, amount, from_currency='', date=''):
        params = self._removeEmpty({
            'from': from_currency,
            'to': to_currency,
            'amount': amount,
            'date': date
        })
        response = self.client.get(f'{self.base_url}/convert', params=params)
        return response.json()

    def timeframe(self, start_date, end_date, base='', currencies=[]):
        params = self._removeEmpty({
            'start_date': start_date,
            'end_date': end_date,
            'base': base,
            'currencies': ','.join(currencies)
        })
        response = self.client.get(f'{self.base_url}/timeframe', params=params)
        return response.json()

    def change(self, start_date, end_date, base='', currencies=[]):
        params = self._removeEmpty({
            'start_date': start_date,
            'end_date': end_date,
            'base': base,
            'currencies': ','.join(currencies)
        })
        response = self.client.get(f'{self.base_url}/change', params=params)
        return response.json()

    def carat(self, base='', date = ''):
        params = self._removeEmpty({
            'base': base,
            'date': date,
        })
        response = self.client.get(f'{self.base_url}/carat', params=params)
        return response.json()

    def usage(self):
        response = self.client.get(f'{self.base_url}/usage')
        return response.json()
