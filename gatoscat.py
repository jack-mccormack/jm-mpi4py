#!/usr/bin/env python3
"""
scatter/gather demo
"""

from mpi4py import MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()

root = 0

if rank == root:
	data = [i for i in range(size)]
else:
	data = None
data = comm.scatter(data)
print("process #" +str(rank) + ": " + str(data))
bucket = comm.gather(data)
if rank == root:
	print(bucket)
