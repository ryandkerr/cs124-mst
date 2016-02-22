#include <stdio.h>
#include <stdlib.h>
#include <time.h>




// typedef struct adj_matrix {
//     int nodes;
//     float matrix[][];
// } adj_matrix;


float** create_graph(int numpoints, int dimension)
{
	float **matrix = (float **) malloc(sizeof (float *) * numpoints);
	for (int i = 0; i < numpoints; ++i) {
    	matrix[i] = (float *) malloc(sizeof (float) * numpoints);
	}
   /* Intializes random number generator */
   srand((unsigned) time(NULL));

	if (dimension == 0)
	{
        // because we're filling in left-diagonal matrix, only one col is filled on first row,
        // then two on the second, cols just needs to go up to rows each loop.
            for (int row = 1; row < numpoints; row ++)
            {
            	for (int col = 0; col < row; col++)
            	{
                    matrix[row][col] = (float)rand()/(float)RAND_MAX;
                    printf("Check%d %d\n",row, col);
                }
            } 
    }

	if (dimension != 0)
	{
		int coords[numpoints];
		
	}

   return matrix;
}



// int matrix[numpoints][numpoints];


int main (int argc, char *argv[])
{
	//printf("Hello, world.");
	int testing = atoi(argv[1]);
	int numpoints = atoi(argv[2]);
	int numtrials = atoi(argv[3]);
	int dimension = atoi(argv[4]);

	// float[][] m = create_graph(numpoints, dimension);
	float** m = create_graph(numpoints, dimension);
	printf("%f\n", m[1][1]);

	//float m[numpoints][numpoints];
	//printf("%f\n", m[1][1]);
	//m[3][3] = 2;
	return 0;
}