#!/usr/bin/env python

from redis import Redis
from rq import Worker


connection=Redis(host="localhost")
workers=Worker.all(connection=connection)
for worker in workers:
	worker.register_death()
