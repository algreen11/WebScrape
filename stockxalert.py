import requests
import urllib.request
from bs4 import BeautifulSoup
from twilio.rest import Client
import time

account_sid = "TWILIO ACCOUNT SID"
auth_token = "TWILIO ACCOUNT AUTH TOKEN"
twilio_phone_number = 'TWILIO NUMBER'
user_phone = 'MY PHONE NUMBER'

shoe_url = 'https://stockx.com/adidas-yeezy-boost-350-pirate-black-2016'
size = 10
price_threshold = 1200
current_price = 1250
refresh_minutes = 60

def Scrape(soup):
	shoesize, price = ([] for i in range(2))
	for link in soup.find_all(class_='title'):
		shoesize.append(link.get_text())
	for link in soup.find_all(class_='subtitle'):
		price.append(link.get_text())

	shoe = shoesize[1:30]
	pri = price[1:30]
	dic = {}
	x = 0
	while x < len(shoe):
		dic[shoe[x]] = pri[x]
		x += 1
	return dic

def CheckPrice(price_dict):
	new = price_dict.get(str(size))
	new = int(new[1:])
	global current_price
	if new < current_price and new < price_threshold:
		current_price = new
		return True
	else: 
		current_price = new
		return False

def Text(message):
	client = Client(account_sid, auth_token)
	client.messages.create(to=user_phone, from_=twilio_phone_number, body=message)

def main():
	while True:
		request = urllib.request.urlopen(shoe_url).read()
		soup = BeautifulSoup(request, "html.parser")
		shoe_data = Scrape(soup)
		if CheckPrice(shoe_data):
			Text('The ' + shoe_url[19:] + ' have dropped below $' + str(price_threshold) + 
				'. They are now $' + str(current_price) + '. Check it out at ' + shoe_url)
			# print('The ' + shoe_url[19:] + ' have dropped below $' + str(price_threshold) + '. They are now $' + str(current_price) + '. Check it out at ' + shoe_url)
		time.sleep(60*refresh_minutes)

if __name__ == '__main__':
   main()