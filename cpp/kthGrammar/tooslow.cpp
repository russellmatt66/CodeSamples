using namespace std;

#include<vector>
#include<string>

// Too slow for all the cases
class Solution {
public:
    int kthGrammar(int n, int k) {
        std::vector<string> table(n);
        table[0] = "0";
        for (int is = 1; is < n; is++){
            table[is] = nextRow(table[is-1]); 
        }
        if (table[n-1][k-1] == 48) {
            return 0;
        }// ascii value for 0
        else { return 1; }
    }
private:
    string nextRow(string prevRow){
        string tempString = "";
        for (int ic = 0; ic < prevRow.size(); ic++){
            if (prevRow[ic] == '0'){
                tempString += "01";
            }
            else if (prevRow[ic] == '1'){
                tempString += "10";
            }
        }
        return tempString;
    }
};