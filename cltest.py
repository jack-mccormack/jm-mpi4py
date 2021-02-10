#!/usr/bin/env python3
"""
tests a filesystem
"""

from mpi4py import MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()
fpIn = open("/clusterfs/test.txt", "r")
contents = fpIn.read()
print("I am process %d of %d on %s" % (rank, size, name))
print(contents)
