# -*- coding: utf-8 -*-
"""
Author: Nishant Yadav
Roll Number: 19CY20025
Date: 12/10/2022

"""
# Importing libraries
import numpy as np

# Location of the file
address = "Data/PROBLEM1.data"

# Function that reads velocity vectors from text data
def readVelo(fileAddress):
    # This function returns a list of velocities
    # Each row of the list corresponds to velocity components of a single particle
    txt = open(fileAddress, "r")

    velocities = []

    for x in txt:
        # print(x)
        if x[0] != "#":
            temp = x.split()
            velocity = np.array([float(temp[1]), float(temp[2]), float(temp[3])])
            # print(velocity)
            velocities.append(velocity)

    return velocities

# Function that calculates the kinetic energy of system
# This function takes velocity list and mass as input
def KE(mass, velocities):
    sum = 0;
    for velocity in velocities:
        for v in velocity:
            sum += 0.5*mass*(v**2)

    return sum

# calculating list of velocities
arr = readVelo(address)

# calculating energy of system of paticles of mass = 1
TKE = KE(1, arr)

# Printing the results
print("The Total Energy of System of N Particles: ", TKE)