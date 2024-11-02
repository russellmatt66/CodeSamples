#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]){
    int N = atoi(argv[1]);

    printf("Computing factorial of %d in serial\n", N);

    int result = 1;
    for (int i = 2; i <= N; i++){
        result *= i;
    }

    printf("Factorial of %d is: %d\n", N, result);

    return 0;
}