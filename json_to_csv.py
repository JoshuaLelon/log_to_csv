import csv
import json

eventHeaders = {
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
				'Computer': 1,
				'Description': 1
}

def get_csv_from_JSON(jsonFileName, csvFileName):
	with open(jsonFileName) as json_file:
		eventsJSON = json.load(json_file)
		f = csv.writer(open(csvFileName, "w"), delimiter=',', lineterminator='\n')
		f.writerow([key for key, value in eventHeaders.items()])
		
		for event in eventsJSON:
			f.writerow([value for key, value in event.items()])

