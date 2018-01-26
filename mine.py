#!/usr/bin/env python


import request
import time

def time_to_count(num):
	t=time.time()
	x=0
	while True:
		x=x+1
		if x>num:
			return time.time()-t
	


if __name__=="__main__":
	print(time_to_count(100000))
