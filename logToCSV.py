import events
import txt_to_py_list
import json_dump
import json_to_csv

eventListFileName = "eventlog.txt"
jsonResultsFileName = "results.json"
csvFileName = "results.csv"

numEvents = events.getNumEvents(eventListFileName)
eventList = txt_to_py_list.getPyListFromTxt(eventListFileName, numEvents)
json_dump.dumpListAsJSON(eventList, jsonResultsFileName)
json_to_csv.get_csv_from_JSON(jsonResultsFileName, csvFileName)