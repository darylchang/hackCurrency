import csv

def writeFile():
	# Open currency list and read in data
	f = open('raw.csv', 'r')
	lines = [line.strip('\n').split('\t') for line in f.readlines()]
	f.close()

	# Write to file
	f = open('currencyList.csv', 'w')
	for line in lines:
		line = ','.join(line)
		f.write(line + '\n')

	f.close()

def getCurrencyCodes():
	lines = [line.strip('\n').split(',') for line in open('currencyList.csv', 'r').readlines()]
	lines = [line[3] for line in lines]
	print lines[1:]
