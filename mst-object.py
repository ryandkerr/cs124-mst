import random
import math
import timeit
import pdb

class AdjacencyMatrix(object):
    """Adjeacency Matrix obejct for covenient manipulation"""
    def __init__(self, n, dims):
        start = timeit.default_timer()
        self.n = n
        self.matrix = []

        # first create our adjacency matrix
        if dims == 0:
            self.matrix = [[0]*n for x in range(n)]
            # because we're filling in left-diagonal matrix, only one col is filled on first row,
            # then two on the second, cols just needs to go up to rows each loop.

            for row in range(1,n):
                for col in range(0,row):
                    self.matrix[row][col] = random.random()

        if dims != 0:
            # 1D array of coords:
            coords = [[0]*dims for x in range(n)]
            for i in range(0,n):
                for d in range(dims):
                    coords[i][d] = random.random()
            # matrix of distances:
            self.matrix = [[0]*n for x in range(n)]
            # Fill in distances:
            for row in range(1,n):
                for col in range(0, row):
                    point1 = coords[row]
                    point2 = coords[col]
                    sumSquares = [math.pow(point1[i]-point2[i],2) for i in range(len(point1))]
                    distance = math.sqrt(sum(sumSquares))
                    self.matrix[row][col] = distance

        # initialize one random vertex as root and prepare tracking lists
        self.root_index = random.randint(0, n-1)
        self.all_weights = self.get_weights(self.root_index)
        self.visited = [None] * n
        self.visited[self.root_index] = 0
        self.min_index = self.root_index
        self.min_value = 0

        stop = timeit.default_timer()
        print stop - start, "seconds"


    def get_weights(self, i):
        """Returns a list of the weights for vertex i's edges.
        Note that this returns a weight of 0 at index i."""
        weights = [0] * self.n
        for j in range(i):
            weights[j] = self.matrix[i][j]
        for j in range(i+1, self.n):
            weights[j] = self.matrix[j][i]
        return weights


    def mst_weight(self):
        s = 0
        for weight in self.visited:
            if weight:  # check that it's not None - temporary
                s+= weight
        return s

    def prim_mst(self):
        """Complete's Prim's algorithm and return the final mst"""
        start = timeit.default_timer()
        for _ in range(self.n):
            weights = self.get_weights(self.min_index)
            self.visited[self.min_index] = self.min_value
            
            # reset min value
            self.min_value = float("inf")
            for i, weight in enumerate(weights):
                if self.visited[i] == None:
                    if weight < self.all_weights[i]:
                        self.all_weights[i] = weight
                    if self.all_weights[i] < self.min_value:
                        self.min_value = self.all_weights[i]
                        self.min_index = i

        # return the total weight of the mst
        s = self.mst_weight()
        stop = timeit.default_timer()
        print "Seconds:", stop - start
        return s







        