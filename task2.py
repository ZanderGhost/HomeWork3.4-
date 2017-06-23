import osa
import re

URL = 'http://www.webservicex.net/length.asmx?WSDL'

def read_file(file_name):
	with open(file_name, 'r') as f:
		return [item.split() for item in f.read().split('\n')]


def length_convert(length):
	client = osa.client.Client(URL)

	return client.service.ChangeLengthUnit(LengthValue=length, 
											fromLengthUnit='Miles', toLengthUnit='Kilometers')


def main():
#	file_path = input('Введите путь к файлу: ')
#	list_data = read_file(file_path)
#	sum_length = 0
	print(length_convert(100.23))
#	for item in list_data:
#		sum_length = sum_length + length_convert(re.sub(r',', '', item[1]))
#		print(sum_length)
#	print(sum_length)


main()
