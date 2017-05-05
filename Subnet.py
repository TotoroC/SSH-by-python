import urllib2
from re import findall
w = open('VN.txt', 'w')
url = "http://lite.ip2location.com/myanmar-ip-address-ranges"
opens = urllib2.urlopen(url).read()
xuly = list(findall(r'[0-9]+(?:\.[0-9]+){3}',opens))
for i in xuly:
	if (xuly.index(i) % 2 != 0):       
		w.write(',' + i + '\n')
	else:
		w.write(i)
