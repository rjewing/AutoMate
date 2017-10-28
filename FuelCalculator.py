import requests
import json
from HTMLParser import HTMLParser


""" This class will calculate fuel costs given miles traveled, and mpg """

class FuelCost:
	def getFuelCost(self, state):
		session = requests.Session()
		r = session.get("http://gasprices.aaa.com/", headers={'User-Agent': 'Mozilla/5.0'})
		global parser
		parser = MyHTMLParser()
		parser.feed(r.text)
		index = parser.data.find(state)
		return float(parser.data[index + len(state) + 2:index + len(state) + 7])

	def calculateFuelCost(self, state, distance, mpg):
		fuelCost = self.getFuelCost(state)
		return (distance/mpg) * fuelCost


	def calculateFuelCostByMake(self, state, distance, make, model, year):
		session = requests.Session()
		r = session.get("https://apis.solarialabs.com/shine/v1/vehicle-stats/fuel-usage?make=" + make + "&car-truck=car&apikey=GSHwbZpUH4nB3LJEqqoSMtdyGyq4uD3A", headers={'User-Agent': 'Mozilla/5.0'})
		data = json.loads(r.text)
		for key in data:
			if model in key['Model']:
				print key
				print self.calculateFuelCost(state, distance, key['Hwy_Conventional_Fuel'])
		r = session.get("https://apis.solarialabs.com/shine/v1/vehicle-stats/fuel-usage?make=" + make + "&car-truck=truck&apikey=GSHwbZpUH4nB3LJEqqoSMtdyGyq4uD3A", headers={'User-Agent': 'Mozilla/5.0'})
		data = json.loads(r.text)
		for key in data:
			if model in key['Model']:
				print key
				print self.calculateFuelCost(state, distance, key['Hwy_Conventional_Fuel'])

class MyHTMLParser(HTMLParser):
	def handle_data(self, data):
		if "iwmparam[0].placestxt =" in data:
			self.data = data
