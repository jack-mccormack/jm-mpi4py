# mpi4py
MPI is a system that allows communication between processes in a distributed computing arrangement; mpi4py allows you to write it into python code.

# point-to-point communication
this is when data passes directly from one process to another, along one of the following lines:
## scatter
automatically splits an array of data between recipients, fails without a 1-to-1 ratio
## gather
collects data from different processes into a list
## broadcast
sends one piece of data to every process
## reduce
combines data from different processes into one item
