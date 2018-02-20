import numpy as np
import pandas as pd

import random

data_path = './data/'

# returns the list of plants
def get_plant_list():
	return [('A', [1,2]), ('B', [1,2,3]), ('C', [1])]

def changeover_cost(plant, line):
	changeover_cost = pd.read_csv(data_path+'train/changeover_cost.csv')
	return changeover_cost.loc[(changeover_cost['Plant'] == plant) & (changeover_cost['Line'] == line)]

def get_products_list():
	shipping_region = pd.read_csv(data_path+'test/shipping_region.csv')
	products = np.unique(shipping_region['Product_ID'])
	del shipping_region
	return products

def get_predicted_demand(month = 'all'):
	predicted_demand = pd.read_csv('./predicted_demand.csv')
	if month == 37:
		predicted_demand = pd.read_csv('./predicted_demand_in_37.csv')
	elif month == 38:
		predicted_demand = pd.read_csv('./predicted_demand_in_38.csv')
	elif month == 39:
		predicted_demand = pd.read_csv('./predicted_demand_in_39.csv')
	return predicted_demand

def _delivery_cost():
	return pd.read_csv(data_path+'train/delivery_cost.csv')

def _production_capacity():
	return pd.read_csv(data_path+'train/production_capacity.csv')

def _products():
	shipping_region = pd.read_csv(data_path+'test/shipping_region.csv')
	products = np.unique(shipping_region['Product_ID'])
	del shipping_region
	return products

def regions():
	return np.unique(predicted_demand()['Region'])

# get the list of demanding products sorted in descending according to their
#  overall demand and the list of 
def get_most_demanding_products(top = 10, month='all'):
	products = _products()
	prod_freq = [0]*len(products)
	prod_freq_set = {}
	predicted_demand = get_predicted_demand(month=month)
	for i in range(len(products)):
		freq = predicted_demand.loc[(predicted_demand['Product_ID'] == products[i])]
		prod_freq_set[products[i]] = freq['Demand'].sum()
		prod_freq[i] = freq['Demand'].sum()

	# sort the prod_freq
	sorted_freq = sorted(prod_freq)
	# reverse it
	sorted_freq.reverse()
	# print([products[prod_freq.index(freq)] for freq in sorted_freq][:top])
	# products[prod_freq.index(max(prod_freq))]
	results = [products[prod_freq.index(freq)] for freq in sorted_freq][:top]
	print("total demand ", sum(prod_freq))
	results_sum = sum([freq for freq in sorted_freq][:top])
	print("demand of top ", top, " ", results_sum)
	return results, prod_freq_set



def test_get_most_demanding_products(top, month):
	print(get_most_demanding_products(top, month))


def test():
	test_get_most_demanding_products(20, 37)


test()