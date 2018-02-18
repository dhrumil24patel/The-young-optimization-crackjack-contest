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

def get_predicted_demand():
	return pd.read_csv('./predicted_demand.csv')

def delivery_cost():
	return pd.read_csv(data_path+'train/delivery_cost.csv')

def production_capacity():
	return pd.read_csv(data_path+'train/production_capacity.csv')

def products():
	shipping_region = pd.read_csv(data_path+'test/shipping_region.csv')
	products = np.unique(shipping_region['Product_ID'])
	del shipping_region
	return products

def regions():
	return np.unique(predicted_demand()['Region'])

def get_most_demanding_products(top = 10):
	products = products()
	for i in range(len(products)):
		freq = predicted_demand.loc[(predicted_demand['Product_ID'] == products[i])]
		prod_freq[i] = freq['Demand'].sum()

	# sort the prod_freq
	sorted_freq = sorted(prod_freq)
	# reverse it
	sorted_freq.reverse()
	# print([products[prod_freq.index(freq)] for freq in sorted_freq][:top])
	# products[prod_freq.index(max(prod_freq))]
	return [products[prod_freq.index(freq)] for freq in sorted_freq][:top], prod_freq