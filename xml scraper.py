import os
from bs4 import BeautifulSoup
import pandas as pd

os.chdir("C:/Users/BABU YOGESH K/Desktop/Assignment")
items=os.listdir(".")

newlist = []
for names in items:
     if names.endswith(".xml"):
         newlist.append(names)
print (newlist)

# print(os.getcwd())
for i in range(0,len(newlist)):
	infile = open(newlist[i],"r")
	contents = infile.read()
	soup = BeautifulSoup(contents,'xml')
	customer = soup.find('customer')
	customer_data=customer.text.split(">")
	# customer_data=customer.text
	print(customer_data)
	bill = soup.find('billnumber')
	data={'Customer':[customer_data],'Bill Number':[bill.text]}
	k=pd.DataFrame(data)
	k.to_csv('mycsv2.csv',mode='a',index=False,header=False)
