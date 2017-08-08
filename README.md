# log_to_csv
This is a script I use to parse my windows event log file into a csv / excel readable format for data analysis.

To run it, using the command prompt, clone the project, navigate to the project directory, and then run the following command:

python create_log.py

That should run the windows command to create your event log file.

After the event log file is created, move it into the project directory you just cloned, and run: 

python logToCSV.py

This will create both a JSON and CSV file with all of the data neatly parsed.

I designed this to use on Windows 10, but I think it'll work on 8 and possibly 7. The python definitely will (since it depends on having python installed, regardless of OS), I'm just hesistant about create_log.py - I haven't tested it.

Future Iterations may include:
- logic to store ALL of the description for a given event, instead of just the first line of each event from the eventlog.txt file.
- glue code to create the log in the same directory as the project to prevent the user from having to move it manually. Kind of a drag, but not worth trying to code it so far.
- further refactoring / revision of the code. It could be modularized a bit more, but it's readable to me after not having looked at it for a week, which works well enough.