// https://leetcode.com/submissions/detail/1084219375/

#include<cmath>

class Solution {
public:
    int kthGrammar(int n, int k) {
        // base case
        if (n == 1 && k == 1){
            return 0;
        }
        // Recurrence relation
        else if (k < pow(2, n-2) + 1) {
            return kthGrammar(n-1, k);
        }
        else if (k >= pow(2, n-2) + 1){
            return !(kthGrammar(n-1, k - pow(2,n-2)));
        }
        return -1;
    }
};
