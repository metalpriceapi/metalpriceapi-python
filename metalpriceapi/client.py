import requests

class Client(object):
    SERVERS = {
        'us': 'https://api.metalpriceapi.com/v1',
        'eu': 'https://api-eu.metalpriceapi.com/v1',
    }

    def _removeEmpty(self, params):
        return {key: value for key, value in params.items() if value is not None and value != ''}

    def __init__(self, api_key, server='us'):
        self.base_url = self.SERVERS.get(server, self.SERVERS['us'])
        self.client = requests.Session()
        self.client.params.update({'api_key': api_key})

    def setServer(self, server):
        self.base_url = self.SERVERS.get(server, self.SERVERS['us'])

    def fetchSymbols(self):
        response = self.client.get(f'{self.base_url}/symbols')
        return response.json()

    def fetchLive(self, base='', currencies=None, unit='', purity='', math=''):
        params = self._removeEmpty({
            'base': base,
            'currencies': ','.join(currencies or []),
            'unit': unit,
            'purity': purity,
            'math': math,
        })
        response = self.client.get(f'{self.base_url}/latest', params=params)
        return response.json()

    def fetchHistorical(self, date, base='', currencies=None, unit=''):
        params = self._removeEmpty({
            'base': base,
            'currencies': ','.join(currencies or []),
            'unit': unit,
        })
        response = self.client.get(f'{self.base_url}/{date}', params=params)
        return response.json()

    def hourly(self, base='', currency='', unit='', start_date='', end_date='', math='', date_type=''):
        params = self._removeEmpty({
            'base': base,
            'currency': currency,
            'unit': unit,
            'start_date': start_date,
            'end_date': end_date,
            'math': math,
            'date_type': date_type,
        })
        response = self.client.get(f'{self.base_url}/hourly', params=params)
        return response.json()

    def fetchOHLC(self, base='', currency='', date='', unit='', date_type=''):
        params = self._removeEmpty({
            'base': base,
            'currency': currency,
            'date': date,
            'unit': unit,
            'date_type': date_type,
        })
        response = self.client.get(f'{self.base_url}/ohlc', params=params)
        return response.json()

    def convert(self, from_currency='', to_currency='', amount='', date='', unit=''):
        params = self._removeEmpty({
            'from': from_currency,
            'to': to_currency,
            'amount': amount,
            'date': date,
            'unit': unit,
        })
        response = self.client.get(f'{self.base_url}/convert', params=params)
        return response.json()

    def timeframe(self, start_date, end_date, base='', currencies=None, unit=''):
        params = self._removeEmpty({
            'start_date': start_date,
            'end_date': end_date,
            'base': base,
            'currencies': ','.join(currencies or []),
            'unit': unit,
        })
        response = self.client.get(f'{self.base_url}/timeframe', params=params)
        return response.json()

    def change(self, start_date, end_date, base='', currencies=None, date_type=''):
        params = self._removeEmpty({
            'start_date': start_date,
            'end_date': end_date,
            'base': base,
            'currencies': ','.join(currencies or []),
            'date_type': date_type,
        })
        response = self.client.get(f'{self.base_url}/change', params=params)
        return response.json()

    def carat(self, base='', currency='', date=''):
        params = self._removeEmpty({
            'base': base,
            'currency': currency,
            'date': date,
        })
        response = self.client.get(f'{self.base_url}/carat', params=params)
        return response.json()

    def usage(self):
        response = self.client.get(f'{self.base_url}/usage')
        return response.json()
