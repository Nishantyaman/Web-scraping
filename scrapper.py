from bs4 import BeautifulSoup
import requests
import pandas as pd
# import csv

# source = requests.get("http://solarelectricityhandbook.com/solar-irradiance.html").text

# soup=BeautifulSoup(source,'lxml')

# print (soup)

from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("C:\\Users\\BABU YOGESH K\\Downloads\\chromedriver_win32\\chromedriver.exe")


driver.get("http://solarelectricityhandbook.com/solar-irradiance.aspx")
driver.set_page_load_timeout(30)



# a=driver.find_element_by_id('#country > option:nth-child(1)')
driver.find_element_by_xpath("//select[@id='country']/option[@value='Afghanistan']").click()

driver.set_page_load_timeout(20)

try:
	driver.find_element_by_xpath("//select[@id='state']/option[@value='Alabama']").click()

	driver.set_page_load_timeout(20)
	j=5;

except Exception as e:
	j=4;
	pass

driver.find_element_by_xpath("//select[@id='city']/option[@value='Ghazni']").click()

driver.set_page_load_timeout(20)

driver.find_element_by_xpath("//select[@id='ddlDirection']/option[@value='Facing directly South']").click()

driver.set_page_load_timeout(5000)

# username = driver.find_element_by_xpath('.//span[@id="lblJan"]').text
# //*[@id="lblJan"]

# print(username)

a=["1b1Jan","1b1Feb","1b1Mar","1b1Apr","1b1May","1b1Jun","1b1Jul","1b1Aug","1b1Sep","1b1Oct","1b1Nov","1b1Dec"]
# source = requests.get("http://solarelectricityhandbook.com/solar-irradiance.aspx").text

# for i in a:
	# k = './/span[@id='+i+']'
username = driver.find_elements_by_xpath('.//span[starts-with(@id,"lbl")]')

values=[]
for i in username:
	values.append(i.text)
	# print(i.text)
# print(values)
# j=4;
d={}
for i in a:
	d[i]=values[j]
	j+=1

print(d)

# df = pd.DataFrame(data=d)
# driver.set_page_load_timeout(500)

# soup=BeautifulSoup(source,'lxml')

# a=soup.find("id:"1b1Jan")

# driver.set_page_load_timeout(50)

# span1 = soup.find("span", id="1b1Jan")

# print(source)



#country


#country > option:nth-child(1)	
driver.maximize_window()

driver.quit()