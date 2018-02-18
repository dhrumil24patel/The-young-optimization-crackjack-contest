import numpy as np
import pandas as pd

from helper import *

import random

data_path = './data/'

def total_costing(manufacturing_seq, shipping_region):
	#
	print()


def get_changeover_cost(manufacturing_seq):
	# collect number of changes
	changes = get_num_of_changes(manufacturing_seq)

# returns list of tupples of (plant, num_of_changes)
def get_num_of_changes(manufacturing_seq):
	plants = get_plant_list()
	results = []
	for plant in plants:
		for line in plant[1]:
			# get manufacuting sequence of 'plant'
			plant_seq = manufacturing_seq.loc[(manufacturing_seq['Plant'] == plant[0])\
			 & (manufacturing_seq['Line'] == line)]
			# calculate number of changes in this plant
			making = None
			change = 0
			for day_plan in plant_seq.iterrows():
				todays_product = day_plan[1]['Product_ID']
				# start with the 
				# if making is None:
					# making = todays_product
					# continue
				# if making product is different than day plan's product then
				# change making and increment change
				if todays_product != None and making != todays_product:
					making = todays_product
					change += 1
			results.append(((plant[0], line), change))
	return results



def test_get_num_of_changes():
	products = get_products_list()
	production_sequence = pd.read_csv(data_path+'test/manufacture_sequence.csv')
	for i in range(production_sequence.shape[0]):
		# production_sequence.set_value(i, 'Product_ID', str(random.choice(products)))
		production_sequence.loc[i, 'Product_ID'] = random.choice(products)
		# production_sequence.loc[i, 'Product_ID'] = 'P1'
	print('number of changes ', get_num_of_changes(production_sequence))

def test():
	test_get_num_of_changes()

test()