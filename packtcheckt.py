#!/usr/bin/python
import urllib2
import re
from sys import argv
import datetime


cachePath = "/tmp/packtchecktcache"
def getToday():
	now = datetime.datetime.now()
	return now.day

def isToday(dayToBeTested):
	today = getToday()
	return dayToBeTested == str(today)
	

def getBookNameFromCache():
	try: 
		f = open(cachePath, 'r')
		today, bookName = f.readlines()
		today = today.strip()
		bookName = bookName.strip()

		if (isToday(today)):
			return bookName
		else:
			return None
	except Exception:
		return None

		

def writeToCache(bookName):
	f = open(cachePath, 'w')
	
	day = getToday()

	f.write(str(day))
	f.write("\n")
	f.write(bookName)

	f.close()


bookName = getBookNameFromCache()

if not bookName:
	print("Retrieving the new book...")

	response = urllib2.urlopen('https://www.packtpub.com/packt/offers/free-learning')
	html = response.read()

	bookNameRegex = re.compile(ur'<div class="dotd-title">\s*<h2>\s*(.*)\s*<\/h2>\s*<\/div>')

	bookName = re.search(bookNameRegex, html).group(1)

	writeToCache(bookName)

print("The free book of the day is:")
print(bookName)
print("\nMore information at: https://www.packtpub.com/packt/offers/free-learning")



