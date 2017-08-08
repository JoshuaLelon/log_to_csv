import os
os.popen("wevtutil qe System /f:text > \"%USERPROFILE%\Desktop\eventlog.txt\"") # this assumes you are on windows

# Once you've produced the above file, just put it in the project folder (wherever you cloned it)