https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/submissions/
class Solution {
public:
    bool checkValid(vector<vector<int>>& matrix) {
        int n = matrix.size();
        std::vector<int> numFreq (n+1,0); // std::vector is 0-indexed
        
        // Scan through rows
        for (int i = 0; i < matrix.size(); i++){
            std::fill(numFreq.begin(), numFreq.end(), 0);
            for (int j = 0; j < matrix[0].size(); j++){
                if (matrix[i][j] > n){
                    return false;
                }
                numFreq[matrix[i][j]] += 1;
                if (numFreq[matrix[i][j]] > 1){
                    return false;
                }
            }
        }

        // Scan through columns
        for (int j = 0; j < matrix[0].size(); j++){
            std::fill(numFreq.begin(), numFreq.end(), 0);
            for (int i = 0; i < matrix.size(); i++){
                if (matrix[i][j] > n){
                    return false;
                }
                numFreq[matrix[i][j]] += 1;
                if (numFreq[matrix[i][j]] > 1){
                    return false;
                }
            }
        }
        return true;
    }
};