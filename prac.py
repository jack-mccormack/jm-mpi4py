#!/usr/bin/env python3
"""

"""

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

root = 0

if rank == root:
	data = {'a': 7, 'b': 3.14}
	comm.send(data, dest=1, tag=11)
elif rank == 1:
	data = comm.recv(source=0, tag=11)
	print("from " + str(rank) + " the data: " + str(data))


