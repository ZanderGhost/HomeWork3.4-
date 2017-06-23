import osa


URL = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'

def read_file(file_name):
	with open(file_name, 'r') as f:
		return [item.split() for item in f.read().split('\n')]


def currency_convert(from_currency, amount_currency):
	client = osa.client.Client(URL)
	amount_currency = float(amount_currency)
	return client.service.ConvertToNum(toCurrency='RUB', fromCurrency=from_currency,
											amount=amount_currency, rounding=True)


def main():
	file_path = input('Введите путь к файлу: ')
	list_data = read_file(file_path)
	sum_rub = 0
	for item in list_data:
		sum_rub = sum_rub + currency_convert(item[-1], item[-2])
	print(sum_rub)


main()
###
#print(read_file('currencies.txt'))