from bs4 import BeautifulSoup
import sys
import urllib.request
import unicodedata
import datetime
import csv

badcount = 0
emails = []
##Current Schema: List of lists. Each email: [from,to,date]
##Better data scrctures? does a class make sense here??


#for i in range(33727):
for i in range(10):

	ar_url = "https://wikileaks.org/clinton-emails/emailid/" + str(i)

	with urllib.request.urlopen(ar_url) as url:
		ar_html = url.read()
		ar_soup = BeautifulSoup(ar_html, 'html.parser')
		try:
			header = ar_soup.find("header").contents
			emailfrom = BeautifulSoup(str(header[1]), 'html.parser').find("span").contents[0]
			emailto = BeautifulSoup(str(header[3]), 'html.parser').find("span").contents[0]
			emaildatestring = header[4].split('\n\t\t\t\t\t')[1][6:]
			emaildate = datetime.datetime.strptime(emaildatestring[:10], '%Y-%m-%d').date()
			emails.append([emailfrom,emailto,emaildate])
		except:
			badcount += 1
		# print(header)
		# print("from:")
		# print(emailfrom)
		# print("to:")
		# print(emailto)
		# print(emaildate)
print("writing")
print(emails)
with open("wikileaksout.csv", 'w') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(emails)