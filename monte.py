#!/usr/bin/env python3
"""
finding pi w/ the monte carlo method
"""

from mpi4py import MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
import numpy as np

root = 0

"""
setting up important features
"""
def circlecheck(x, y):
	return x**2 + y**2 <= 1
unit = 0
tries = 100
alltries = tries*size
"""
beginning the script
"""
for x in range(tries):
	if(circlecheck(np.random.rand(), np.random.rand())):
		unit += 1
unittotal = comm.reduce(unit, root=root)
if rank==root:
	pi = 4*(unittotal/(alltries))
	print("pi ~= " + (str)(pi))
