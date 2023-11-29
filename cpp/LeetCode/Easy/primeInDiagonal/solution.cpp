// https://leetcode.com/problems/prime-in-diagonal/submissions/
class Solution {
public:
    int diagonalPrime(vector<vector<int>>& nums) {
        int i = 0, maxDiagPrime = 0;
        for (; i < nums.size(); i++){
            for (int j = 0; j < nums[0].size(); j++){
                if (isPrime(nums[i][j]) && onDiag(nums.size(),i,j) && nums[i][j] > maxDiagPrime){
                    maxDiagPrime = nums[i][j];
                }
            }
        }
        return maxDiagPrime;
    }

    // Prime-checking algorithm courtesy of Chat-GPT
    bool isPrime(int number) {
        if (number <= 1) {
            return false;  // 0 and 1 are not prime numbers
        }

        if (number <= 3) {
            return true;   // 2 and 3 are prime numbers
        }

        if (number % 2 == 0 || number % 3 == 0) {
            return false;  // numbers divisible by 2 or 3 are not prime
        }

        for (int i = 5; i * i <= number; i += 6) {
            if (number % i == 0 || number % (i + 2) == 0) {
                return false;  // numbers divisible by i or i+2 are not prime
            }
        }

        return true;
    }

    bool onDiag(int numsLength, int i, int j){
        if (i == j || j == numsLength - i - 1) {
            return true;
        }
        else {
            return false;
        }
    }
};