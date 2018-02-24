from bs4 import BeautifulSoup
import sys
import urllib.request
import unicodedata
import datetime

ar_url = "https://wikileaks.org/clinton-emails/emailid/1149"

with urllib.request.urlopen(ar_url) as url:
	ar_html = url.read()
	ar_soup = BeautifulSoup(ar_html, 'html.parser')
	header = ar_soup.find("header").contents
	emailfrom = BeautifulSoup(str(header[1]), 'html.parser').find("span").contents[0]
	emailto = BeautifulSoup(str(header[3]), 'html.parser').find("span").contents[0]
	emaildatestring = header[4].split('\n\t\t\t\t\t')[1][6:]
	emaildate = datetime.datetime.strptime(emaildatestring[:10], '%Y-%m-%d').date()
	print(header)
	print("from:")
	print(emailfrom)
	print("to:")
	print(emailto)
	print(emaildate)