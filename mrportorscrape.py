import requests
import urllib.request
#import pandas as pd
from bs4 import BeautifulSoup

def Scrape(soup):
	designer,product,price = ([] for i in range(3))

	for link in soup.find_all("span", class_="product-designer"):
		designer.append(link.get_text())

	for link in soup.find_all("span", class_="product-title"):
		product.append(link.get_text().rstrip())
	for link in soup.find_all("div", class_="price-container"):
		pricebreak = link.get_text().splitlines()
		if len(pricebreak) > 2: # is sale item
			add = pricebreak[4].strip()
		else:
			add = pricebreak[1]
		price.append(add)

	if (len(designer) != len(product) != len(price)):
		print("There is something w rong with the scraping.")
		return null 

	output = []
	for x in range(len(designer)):
		tupl = designer[x],product[x],price[x]
		output.append(tupl)
	
	return output
	

def main():
	request = urllib.request.urlopen('https://www.mrporter.com/mens/search?keywords=blue+oxford+shirt').read()
	# print(request.info())
	soup = BeautifulSoup(request, "html.parser")
	shirts = Scrape(soup)
	print(shirts)

	request = urllib.request.urlopen('https://www.mrporter.com/en-gb/').read()
	#get headers / cookies
	#then request the page? le


if __name__ == '__main__':
   main()


