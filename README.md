# metalpriceapi

metalpriceapi is the official Python wrapper for MetalpriceAPI.com. This allows you to quickly integrate our metal price API and foreign exchange rate API into your application. Check https://metalpriceapi.com documentation for more information.

## Installation

Install the latest release with:


    pip install metalpriceapi

## Usage

```python
from metalpriceapi.client import Client

api_key = 'SET_YOUR_API_KEY_HERE'
client = Client(api_key)
```
---
## Documentation

#### fetchSymbols()
```python
client.fetchSymbols()
```

[Link](https://metalpriceapi.com/documentation#api_symbol)

---
#### fetchLive(base, currencies)

- `base` <[string]> Optional. Pass in a base currency, defaults to USD.
- `currencies` <[List]<[string]>> Optional. Pass in an list of currencies to return values for.

```python
client.fetchLive(base='USD', currencies=['XAU', 'XAG', 'XPD', 'XPT'])
```

[Link](https://metalpriceapi.com/documentation#api_realtime)

---
#### fetchHistorical(date, base, currencies)

- `date` <[string]> Required. Pass in a string with format `YYYY-MM-DD`
- `base` <[string]> Optional. Pass in a base currency, defaults to USD.
- `currencies` <[List]<[string]>> Optional. Pass in an list of currencies to return values for.

```python
client.fetchHistorical(date='2024-02-05', base='USD', currencies=['XAU', 'XAG', 'XPD', 'XPT'])
```

[Link](https://metalpriceapi.com/documentation#api_historical)

---
#### fetchOHLC(base, currency, date, unit, dateType)

- `base` <[string]> Optional. Pass in a base currency, defaults to USD.
- `currency` <[string]> Required. Specify currency you would like to get OHLC for.
- `date` <[string]> Required. Specify date to get OHLC for specific date using format `YYYY-MM-DD`.
- `unit` <[string]> Optional. Pass in a unit, defaults to troy_oz.
- `dateType` <[string]> Optional. Pass in a date type, overrides date parameter if passed in.

```python
client.fetchOHLC(base='USD', currency='XAU', date='2024-02-05', unit='troy_oz', dateType=None)
```

[Link](https://metalpriceapi.com/documentation#api_ohlc)

---
#### convert(from_currency, to_currency, amount, date)

- `from_currency` <[string]> Optional. Pass in a base currency, defaults to USD.
- `to_currency` <[string]> Required. Specify currency you would like to convert to.
- `amount` <[number]> Required. The amount to convert.
- `date` <[string]> Optional. Specify date to use historical midpoint value for conversion with format `YYYY-MM-DD`. Otherwise, it will use live exchange rate date if value not passed in.

```python
client.convert(from_currency='USD', to_currency='EUR', amount=100, date='2024-02-05')
```

[Link](https://metalpriceapi.com/documentation#api_convert)

---
#### timeframe(start_date, end_date, base, currencies)

- `start_date` <[string]> Required. Specify the start date of your timeframe using the format `YYYY-MM-DD`.
- `end_date` <[string]> Required. Specify the end date of your timeframe using the format `YYYY-MM-DD`.
- `base` <[string]> Optional. Pass in a base currency, defaults to USD.
- `currencies` <[List]<[string]>> Optional. Pass in an list of currencies to return values for.

```python
client.timeframe(start_date='2024-02-05', end_date='2024-02-06', base='USD', currencies=['XAU', 'XAG', 'XPD', 'XPT'])
```

[Link](https://metalpriceapi.com/documentation#api_timeframe)

---
#### change(start_date, end_date, base, currencies)

- `start_date` <[string]> Required. Specify the start date of your timeframe using the format `YYYY-MM-DD`.
- `end_date` <[string]> Required. Specify the end date of your timeframe using the format `YYYY-MM-DD`.
- `base` <[string]> Optional. Pass in a base currency, defaults to USD.
- `currencies` <[List]<[string]>> Optional. Pass in an list of currencies to return values for.

```python
client.change(start_date='2024-02-05', end_date='2024-02-06', base='USD', currencies=['XAU', 'XAG', 'XPD', 'XPT'])
```

[Link](https://metalpriceapi.com/documentation#api_change)

---
#### carat(base, date)

- `base` <[string]> Optional. Pass in a base currency, defaults to USD.
- `date` <[string]> Optional. Specify date to get Carat for specific date using format `YYYY-MM-DD`. If not specified, uses live rates.

```python
client.carat(base='USD', date='2024-02-05')
```

[Link](https://metalpriceapi.com/documentation#api_carat)

---
#### usage()

```python
client.usage()
```

[Link](https://metalpriceapi.com/documentation#api_usage)

---
**[Official documentation](https://metalpriceapi.com/documentation)**

---
## FAQ

- How do I get an API Key?

    Free API Keys are available [here](https://metalpriceapi.com).

- I want more information

    Checkout our FAQs [here](https://metalpriceapi.com/faq).


## Support

For support, get in touch using [this form](https://metalpriceapi.com/contact).


[List]: https://www.w3schools.com/python/python_datatypes.asp 'List'
[number]: https://www.w3schools.com/python/python_datatypes.asp 'Number'
[string]: https://www.w3schools.com/python/python_datatypes.asp 'String'