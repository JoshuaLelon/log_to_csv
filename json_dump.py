import json

def dumpListAsJSON(list, jsonFileName):
	with open(jsonFileName, 'w') as fp:
		json.dump(list, fp)
