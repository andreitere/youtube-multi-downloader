from sys import argv 
import os
import pafy
from threading import Thread

def threaded_dl(url):
	audio = pafy.new(line)
	print("Downloading %s" % audio.title)

	audio = audio.getbestaudio("m4a")
	audio.download("downloads/", True)



dirname = "downloads/"
try:
    os.makedirs(dirname)
except OSError:
    if os.path.exists(dirname):
        # We are nearly safe
        pass
    else:
        # There was an error on creation, so make sure we know about it
        raise
        

# read file
script, file = argv
print ("argv" % argv)
f = open(file, "r")
print ("File: %r:" % file)
i = 1;
for line in f:
	thread = Thread(target = threaded_dl, args = (line, ))
	thread.start()
