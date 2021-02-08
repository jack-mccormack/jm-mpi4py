#!/usr/bin/env python3
"""
adds the rank of each processor
"""

from mpi4py import MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

root = 0

data = rank
sum = comm.reduce(data)
if rank == root:
	print(sum)
