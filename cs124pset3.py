### CS 124 Assignment 3

### February 22, 2016

### Joseph Hostyk, Ryan Kerr


# Create a new x containing only the element x.
def makeset(x):
	return

#  Given an element x, which set does it belong to?
def find(x):
	return

# Replace the set containing x and the set containing y by their union.
def union(x,y):
	return


import random
import math
# Create a dims-dimension graph with n nodes:
def create_graph(n, dims):
	if dims == 0:
		matrix = [[0]*n for x in range(n)]
		# because we're filling in left-diagonal matrix, only one col is filled on first row,
		# then two on the second, cols just needs to go up to rows each loop.

		for row in range(1,n):
			for col in range(0,row):
				matrix[row][col] = random.random()

	if dims != 0:
		# 1D array of coords:
		coords = [[0]*dims for x in range(n)]
		for i in range(0,n):
			for d in range(dims):
				coords[i][d] = random.random()
		# matrix of distances:
		matrix = [[0]*n for x in range(n)]
		# Fill in distances:
		for row in range(1,n):
			for col in range(0, row):
				point1 = coords[row]
				point2 = coords[col]
				sumSquares = [math.pow(point1[i]-point2[i],2) for i in range(len(point1))]
				distance = math.sqrt(sum(sumSquares))
				matrix[row][col] = distance




# Find MST:
# visitedVertices =[]
# when length(vistied )= n
# 	we're done

# randnum generator: 100000000.0/(struct.unpack("<L", os.urandom(4))[0])



if __name__ == "__main__":
	create_graph(2000,2)

