# Web Scraping
 - These are a few of my pet scraping projects
 - Must Install `urlib.request`, `Beautiful Soup`, 'twilio' to work, which can be done via a combination of HomeBrew/pip

### MrPorterWebScrape
Gets prices of blue oxford tshirts (however, can modify search for anything on website)


### Stockx Alert 
Sends text messages (must have Twilio account for this to work) or can just print output in terminal when price of shoes on stockx drops below a inputted threshold. This is useful to jump on those pair of kicks you have always been trying to find at a reasonable price. 

- To run in background run `python3 stockxaler.py &` 

- make sure to include country code in front of phone numbers for twilio pass 
