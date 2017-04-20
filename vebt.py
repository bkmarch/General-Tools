#Van Emde Boas Tree

import math
from decimal import *

#def sort_input(z):		takes list and sorts if I feel like it. just for the practice. Quick sort = O(nlgn). Max heap = O(n)

input = []				#list of numbers input
bit_vector  = [] 		#list of 1s and 0s for present or not
pwr = 0					#exponent 2,4,8,16,32
maximum = 0				#actual maximum value of our input so we don't need to do extra comparisons and just fill in summary vector with 0s

def create_bit_vector(x):
	max = 0
	for i in x:						
		if i > max:
			max = i					#get max value from input list
	
	maximum = max
	power = 0
	
	
	while 2**power <= max+1:		#obtains a power of 2. ex 32 but 32 isn't a square number
		if 2**power == max+1:
			break
		else:
			power += 1
		
	len_bv = 2**power
	pwr = power						#set length of bit vector to outer variable

	for i in range(len_bv):			#initialize bit vector that has a length that is a power of 2
		bit_vector[i] = 0			#want to create power of 2 to make things easier	
		
	for i in input:					#fill bit vector
		if bit_vector[i] = 0:
			bit_vector[i] = 1
		else:
			pass	
				
A = create_bit_vector(input)		#ex [1,0,0,0,1,0,1,0]

def create_summary_vector(k):			#k is our bit_vector. fnc returns our summary vector
	
	pwr2 = pwr
	while Decimal(math.sqrt(2**pwr2)) % 1 != 0:		#find cluster size exponent
		pwr2 -= 1
	
	cluster_size = math.sqrt(2**pwr2)				#get actual size of cluster.
	
	summary_layer = math.floor(pwr/2)				#height we need to go up to get to our summary vector layer
	current_layer = 0								#start at leaves.
	
	summary_vector = []
	
	holding_bit_vector = k
	next_layer_vector = []
	
	while current_layer <= summary_layer:
		
		len_current_v = len(holding_bit_vector)		#length of the current vector we are looking at. not the one we are appending to
		start = 0									#leaf layer
		end = summary_layer							#summary vector layer that we want to end at
		cluster_chunk =	cluster_size
		
		while cluster_chunk <= len_current_v:
			if 1 in holding_bit_vector[start:cluster_size]:
				next_layer_vector.append(1)
				start += cluster_size
				cluster_chunk += cluster_size
			else:
				next_layer_vector.append(0)
				start += cluster_size
				cluster_chunk += cluster_size
				
		if current_layer == summary_layer:			#summary vector created and finished
			summary_vector = next_layer_vector
			current_layer += 1
		
		else:
			holding_bit_vector = next_layer_vector #layer finished and now we move up another level
			current_layer += 1
	
	return summary_vector

B = create_summary_vector(A)		
	
def augment_bit_vector(v):	#augments bit vector with min and max values for each cluster.

	
	
	
	
	