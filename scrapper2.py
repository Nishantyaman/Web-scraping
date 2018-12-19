from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
# import csv

# source = requests.get("http://solarelectricityhandbook.com/solar-irradiance.html").text

# soup=BeautifulSoup(source,'lxml')

# print (soup)

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def func2():
	# WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//select[@id='city']")))
	while True:
		try:
			select_box2 = driver.find_element_by_name("city") 
			time.sleep(2)
			options2 = [x for x in select_box2.find_elements_by_tag_name("option")]
			for element in options2[1:]:
				driver.set_page_load_timeout(30)
				WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//select[@id='city']")))
				value=element.text
				print (value)
				obj2=Select(select_box2)
				obj2.select_by_visible_text(value)
				
				# dropdown=driver.find_element_by_xpath("//*[@id='country']")
				# select = Select(dropdown)
				# select.select_by_value(value).click()
				time.sleep(2)
				obj3=Select(driver.find_element_by_name('ddlDirection'))
				obj3.select_by_value('Facing directly South')
		except Exception as e:
			print (e)
			break
	# options2 = [x for x in select_box2.find_elements_by_tag_name("option")]
	# for element in options2:
	# 	value=element.text
	# 	# dropdown=driver.find_element_by_xpath("//*[@id='country']")
	# 	# select = Select(dropdown)
	# 	# select.select_by_value(value).click()
	# 	obj3=Select(driver.find_element_by_name('ddlDirection'))
	# 	obj3.select_by_value('Facing directly South')


driver = webdriver.Chrome("C:\\Users\\BABU YOGESH K\\Downloads\\chromedriver_win32\\chromedriver.exe")


driver.get("http://solarelectricityhandbook.com/solar-irradiance.aspx")
driver.set_page_load_timeout(30)


select_box = driver.find_element_by_name("country") 
# a=driver.find_element_by_id('#country > option:nth-child(1)')
options = [x for x in select_box.find_elements_by_tag_name("option")]
for element in options[1:]:
	value=element.text
	print(value)
	driver.set_page_load_timeout(100)
	WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "country")))
	# dropdown=driver.find_element_by_xpath("//*[@id='country']")
	# select = Select(dropdown)
	# select.select_by_value(value).click()
	obj=Select(select_box)
	obj.select_by_value(value)

	driver.set_page_load_timeout(50)

	# source = requests.get("http://solarelectricityhandbook.com/solar-irradiance.html").text
	# print(source)

	# soup=BeautifulSoup(source,'lxml')

	# a=soup.find("select", {"name":"city"})
	time.sleep(1)
	func2()
	# driver.set_page_load_timeout(1000)

	# driver.get("http://solarelectricityhandbook.com/solar-irradiance.aspx")

	# wait = WebDriverWait(driver, 5)



driver.set_page_load_timeout(20)

driver.find_element_by_xpath("//select[@id='city']/option[@value='Berat']").click()

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
j=4;
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