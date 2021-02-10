# mpi4py
MPI is a system that allows communication between processes in a distributed computing arrangement; mpi4py allows you to write it into python code.

# point-to-point communication
this is when data passes directly from one process to another, using either .send or .recv (receive)
# collective communication
every process is involved, uses one of the following:
## scatter
automatically splits an array of data between recipients; fails without a clean ratio of elements to recipients
## gather
collects data from different processes into a list
## broadcast
sends one piece of data to every process
## reduce
combines data from different processes into one item
