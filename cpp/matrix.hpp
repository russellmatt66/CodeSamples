#ifndef MATRIX_H
#define MATRIX_H

#include <cstddef>
#include <vector>

class Matrix{
    public:
        Matrix(size_t M, size_t N): num_rows_(M), num_cols_(N), storage_(M * N, 0.0) {}

        // Row-Major order
        double& operator()(size_t i, size_t j) { return storage_[num_cols_ * i + j]; }
        const double& operator()(size_t i , size_t j) const { return storage_[num_cols_ * i + j]; }

        const size_t num_rows() const { return num_rows_; }
        const size_t num_cols() const { return num_cols_; }

    private:
        size_t num_rows_, num_cols_;
        std::vector<double> storage_;
};

// This is an implementation of a square matrix class based on std::vector<double>
class SquareMatrix{
    public:
        SquareMatrix(size_t N): num_rows_(N), num_cols_(N), storage_(N * N, 0.0) {}

        // Row-Major order
        double& operator()(size_t i, size_t j) { return storage_[num_cols_ * i + j]; }
        const double& operator()(size_t i, size_t j) const { return storage_[num_cols_ * i + j]; }

        const size_t num_rows() const { return num_rows_; }
        const size_t num_cols() const { return num_cols_; }

    private:
        size_t num_rows_, num_cols_;
        std::vector<double> storage_;
};

#endif