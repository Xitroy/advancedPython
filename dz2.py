from requests import get

class InfoResponse():
	'''
	decimal_places: количество разрешенных знаков после запятой
	min_price: минимальная разрешенная цена
	max_price: максимальная разрешенная цена
	min_amount: минимальное разрешенное количество для покупки или продажи
	hidden: пара скрыта (0 или 1)
	fee: комиссия пары
	'''
	def __init__(self):
		response = get("https://yobit.net/api/3/info")
		self.status = "successfully got info" if response.ok else "can't get data"
		response = response.json()
		self.server_time = response["server_time"]
		self.pairs = response["pairs"]
		self.btc_list = self.pairs.keys()
		
	def refresh_data(self):
		self.__init__()

class TickerResponse():
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
		response = get(f"https://yobit.net/api/3/ticker/{btc}")
		self.status = "successfully got info" if response.ok else "can't get data"
		response = response.json()
		self.btc_info = response[btc]

	def refresh_data(self):
		self.__init__()

class DepthResponse():
	'''
	asks: ордера на продажу
	bids: ордера на покупку
	'''
	def __init__(self, btc):
		response = get(f"https://yobit.net/api/3/depth/{btc}")
		self.status = "successfully got info" if response.ok else "can't get data"
		response = response.json()
		self.depth_btc_info = response[btc]

	def refresh_data(self):
		self.__init__()

class TradesResponse():
	'''
	type: ask - продажа, bid - покупка
	price: цена покупки/продажи
	amount: количество
	tid: идентификатор сделки
	timestamp: unix time сделки
	'''
	def __init__(self, btc):
		response = get(f"https://yobit.net/api/3/trades/{btc}")
		self.status = "successfully got info" if response.ok else "can't get data"
		response = response.json()
		self.trades_btc_info = response[btc]

	def refresh_data(self):
		self.__init__()


ir = InfoResponse()
print(ir.status, ir.server_time, ir.pairs, ir.btc_list)
tr = TickerResponse("ltc_btc")
print(tr.status, tr.btc_info)
dr = DepthResponse("ltc_btc")
print(dr.status, dr.depth_btc_info)
tdr = TradesResponse("ltc_btc")
print(tdr.status, tdr.trades_btc_info)