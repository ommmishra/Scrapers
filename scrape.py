from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
# from googlesearch import serch
import requests
import csv

def soupReturn(URL):
	header = {'User-Agent': 'Mozilla/5.0'}
	req = Request(URL, headers = header)
	page = urlopen(req)
	soup = BeautifulSoup(page, 'html.parser')
	return soup

def cityTopicBio(URL):
	soup = soupReturn(URL)
	location = soup.find('div', attrs={'id':'date'})
	locationCity = location.text.strip().split(',')
	locationCity = locationCity[len(locationCity) - 1].strip(" ")
	bio = soup.find('div', attrs={'class':'sbio-text'})
	bio = bio.text
	bio = bio.split('\n')
	topic = soup.find('div', attrs={'class':'sd_speaker-agenda'})
	topic = topic.h3.text
	return locationCity, bio[1], topic

def locCountry(co):
	url = "https://serpapi.com/locations.json"
	PARAMS = {'q':co}
	r = requests.get(url = url, params = PARAMS)
	data = r.json()
	d = data[0]['canonical_name']
	d = d.split(',')
	d = d[len(d)-1]
	return d
# def searchResults(name,designation,company):
def writeAll()
	with open('speakers.csv', 'a') as csvFile:
		writer = csv.writer(csvFile)

URL = "https://www.ai-expo.net/europe/speakers/"
soup = soupReturn(URL)
about = soup.find('div', attrs={'class':'speaker_list speaker_list_wrap'})
for x in about.findAll('div',attrs={"speaker-expand clearfix"}):
	link = x.a['href']
	imgsrc = x.img['src']
	details = x.find('div', attrs={'class':'speaker-key-details-expand'})
	details = details.text.strip().split('\n')
	name = details[0]
	designation = details[1]
	try:
		company = details[2]
	except Exception as e:
		company = 'Problem Fetching'
	try:	
		locationCity, bio, topic = cityTopicBio(link)
	except Exception as e:
		topic = 'Problem Fetching'
	Country = locCountry(locationCity)
	z = [topic,name,imgsrc,designation,company,bio,locationCity,Country]
	