input_truck_ranges = [(1900, 1950),
		 (1910, 1940),
		 (1905, 1960),
		 (1960, 1980)]

class TruckStatsFinder():
	def __init__(self, input_truck_ranges):
		self.input_truck_ranges = input_truck_ranges

		self.min_starting_year = input_truck_ranges[0][0] + 1
		self.max_starting_year = input_truck_ranges[0][1] + 1

		self.count_trucks_by_year = {}

		self.config_min_trucks = []
		self.config_max_trucks = []

	def find_min_truck_starting_year(self, year, current_min):
		if year < current_min:
			return year
		else:
			return current_min

	def find_max_truck_starting_year(self, year, current_max):
		if year > current_max:
			return year
		else:
			return current_max

	def find_minmax_of_ranges(self, input_truck_ranges):
		for year in input_truck_ranges:
			self.min_starting_year = self.find_min_truck_starting_year(year[0], self.min_starting_year)
			self.max_starting_year = self.find_max_truck_starting_year(year[1], self.max_starting_year)

	def find_count_of_active_trucks(self):
		for year in range(self.min_starting_year, self.max_starting_year+1):
			self.count_trucks_by_year[year] = 0

		for truck_range in self.input_truck_ranges:
			for year in self.count_trucks_by_year:
				if year >= truck_range[0] and year <= truck_range[1]:
					self.count_trucks_by_year[year]+=1

	def find_year_with_minmax_active_trucks(self):
		self.year_with_absolute_min_trucks = min(self.count_trucks_by_year, key=self.count_trucks_by_year.get)
		self.year_with_absolute_max_trucks = max(self.count_trucks_by_year, key=self.count_trucks_by_year.get)

	def find_years_with_config_minmax_active_trucks(self, num_of_min_trucks, num_of_max_trucks):
		config_count_trucks = self.count_trucks_by_year.copy()
		self.num_of_min_trucks = num_of_min_trucks
		self.num_of_max_trucks = num_of_max_trucks

		for n in range(0, num_of_min_trucks):
			year_with_config_min_trucks = min(config_count_trucks, key=config_count_trucks.get)

			if year_with_config_min_trucks not in self.config_min_trucks:
				self.config_min_trucks.append(year_with_config_min_trucks)
				config_count_trucks.pop(year_with_config_min_trucks, None)

		for n in range(0, num_of_max_trucks):
			year_with_config_max_trucks = max(config_count_trucks, key=config_count_trucks.get)

			if year_with_config_max_trucks not in self.config_max_trucks:
				self.config_max_trucks.append(year_with_config_max_trucks)
				config_count_trucks.pop(year_with_config_max_trucks, None)

	def print_stats(self):
		print("Min: {} ({} trucks".format(self.year_with_absolute_min_trucks, self.count_trucks_by_year[self.year_with_absolute_min_trucks]))
		print("Max: {} ({} trucks".format(self.year_with_absolute_max_trucks, self.count_trucks_by_year[self.year_with_absolute_max_trucks]))
		print("Least-{}: {}".format(self.num_of_min_trucks, self.config_min_trucks))
		print("Top-{}: {}".format(self.num_of_max_trucks, self.config_min_trucks))


truckStatsFinder = TruckStatsFinder(input_truck_ranges)

truckStatsFinder.find_minmax_of_ranges(input_truck_ranges)
truckStatsFinder.find_count_of_active_trucks()
truckStatsFinder.find_year_with_minmax_active_trucks()
truckStatsFinder.find_years_with_config_minmax_active_trucks(5, 3)
truckStatsFinder.print_stats()
