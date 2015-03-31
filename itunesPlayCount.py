import xml.etree.ElementTree as ET
import os, sys
from subprocess import call
import getopt

XML = "iTunes Music Library.xml"
WIN_PATH = "C:\\Users\\" + str(os.environ.get("USERNAME")) + "\\My Music\\iTunes\\" + XML
MAC_PATH =  os.path.expanduser("~/Music/iTunes/") + XML

def usage():
	print "One of the following is where your iTunes XML should originate:\n"
	print "  Mac OS X:	" + MAC_PATH
	print "  Windows:	" + WIN_PATH

try:
	opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
except getopt.GetoptError as err:
	print str(err)
	sys.exit(2)

for o, a in opts:
	if o in ("-h", "--help"):
		usage()
		sys.exit()

if sys.platform == "win32":
	path = WIN_PATH 
elif sys.platform == "darwin":
	path = MAC_PATH
else:
	print "Only Windows 7, Windows 8, and Mac OS X supported"
	sys.exit(1)

tree = ET.parse(path)

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
mon, d = divmod(d, 31)
year, mon = divmod(mon, 12)

year_string = "year"
mon_string = "month"
d_string = "day"
h_string = "hour"
m_string = "minute"
s_string = "second"

if year != 1:
	year_string += "s"

if mon != 1:
	mon_string += "s"

if d != 1:
	d_string += "s"

if h != 1:
	h_string += "s"

if m != 1:
	m_string += "s"

if s != 1:
	s_string += "s"

print "%d %s %d %s %d %s %d %s %02d %s %02d %s" % (year, year_string, mon, mon_string, d, d_string, h, h_string, m, m_string, s, s_string)

sys.exit(0)