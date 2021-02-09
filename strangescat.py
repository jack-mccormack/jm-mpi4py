#!/usr/bin/env python3
"""
scatter/gather improper use demo
"""

from mpi4py import MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()

root = 0

if rank == root:
	"""
	this can't be scattered properly
	"""
	data = [i for i in range(size - 2)]
else:
	data = None
data = comm.scatter(data)
print("process #" +str(rank) + ": " + str(data))
