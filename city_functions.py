
class CityInfo():
	def __init__(self, city, country):
		self.city = city
		self.country = country
		
	def city_info(self):
		print(self.city + ", " + self.country)
		
my_city = CityInfo('Wantage', 'New Jersey')
my_city.city_info()