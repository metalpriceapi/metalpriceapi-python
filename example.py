from metalpriceapi.client import Client

api_key = 'REPLACE_ME'
client = Client(api_key)

result = client.fetchSymbols()
print(result)

result = client.fetchLive(base='USD', currencies=['XAU', 'XAG', 'XPD', 'XPT'])
print(result)

result = client.fetchHistorical(date='2024-02-05', base='USD', currencies=['XAU', 'XAG', 'XPD', 'XPT'])
print(result)

result = client.convert(from_currency='USD', to_currency='EUR', amount=100, date='2024-02-05')
print(result)

result = client.timeframe(start_date='2024-02-05', end_date='2024-02-06', base='USD', currencies=['XAU', 'XAG', 'XPD', 'XPT'])
print(result)

result = client.change(start_date='2024-02-05', end_date='2024-02-06', base='USD', currencies=['XAU', 'XAG', 'XPD', 'XPT'])
print(result)

result = client.carat(base='USD', date='2024-02-06')
print(result)
