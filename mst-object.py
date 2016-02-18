import random
import math
import timeit

class AdjacencyMatrix(object):
    """Adjeacency Matrix obejct for covenient manipulation"""
    def __init__(self, n, dims):
        self.n = n
        self.matrix = []
        self.visited = {}

        # initialize one random vertex as root
        self.visited[random.randint(0, n-1)] = 0

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

    def find_min(self, i):
        """For input vertex with index i, finds non-visited vertex with minimum 
        weight and returns that vertex and its corresponding weight"""
        lowest_vertex = float("inf")
        lowest_weight = float("inf")

        # first search through ith row of matrix
        for j in range(i):
            if j not in self.visited:
                if self.matrix[i][j] < lowest_weight:
                    lowest_vertex = j 
                    lowest_weight = self.matrix[i][j]

        # next search through ith column
        for j in range(i+1, self.n):
            if j not in self.visited:
                if self.matrix[j][i] < lowest_weight:
                    lowest_vertex = j
                    lowest_weight = self.matrix[j][i]

        return (lowest_vertex, lowest_weight)

    def extract_min(self):
        """Extracts vertex with minimum weight from available vertices
        in matrix and adds that vertex/weight to visited dict"""
        # TODO: implement real error checking here for end of sequence?
        if len(self.visited.keys()) < self.n:
            lowest_vertex = float("inf")
            lowest_weight = float("inf")

            for v in self.visited.keys():
                u, weight = self.find_min(v)
                if weight < lowest_weight:
                    lowest_vertex = u
                    lowest_weight = weight

            self.visited[lowest_vertex] = lowest_weight

    def mst_weight(self):
        s = 0
        for weight in self.visited.values():
            s+= weight
        return s

    def prim_mst(self):
        """Complete's Prim's algorithm and return the final mst"""
        start = timeit.default_timer()
        while len(self.visited.keys()) < self.n:
            self.extract_min()

        # return the total weight of the mst
        s = self.mst_weigh()

        stop = timeit.default_timer()
        print "Seconds:", stop - start
        return s







        