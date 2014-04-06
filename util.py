import csv, datetime, json, math, pickle, urllib
import bellman

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
	return lines[1:]

def getTimeDiff(dateOne, dateTwo):
	c = dateTwo - dateOne
	minutes, sec = divmod(c.days * 86400 + c.seconds, 60)
	return minutes

def findCycles(source='USD'):
  # Open file to check time of last data entry
  lines = open('time.txt', 'rw').readlines()
  print lines
  oldDate = datetime.datetime.strptime(lines[0], "%Y-%m-%d %H:%M:%S")
  currDate = datetime.datetime.now()
  timeDiff = getTimeDiff(oldDate, currDate)
  print timeDiff

  # Create adjacency matrix
  codeList = getCurrencyCodes()
  currAdjMatrix = {code: {code: None for code in codeList} for code in codeList}

  if timeDiff > 60:
  	# Fill adjacency matrix with rates
  	for fromCode in codeList:
  		for toCode in codeList:
	  		url = 'http://rate-exchange.appspot.com/currency?from={}&to={}'.format(fromCode,toCode)
	  		f = urllib.urlopen(url).read()
	  		print f
	  		j = json.loads(f)
	  		currAdjMatrix[fromCode][toCode] = -math.log(j['rate']) if 'rate' in j else None

	# Write to file
	f = open('currencyRates.csv', 'w')
	pickle.dump(currAdjMatrix, f)
	f = open('time.txt', 'w')
	f.write(currDate.strftime("%Y-%m-%d %H:%M:%S"))

  else:
  	f = open('currencyRates.csv', 'r')
  	currAdjMatrix = pickle.load(f)
  	print currAdjMatrix

  # Run Bellman
  paths = bellman.bellman_ford(currAdjMatrix, source)

  # Calculate value of each cycle
  results = []
  for path in paths:
  	gain = 0

  	# Run cycle
  	for i in range(len(path)-1):
  		fromCurr = path[i]
  		toCurr = path[i+1]
  		gain += currAdjMatrix[fromCurr][toCurr]

  	gain = math.exp(-gain)
  	results.append((path, gain))

  results.sort(key=lambda x:x[1], reverse=True)
  return results

findCycles()
