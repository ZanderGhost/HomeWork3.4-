import osa


URL = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'

def read_file(file_name):
	with open(file_name, 'r') as f:
		return [item.split() for item in f.read().split('\n')]


def temper_convert(amount_temper):
	client = osa.client.Client(URL)
	amount_currency = float(amount_temper)
	return client.service.ConvertTemp(Temperature=amount_currency, FromUnit='degreeFahrenheit', ToUnit='degreeCelsius')


def main():
	file_path = input('Введите путь к файлу: ')
	list_data = read_file(file_path)
	sum_temp = 0
	for item in list_data:
		sum_temp = sum_temp + temper_convert(item[0])
	average_temp = sum_temp / len(list_data)
	print(average_temp)


main()