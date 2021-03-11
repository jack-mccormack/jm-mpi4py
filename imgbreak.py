#!/usr/bin/env python3
"""
inverts the middle ninth of the image
"""
import cv2 as cv
from mpi4py import MPI

plan = cv.imread("/clusterfs/Venus.png", cv.IMREAD_COLOR)
(height, width) = plan.shape[:2]
chunk = plan[(height//3):2*(height//3), (width//3):2*(width//3)]
chunk = cv.flip(chunk, 0)
chunk = cv.flip(chunk, 1)
long1 = plan[:(height//3), :width]
long2 = plan[2*(height//3):height, :width]
small1 = plan[(height//3):2*(height//3), :(width//3)]
small2 = plan[(height//3):2*(height//3), 2*(width//3):width]
chunk = cv.hconcat([small1, chunk, small2])
chunk = cv.vconcat([long1, chunk, long2])
cv.imwrite("/clusterfs/jackm/venusbad.jpg", chunk)
