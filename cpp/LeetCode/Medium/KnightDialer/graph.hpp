#include <vector>
#include <string>

using vector = std::vector<int>;

// https://leetcode.com/problems/knight-dialer/?envType=daily-question&envId=2023-11-27
class KnightDialerGraph{
    public:
        KnightDialerGraph() : std::vector<vector> AdjMat(10, vector(10,0))
        {
            // Initialize the rest of the adjacency matrix for the Knight Dialer problem 
            AdjMat[0][4] = 1;
            AdjMat[0][6] = 1;
            AdjMat[1][6] = 1;
            AdjMat[1][8] = 1;
            AdjMat[2][7] = 1;
            AdjMat[2][9] = 1;
            AdjMat[3][4] = 1;
            AdjMat[3][8] = 1;
            AdjMat[4][0] = 1;
            AdjMat[4][3] = 1;
            AdjMat[4][9] = 1;
            AdjMat[6][0] = 1;
            AdjMat[6][1] = 1;
            AdjMat[6][7] = 1;
            AdjMat[7][2] = 1;
            AdjMat[7][6] = 1;
            AdjMat[8][1] = 1;
            AdjMat[8][3] = 1;
            AdjMat[9][2] = 1;
            AdjMat[9][4] = 1; 
        }

        // Phone number of length n
        std::string PhoneNumber(int n){
            
        }

    private:
        std::vector<vector> AdjMat;
};