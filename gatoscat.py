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
"""
scatters the data from root
"""
data = comm.scatter(data)
print("process #" +str(rank) + ": " + str(data))

"""
gathers the data to root
"""
bucket = comm.gather(data)
if rank == root:
	print(bucket)
