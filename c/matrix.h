#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int num_rows;
    int num_cols;
    double **data; // 2D array of doubles
} Matrix;

// Column-Major order
Matrix createMatrix(int num_rows, int num_cols) {
    Matrix mat;
    mat.num_rows = num_rows;
    mat.num_cols = num_cols;

    // Allocate a row of double *
    mat.data = (double **)malloc(num_rows * sizeof(double *));
    
    for (int i = 0; i < num_rows; i++) { // allocate the columns
        mat.data[i] = (double *)malloc(num_cols * sizeof(double));
    }

    return mat;
}

void freeMatrix(Matrix mat) {
    for (int i = 0; i < mat.num_rows; i++) {
        free(mat.data[i]);
    }
    free(mat.data);
}

void setElement(Matrix mat, int row, int col, double value) {
    if (row >= 0 && row < mat.num_rows && col >= 0 && col < mat.num_cols ) {
        mat.data[row][col] = value;
    }
}

double getElement(Matrix mat, int row, int col) {
    if (row >= 0 && row < mat.num_rows && col >= 0 && col < mat.num_cols ) {
        return mat.data[row][col];
    }
    else {
        // Handle out-of-bounds access
        printf("Out-of-bounds access\n");
    }
}