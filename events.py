import re

def getNumEvents(eventsListFileName):
	with open(eventsListFileName) as file:
		lines = file.read()
		eventsList = re.findall("(Event\[)[0-9]+(\])", lines)
		return len(eventsList)