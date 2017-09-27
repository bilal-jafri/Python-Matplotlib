#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import csv

africa_year = []

africa_array = []
america_array = []
south_east_asia = []
europe = []
eastern_mediterranean = []
western_pacific = []
_global = []

mortality_rate = []
global final_mortality_rate
final_mortality_rate = []
region = []

child_mortality_rate = []
final_child_mortality_rate = []

def plot_graph_one():	
	with open('/home/syedsaad/Desktop/MDG_0000000007,MDG_0000000001,WHOSIS_000003.csv') as csvfile:
		reader = csv.DictReader(csvfile)	
		for i in reader:
			if (i['WHO region'] == "Africa"):
				africa_array.append(i['Neonatal mortality rate (per 1000 live births)'])
	 			africa_year.append(i['Year'])
	 		if (i['WHO region'] == "Americas"):	
				america_array.append(i['Neonatal mortality rate (per 1000 live births)'])
	 		if (i['WHO region'] == "South-East Asia"):	
				south_east_asia.append(i['Neonatal mortality rate (per 1000 live births)'])
	 		if (i['WHO region'] == "Europe"):	
				europe.append(i['Neonatal mortality rate (per 1000 live births)'])
	 		if (i['WHO region'] == "Eastern Mediterranean"):	
				eastern_mediterranean.append(i['Neonatal mortality rate (per 1000 live births)'])
	 		if (i['WHO region'] == "Western Pacific"):	
				western_pacific.append(i['Neonatal mortality rate (per 1000 live births)'])
	 		if (i['WHO region'] == "Global"):	
				_global.append(i['Neonatal mortality rate (per 1000 live births)'])
	font = {'family': 'serif',
	        'color':  'darkred',
	        'weight': 'normal',
	        'size': 16,
	        }
	plt.plot(africa_year, africa_array, 'r', label='Africa')
	plt.plot(africa_year, america_array, 'g', label='America')
	plt.plot(africa_year, south_east_asia, 'b', label='South East Asia')
	plt.plot(africa_year, europe, 'm', label='Europe')
	plt.plot(africa_year, eastern_mediterranean, 'c', label='Eastern Mediterranean')
	plt.plot(africa_year, western_pacific, 'y', label='Western Pacific')
	plt.plot(africa_year, _global, 'k', label='Global')
	plt.title('Year vs Neonatal Mortality Rate', fontdict=font)
	plt.xlabel('Year', fontdict=font)
	plt.ylabel('Neonatal Mortality Rate', fontdict=font)
	plt.subplots_adjust(left=0.15)
	legend = plt.legend(loc='upper right')
	frame = legend.get_frame()
	frame.set_facecolor('0.90')
	plt.show()

def plot_graph_two():
	global final_mortality_rate
	with open('/home/syedsaad/Desktop/MDG_0000000007,MDG_0000000001,WHOSIS_000003.csv') as csvfile:
		reader = csv.DictReader(csvfile)	
		for j in reader:
			if (j['Year'] == " 2015"):
				mortality_rate.append(j['Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)'])
				region.append(j['WHO region'])
		for k in mortality_rate:
			final_mortality_rate.append(k[0:4:1])	
	y_pos = np.arange(len(region))
	plt.bar(y_pos, final_mortality_rate, align='center')
	plt.xticks(y_pos,region)
	print final_mortality_rate
	plt.show()
	return final_mortality_rate

def plot_graph_three():
	global final_mortality_rate
	#print final_mortality_rate
	with open('/home/syedsaad/Desktop/MDG_0000000007,MDG_0000000001,WHOSIS_000003.csv') as csvfile:
		reader = csv.DictReader(csvfile)	
		for j in reader:
			if (j['Year'] == " 2015"):
				child_mortality_rate.append(j['Under-five mortality rate (probability of dying by age 5 per 1000 live births)'])
				mortality_rate.append(j['Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)'])
				region.append(j['WHO region'])				
		for k in child_mortality_rate:
			final_child_mortality_rate.append(k[0:4:1])
		for k in mortality_rate:
			final_mortality_rate.append(k[0:4:1])	
	
	print final_child_mortality_rate
	print final_mortality_rate
	fig, ax = plt.subplots()
	bar_width = 0.35
	opacity = 0.8	
	y_pos = np.arange(len(region))
	rects1 = plt.bar(y_pos, final_mortality_rate, bar_width, alpha=opacity, color='b')
	rects1 = plt.bar(y_pos + bar_width, final_child_mortality_rate, bar_width, alpha=opacity, color='g')
	plt.xticks(y_pos + bar_width/2, region)
	plt.show()

plot_graph_one()
plot_graph_two()
#plot_graph_three()