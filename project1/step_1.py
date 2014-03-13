import csv

FILE_NAME = 'fdic_failed_bank_list.csv'

def open_csv(file_name):
	csv_file = open(file_name, 'rb')

	csv_data = csv.reader(csv_file)

	print csv_data

	csv_file.close()