import csv

FILE_NAME = 'fdic_failed_bank_list.csv'

def open_csv(file_name):
	csv_file = open(file_name, 'rb')

	csv_data = csv.reader(csv_file)

	csv_file.close()


def count_csv_rows(file_name):
	number_of_rows = sum(1 for line in open(file_name))
	print number_of_rows

def output_rows_from(file_name):
	csv_file = open(file_name, 'rb')
	csv_data = csv.reader(csv_file)

	for row in csv_data:
		print type(row)
		print len(row)
		print row

	csv_file.close

def output_first_csv_row(file_name):
	csv_file = open(file_name, 'rb')
	csv_data = csv.reader(csv_file)
	
	header_row = csv_data.next()
	print header_row
	
	header_length = len(header_row)
	print header_length

	header_type = type(header_row)
	print header_row

	for column_name in header_row:
		print column_name

		column_name_length = len(column_name)
		print column_name_length

		column_name_type = type(column_name)
		print column_name_type

	csv_file.close()

def working_with_strings(file_name):
	csv_file = open(file_name, 'rb')
	csv_data = csv.reader(csv_file)
	header_row = csv_data.next()

	print header_row

	print header_row[4]

	print type(header_row[4])

	print len(header_row[4])

	my_string = header_row[4]

	print my_string[2]

	print my_string[:5]

	print my_string[5:]

	print my_string.capitalize()

	print my_string.lower()

	print my_string.upper()

	csv_file.close()

def doing_more_with_strings(file_name):
	csv_file = open(file_name, 'rb')
	csv_data = csv.reader(csv_file)
	header_row = csv_data.next()
	print header_row

	my_string = header_row[4]

	print my_string.upper() == my_string.lower()

	print my_string.replace(' ','')

	print my_string.replace(' ', '_')

	print my_string.strip('Acquiring').strip()

	print my_string.split(' ')

	my_split_string = my_string.split(' ')

	print type(my_split_string)

	print my_split_string[0]

	print 'I made %d strings from a list I created.  They are: %s & %s' % (len(my_split_string), my_split_string[0].lower(), my_split_string[1].lower())
	
	csv_file.close()





#open_csv(FILE_NAME)
#count_csv_rows(FILE_NAME)
#output_rows_from(FILE_NAME)
#output_first_csv_row(FILE_NAME)
working_with_strings(FILE_NAME)
doing_more_with_strings(FILE_NAME)