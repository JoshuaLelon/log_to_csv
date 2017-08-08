import re
import json
import csv
import events

eventsListFileName = "eventlog.txt"
log = []
numEvents = events.getNumEvents(eventsListFileName)
	
with open(eventsListFileName) as file:
	eventCount = 0
	eventAttributeDictionary = {
		'Log Name': 2,
		'Source': 1, 
		'Date': 1,
		'Event ID': 2,
		'Task': 1,
		'Level': 1,
		'Opcode': 1,
		'Keyword': 1,
		'User': 1,
		'User Name': 2,
		'Computer': 1
		}
		
	while eventCount < numEvents:
		line = file.readline().strip()
		eventsFound = re.findall("(Event\[)[0-9]+(\])", line)
		isBeginning = len(eventsFound) == 1 # if this line is the start of an event
		if (isBeginning): # then parse it
			event = {}
			eventCount+= 1
			eventNumberArray = re.findall("[0-9]+", line)
			eventNumber = int(eventNumberArray[0])
			event['Number'] = eventNumber
			for key, value in eventAttributeDictionary.items(): # this assumes it loops through the dict in the order the dict is initialized with
				line = file.readline().strip()
				wordArray = line.split()
				event[key] = wordArray[value]
			
			line = file.readline()
			line = file.readline().strip()
			event['Description'] = line
			
			log.append(event)
		
with open('result.json', 'w') as fp:
    json.dump(log, fp)
