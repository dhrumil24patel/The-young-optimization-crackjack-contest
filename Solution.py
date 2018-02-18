import numpy as np
import pandas as pd

from helper import *
from costing import *

import random

data_path = './data/'

def solve():
	# get top demanding products
	sorted_freq, prod_freq = get_most_demanding_products(top=20)