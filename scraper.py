from bs4 import BeautifulSoup
import sys
import urllib.request
import unicodedata
import datetime
import csv
import pandas as pd
import time

badcount = 0
emails = []
df = pd.DataFrame(columns=["emaildate","otherhuman"])
##Current Schema: List of lists. Each email: [from,to,date]
##Better data scrctures? does a class make sense here??


#for i in range(33727):
for i in range(10000):
	ii = i + 1000
	time.sleep(2)
	ar_url = "https://wikileaks.org/clinton-emails/emailid/" + str(ii)
	print("querying " + ar_url)
	try:
		url = urllib.request.urlopen(ar_url)
		ar_html = url.read()
		ar_soup = BeautifulSoup(ar_html, 'html.parser')
		try:
			header = ar_soup.find("header").contents
			emailfrom = BeautifulSoup(str(header[1]), 'html.parser').find("span").contents[0]
			emailto = BeautifulSoup(str(header[3]), 'html.parser').find("span").contents[0]
			emaildatestring = header[4].split('\n\t\t\t\t\t')[1][6:]
			emaildate = datetime.datetime.strptime(emaildatestring[:10], '%Y-%m-%d').date()
			emails.append([emailfrom,emailto,emaildate])
			human = ""
			if emailfrom == "Hillary Clinton":
				human = emailto
			else:
				human = emailfrom
			#df = df.append([emaildate,human]);
			df.loc[len(df.index)] = [emaildate,human]
		except:
			badcount += 1
	except urllib.HTTPError:
		print("HTTPError")
		# print(header)
		# print("from:")
		# print(emailfrom)
		# print("to:")
		# print(emailto)
		# print(emaildate)

#setting the date as the index
df['dateindex'] = pd.to_datetime(df['emaildate'])
df = df.set_index('dateindex')
df = df.drop('emaildate', 1)

#getting the frequency 

dfvalcount = df.loc["2010-06-01":"2010-06-30"].otherhuman.value_counts()

# print("list:")
# print(emails)
# print("dataframe:")
print(df)
# print("value count:")
print(dfvalcount)


#write to csv
df.to_csv("wikileaksout2.csv")
dfvalcount.to_csv("wikivalout2.csv")
df.to_csv("bigout.csv")
# with open("wikileaksout.csv", 'w') as myfile:
#     wr = csv.writer(myfile)
#     wr.writerow(emails)