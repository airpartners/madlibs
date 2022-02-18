import numpy as np
import pandas as pd

# Class for importing and sorting AP data
class APDataFrame(object):

	def __init__(self):

		self.df = pd.DataFrame()

		# dictionary of cardinal directions and corresponding degrees
		self.wind_dict = {'NE': [22.5, 67.5],
							'E': [67.5, 112.5],
							'SE': [112.5, 157.5],
							'S': [157.5, 202.5],
							'SW': [202.5, 247.5],
							'W': [247.5, 292.5],
							'NW': [292.5, 337.5]}
		
		# dictionary with time of day definition
		self.time_dict = {'early morning': [4, 6],
							'morning': [6, 10],
							'midday': [10, 13],
							'afternoon': [13, 16],
							'evening': [16, 19],
							'night': [19, 22]}
	
	# takes csv file and reads into dataframe	
	def load_data(self, csv_file = r"C:\Users\13348\madlibs\app\data\sn45-final-w-ML-PM.csv"):
		self.df = pd.read_csv(csv_file)
		print(self.df)

	# sorts and indexes dataframe via wind direction
	def sort_by_dir(self, wind_dir):
		if wind_dir == "N":
			self.df = self.df[(self.df["wind_dir"] > 337.5) | (self.df["wind_dir"] < 22.5)]
		else:
			dir_range = self.wind_dict[wind_dir]
			self.df = self.df[(self.df["wind_dir"] < (dir_range[1])) & (self.df["wind_dir"] > dir_range[0])]

	# sorts and indexes dataframe via time of day
	def sort_by_time(self, time):
		pass

	def sort_by_pollutant(self, pollutant):
		self.df = self.df.loc[:, ["date_local", "timestamp", "wind_dir", pollutant]]

# testing~
data = APDataFrame()
data.load_data()
data.sort_by_dir("E")
data.sort_by_pollutant("co")
print(data.df)
