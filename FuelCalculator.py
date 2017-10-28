import requests
import json
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup


""" This class will calculate fuel costs given miles traveled, and mpg """

class FuelCost:
	# def __init__(self):
	
	def getFuelCost(self, state):
		session = requests.Session()
		global r
		r = session.get("http://gasprices.aaa.com/", headers={'User-Agent': 'Mozilla/5.0'})

		global parser
		parser = MyHTMLParser()
		parser.feed(r.text)
		index = parser.data.find(state)
		return float(parser.data[index + len(state) + 2:index + len(state) + 7])

	def calculateFuelCost(self, state, distance, mpg):
		fuelCost = self.getFuelCost(state)
		return (distance/mpg) * fuelCost


class MyHTMLParser(HTMLParser):
	def handle_data(self, data):
		if "iwmparam[0].placestxt =" in data:
			self.data = data
