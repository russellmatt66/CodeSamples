#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]){
    int rank, world_size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    int N = atoi(argv[1]);
    if(rank == 0){
        printf("Computing factorial of: %d with %d processes\n", N, world_size);
    }

    int localResult = 1;
    for(int i = (2 + rank); i <= N; i += world_size){
        localResult *= i;
    }

    int total;
    MPI_Reduce(&localResult, &total, 1, MPI_INT, MPI_PROD, 0, MPI_COMM_WORLD);

    if(rank == 0){
        printf("factorial of: %d = %d\n", N, total);
    }

    MPI_Finalize();
    return 0;
}