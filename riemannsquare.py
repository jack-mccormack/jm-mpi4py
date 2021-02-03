#!/usr/bin/env python3
"""

"""
import math
from mpi4py import MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()

root = 0

data = math.pow(rank + 1, 2)
comm.send(data, dest=root, tag = rank)

if rank == root:
	sum = 0
	for i in range(size):
		sum += comm.recv(source = i, tag = i)
	print("area under x^2 through " + str(size) + ": ~" + str(sum))
