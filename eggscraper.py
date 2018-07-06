from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url='https://www.newegg.com/global/in/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphics+card&ignorear=0&N=-1&isNodeId=1'

uClient=uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html,"html.parser")
#print(page_soup.h1)

containers=page_soup.findAll("div",{"class":"item-container"})
filename = "products.csv"
f= open(filename,"w")

headers = "brand,product_name\n"

f.write(headers)

for container in containers:
    #print(containers[0])
    try:
       brand=container.div.div.a.img["title"]
    except Exception as e:
       pass
    title_container=container.findAll("a",{"class":"item-title"})
    product_name = title_container[0].text
    price_container = container.findAll("li",{"class":"price-current"})
    price=price_container[0].text.strip()
    #print(brand)
    #print(product_name)
    f.write(brand + "," + product_name.replace(",","|") + "\n" ) 
	
f.close()