import re

log = []
numEvents = 0
line = []

with open("eventlog.txt") as file:
	lines = file.read()
	eventsList = re.findall("(Event\[)[0-9]+(\])", lines)
	numEvents = len(eventsList)
	print(numEvents)
	print(type(lines))
	
with open("eventlog.txt") as file:
	eventCount = 0
	while eventCount < numEvents:
		line = file.readline().strip()
		eventsFound = re.findall("(Event\[)[0-9]+(\])", line) 
		print(eventsFound)
		print(line)
		isBeginning = len(eventsFound) == 1
		if (isBeginning):
			eventCount+= 1
		# print(isBeginning)
		# print(line)

	# for line in file:
		#stripped_line = line.rstrip()
		# log.append(stripped_line)
	#for line in log:
		# print(line)
		# print(line)
		# print("---------------------------")