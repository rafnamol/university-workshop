#print ('give me fuel, give me fire')
import requests
import feedparser
from pprint import pprint

response = requests.get ('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?')
feed = feedparser.parse(response.content)
print(feed)
pprint(feed, indent=4)
def get_fuel(product_id):
    data = feedparser.parse('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product='+str(product_id)+'&Suburb=Cloverdale')
    return data['entries']
    
#r = requests.get ('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?')
#print ('give me fuel, give me fire')


exit()

