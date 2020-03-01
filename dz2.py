from requests import get

class ResponseRefreshable():
	"""docstring for ResponseRefreshable"""
	def __init__(self, methodurl):
		response = get(methodurl)
		self.status = "successfully got info" if response.ok else "can't get data"
		self.response = response.json()

	def refresh_data(self):
		self.__init__()
		
class InfoResponse(ResponseRefreshable):
	'''
	decimal_places: количество разрешенных знаков после запятой
	min_price: минимальная разрешенная цена
	max_price: максимальная разрешенная цена
	min_amount: минимальное разрешенное количество для покупки или продажи
	hidden: пара скрыта (0 или 1)
	fee: комиссия пары
	'''
	def __init__(self):
		super().__init__("https://yobit.net/api/3/info")
		self.server_time = self.response["server_time"]
		self.pairs = self.response["pairs"]
		self.btc_list = self.pairs.keys()

class TickerResponse(ResponseRefreshable):
	'''
	high: макcимальная цена
	low: минимальная цена
	avg: средняя цена
	vol: объем торгов
	vol_cur: объем торгов в валюте
	last: цена последней сделки
	buy: цена покупки
	sell: цена продажи
	updated: последнее обновление кэша
	'''
	def __init__(self, btc):
		super().__init__(f"https://yobit.net/api/3/ticker/{btc}")
		self.btc_info = self.response[btc]


class DepthResponse(ResponseRefreshable):
	'''
	asks: ордера на продажу
	bids: ордера на покупку
	'''
	def __init__(self, btc):
		super().__init__(f"https://yobit.net/api/3/depth/{btc}")
		self.depth_btc_info = self.response[btc]

class TradesResponse(ResponseRefreshable):
	'''
	type: ask - продажа, bid - покупка
	price: цена покупки/продажи
	amount: количество
	tid: идентификатор сделки
	timestamp: unix time сделки
	'''
	def __init__(self, btc):
		super().__init__(f"https://yobit.net/api/3/trades/{btc}")
		self.trades_btc_info = self.response[btc]


def YobitApiFabric(method, btc="type btc to check (if neccessary)"):
		if btc=="type btc to check (if neccessary)":
			has_btc = False
		else:
			has_btc = True

		if method == "info":
			return InfoResponse()

		if has_btc:
			if method == "ticker":
				return TickerResponse(btc)
			if method == "depth":
				return DepthResponse(btc)
			if method == "trades":
				return TradesResponse(btc)
		else:
			raise Exception("please, provide btc currency")

		raise Exception("unknown method")

# infoobj = YobitApiFabric("info")
# print(infoobj.__doc__)
# print(infoobj.server_time, infoobj.pairs, infoobj.btc_list)

# tickerobj = YobitApiFabric("ticker", "ltc_btc")
# print(tickerobj.__doc__)
# print(tickerobj.btc_info)

# depthobj = YobitApiFabric("depth", "ltc_btc")
# print(depthobj.__doc__)
# print(depthobj.depth_btc_info)

# tradesobj = YobitApiFabric("trades", "ltc_btc")
# print(tradesobj.__doc__)
# print(tradesobj.trades_btc_info)