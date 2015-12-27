#!/usr/bin/python
import urllib2
import re


response = urllib2.urlopen('https://www.packtpub.com/packt/offers/free-learning')
html = response.read()

bookNameRegex = re.compile(ur'<div class="dotd-title">\s*<h2>\s*(.*)\s*<\/h2>\s*<\/div>')

bookName = re.search(bookNameRegex, html).group(1)

print("The free book of the day is:\n"+bookName+"\n\nMore information at: https://www.packtpub.com/packt/offers/free-learning")



