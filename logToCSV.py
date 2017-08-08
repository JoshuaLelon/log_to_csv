import re
import json
import csv
import events
import txt_to_py_list
import json_dump

eventListFileName = "eventlog.txt"
jsonResultsFileName = "results.json"
numEvents = events.getNumEvents(eventListFileName)
eventList = txt_to_py_list.getPyListFromTxt(eventListFileName, numEvents)
json_dump.dumpListAsJSON(eventList, jsonResultsFileName)