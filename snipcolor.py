#!/usr/bin/env python3
"""
ruining an image by changing the colors in vertical strips
"""

from mpi4py import MPI
import cv2 as cv
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

root = 0

main = cv.imread("/clusterfs/jackm/venusbad.jpg", cv.IMREAD_COLOR)
height, width = main.shape[:2]
marker = width//size
roi = main[:height, rank*marker:(rank+1)*marker]
b, g, r = cv.split(roi)
colors = [b, g, r]
colors[rank%3]+= 100
roi = cv.merge(colors)
rois = comm.gather(roi, root=root)
if(rank == root):
	main = cv.hconcat(rois)
	cv.imwrite("/clusterfs/jackm/venus-spicy.jpg", main)
