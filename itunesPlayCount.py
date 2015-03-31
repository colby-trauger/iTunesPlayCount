import xml.etree.ElementTree as ET
import os, sys
from subprocess import call

if sys.platform == "win32":
	path = "C:\\Users\\" + os.environ.get("USERNAME") + "\\My Music\\iTunes\\"
elif sys.platform == "darwin":
	path = os.path.expanduser("~/Music/iTunes/")
else:
	print "Only Windows 7, Windows 8, and Mac OS X supported"
	exit(1)

XML = "iTunes Music Library.xml"
path = path + XML

if os.path.isfile("./" + XML) == False:
	call(["ln", "-s", path, XML])

tree = ET.parse(XML)

songs = tree.find("dict/dict")

totalTime = 0

for song in songs:
	counter = 0
	time = 0
	playCount = 0

	for item in song:
		if item.text == "Play Count":
			playCount = song[counter + 1].text
			playCount = int(playCount)

		if item.text == "Total Time":
			time = song[counter + 1].text
			time = int(time) / 1000
		
		counter += 1

	totalTime += time * playCount

m, s = divmod(totalTime, 60)
h, m = divmod(m, 60)
d, h = divmod(h, 24)

print "%d days %d hours %02d minutes %02d seconds" % (d, h, m, s)

exit(0)