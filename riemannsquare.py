#!/usr/bin/env python3
"""
this takes a right riemann sum of x^2 with interval length 1 and 1 interval
for each processor
"""
import math
from mpi4py import MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

root = 0

data = math.pow(rank + 1, 2)
comm.send(data, dest=root, tag = rank)

if rank == root:
	sum = 0
	for i in range(size):
		sum += comm.recv(source = i, tag = i)
	print("area under x^2 through " + str(size) + ": ~" + str(sum))
