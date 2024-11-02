#include <stdio.h>
#include <stdlib.h>

int factorial(int N);

int main(int argc, char* argv[]){
    int N = atoi(argv[1]);

    printf("Recursively computing factorial of %d in serial\n", N);

    int result = factorial(N);

    printf("Factorial of %d is: %d\n", N, result);

    return 0;
}

int factorial(int N){
    if (N == 1){
        return 1;
    }

    return N * factorial(N - 1);
}