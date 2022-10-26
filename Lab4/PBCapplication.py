import numpy as np

address = "/Users/nishxntyxdxv/Desktop/sem7/Computational-Chemistry-Lab/Lab4/PROBLEM3.data"

def readLocation(fileAddress):
    txt = open(fileAddress, "r")

    coordinates = []

    for x in txt:
        # print(x)
        if x[0] != "#":
            temp = x.split()
            location = np.array([float(temp[0]), float(temp[1]), float(temp[2])])
            # print(velocity)
            coordinates.append(location)
            
    return np.array(coordinates)

# Update function takes current state to next state
# Obeying Periodic Boundary Condition

def update(arr, l):
    # 'nudge' is the matrix that contains the changes
    # to be done in coordinates of particles to take
    # them to a new state. Norm is taken to ensure
    # 1 unit displacement in any random direction
    nudge = np.linalg.norm(np.random.rand(216, 3))
    arr = arr + nudge
    
    for i in arr:
        # Checking the Boundary condition
        if i[0] >= l/2: i[0] = i[0] - l 
        if i[0] < -l/2: i[0] = i[0] + l 
        if i[1] >= l/2: i[1] = i[1] - l 
        if i[1] < -l/2: i[1] = i[1] + l
        if i[2] >= l/2: i[2] = i[2] - l 
        if i[2] < -l/2: i[2] = i[2] + l 
    
#     arr = np.array(arr)
    return arr

# list of coordinates of all the particles in system
locs = readLocation(address)

# length of the box
l = 18.64

# number of iterations
its = 10

states = []
states.append(locs)

for i in range(1, its + 1):
    states.append(update(states[i - 1], l))
    #print("max coordinate of state {} is: {}".format(i, np.amax(states[i])))

print(states[10])


# Saving the 2D array in a text file
file = open("out.txt", "w+")
file.write("# The coordinates of particles after 10 iterations: \n")
for x in states[10]:
    file.write(str(x[0])[:8] + "       " + str(x[1])[:8] + "       " + str(x[2])[:8] + "\n")

