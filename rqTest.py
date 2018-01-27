#!/usr/bin/env python



from rq import Queue
from redis import Redis
from mine import time_to_count
import time


redis_conn=Redis()
highQue=Queue("HIGH",connection=redis_conn)
medQue=Queue("MED",connection=redis_conn)
lowQue=Queue("LOW",connection=redis_conn)
def allque():
	jobs=[]
	t=time.time()
	for x in range(1000):
		jobs.append(lowQue.enqueue(time_to_count,1000000))
		jobs.append(medQue.enqueue(time_to_count,1000000))
		jobs.append(highQue.enqueue(time_to_count,1000000))
	while len(jobs)>0:
		#print(len(jobs))
		for x in jobs:
			if x.is_finished:
				jobs.remove(x)
	print("All Done")
	print(time.time()-t)

def contAdding():
	jobs=[]
	q=highQue
	while True:
		if len(q.jobs)<1000:
			jobs.append(q.enqueue(time_to_count,100000000))

#allque()
contAdding()
	
