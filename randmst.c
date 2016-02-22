#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>




// typedef struct adj_matrix {
//     int nodes;
//     double matrix[][];
// } adj_matrix;


// return an array of coords
double** generate_coords(int numpoints, int dimension)
{
    double **coords = (double **) malloc(sizeof (double *) * numpoints);
     for (int i = 0; i < numpoints; ++i) {
         coords[i] = (double *) malloc(sizeof (double) * numpoints);
     }
    //double coords[numpoints][dimension];
        for (int i = 0; i < numpoints; i++)
        {
            for (int d = 0; d < dimension; d++)
            {
                coords[i][d] = (double)rand()/(double)RAND_MAX;
            }
        }
    return coords;
}


// Return the distances from node "index" to all other unvisited nodes
double* get_weights(int index, int numpoints, int dimension, double* visited, double** coords)
{
    double* weights = (double *) malloc(sizeof (double) * numpoints);
    if (dimension == 0)
    {
        for (int i = 0; i < numpoints; i++)
        {
            // if we haven't visied node i:
            if (visited[i] > 19.0)
            {
                weights[i] = (double)rand()/(double)RAND_MAX;
            }
            // if we have visited i, we don't want to calculate a new distance
            else
            {
                weights[i] = 20.0;
            }
        }
    }
    if (dimension != 0)
    {
        for (int i = 0; i<numpoints; i++)
        {
            if (visited[i] > 19.0)
            {
                // Find Euclidean distance:
                double distance = 0.0;
                for (int d = 0; d < dimension; d++)
                {
                    double p1 = coords[index][d];
                    double p2 = coords[i][d];
                    distance += pow(p1-p2, 2.0);
                    //distance += pow(coords[index][d]-coords[i][d], 2.0);
                }
                weights[i] = sqrt(distance);
            }
            // if we have visited i, we don't want to calculate a new distance
            else
            {
                weights[i] = 20.0;
            }
        }
    }
    weights[index] = 0.0;
    return weights;
}

// Generate graph with the given params; calculate weight of MST
double prim_mst(int n, int dims)
{
    double** coords = NULL;
    if(dims > 0)
    {
        coords = generate_coords(n, dims);
    }

    int root_index = rand();
    root_index = root_index % 3;
    double visited[n];
    for(int i=0; i<n; i++)
    {
        visited[i] = 20.0;
    }
    visited[root_index] = 0;
    double* all_weights = get_weights(root_index, n, dims, visited, coords);

    // these are used to keep track of things for prim's
    int min_index = root_index;
    float min_value = 0.0;

    for(int i=0; i<n; i++)
    {
        double* weights = get_weights(min_index, n, dims, visited, coords);
        visited[min_index] = min_value;
        min_value = 100.0;

        for(int j=0; j<n; j++)
        {
            // if it has not been visited yet (20.0 represents not visited)
            if(visited[j] > 19.0)
            {
                if(weights[j] < all_weights[j])
                {
                    all_weights[j] = weights[j];
                }
                if(all_weights[j] < min_value)
                {
                    min_value = all_weights[j];
                    min_index = j;
                }
            }
            
        }
    }

    // calculate the weight of the tree by summing all values in visited
    double w;
    for(int i=0; i<n; i++)
    {
        w += visited[i];
    }

    return w;
}




int main (int argc, char *argv[])
{
	//printf("Hello, world.");
	int testing = atoi(argv[1]);
	int numpoints = atoi(argv[2]);
	int numtrials = atoi(argv[3]);
	int dimension = atoi(argv[4]);

    // seed random num generator
    srand(time(NULL));
    double x = prim_mst(numpoints, dimension);
    printf("Pleseasease%f\n", x);

    // double weight = 0.0;
    // for (int reps = 0; reps < numtrials; reps++)
    // {
    //     weight = prim_mst(numtrials, dimension);
    // }


	return 0;
}