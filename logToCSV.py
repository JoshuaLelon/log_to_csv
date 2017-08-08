import re
import json
import csv
import events

eventsListFileName = "eventlog.txt"
log = []
numEvents = events.getNumEvents(eventsListFileName)
	
with open("eventlog.txt") as file:
	eventCount = 0
	while eventCount < numEvents:
		line = file.readline().strip()
		eventsFound = re.findall("(Event\[)[0-9]+(\])", line)
		isBeginning = len(eventsFound) == 1
		if (isBeginning):
			event = {}
			eventCount+= 1
			eventNumberArray = re.findall("[0-9]+", line)
			eventNumber = int(eventNumberArray[0])
			event['Number'] = eventNumber
			
			line = file.readline().strip()
			wordArray = line.split()
			event['Log Name'] = wordArray[2]
			
			line = file.readline().strip()
			wordArray = line.split()
			event['Source'] = wordArray[1]
			
			line = file.readline().strip()
			wordArray = line.split()
			event['Date'] = wordArray[1]
			
			line = file.readline().strip()
			wordArray = line.split()
			event['Event ID'] = wordArray[2]
			
			line = file.readline().strip()
			wordArray = line.split()
			event['Task'] = wordArray[1]
			
			line = file.readline().strip()
			wordArray = line.split()
			event['Level'] = wordArray[1]
			
			line = file.readline().strip()
			wordArray = line.split()
			event['Opcode'] = wordArray[1]
			
			line = file.readline().strip()
			wordArray = line.split()
			event['Keyword'] = wordArray[1]
			
			line = file.readline().strip()
			wordArray = line.split()
			event['User'] = wordArray[1]
			
			line = file.readline().strip()
			wordArray = line.split()
			event['User Name'] = wordArray[2]
			
			line = file.readline().strip()
			wordArray = line.split()
			event['Computer'] = wordArray[1]
			
			line = file.readline()
			line = file.readline().strip()
			event['Description'] = line
			
			log.append(event)
		# print(isBeginning)
		# print(line)
	# print(log)
	# for line in file:
		#stripped_line = line.rstrip()
		# log.append(stripped_line)
	#for line in log:
		# print(line)
		# print(line)
		# print("---------------------------")
		
with open('result.json', 'w') as fp:
    json.dump(log, fp)
