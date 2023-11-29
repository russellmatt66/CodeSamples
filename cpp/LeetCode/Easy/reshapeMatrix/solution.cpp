// https://leetcode.com/problems/reshape-the-matrix/description/
#include <vector>
using namespace std;
class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
        int num_rows = mat.size();
        int num_cols = mat[0].size(); // assume rectangular
        int oldDim = num_rows * num_cols, newDim = r * c;

        if (oldDim != newDim){ // matrices must have same number of elements
            return mat;
        }

        vector<vector<int>> newMat (r, vector<int>(c,0));
        vector<int> tempVec(newDim, 0);

        // first reshape into vector
        for (int i = 0; i < num_rows; i++){
            for (int j = 0; j < num_cols; j++){
                 tempVec[i * num_cols + j]= mat[i][j];
            }
        }

        // then populate reshaped vector into new shape
        for (int ir = 0; ir < r; ir++){
            for (int ic = 0; ic < c; ic++){
                newMat[ir][ic] = tempVec[ir * c + ic];
            }
        }
        return newMat;
    }
};