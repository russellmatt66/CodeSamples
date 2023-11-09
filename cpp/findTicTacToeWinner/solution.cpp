// https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/submissions/
class Solution {
public:
    string tictactoe(vector<vector<int>>& moves) {
        std::vector<std::vector<char>> ticTacToeBoard(3, std::vector<char>(3, '\0'));
        char whoseTurn = 'A';
        
        // Play out the game
        for (int i = 0; i < moves.size(); i++){
            if (whoseTurn == 'A'){
                ticTacToeBoard[moves[i][0]][moves[i][1]] = 'X';
                whoseTurn = 'B'; 
            }
            else if (whoseTurn == 'B'){
                ticTacToeBoard[moves[i][0]][moves[i][1]] = 'O';
                whoseTurn = 'A';
            }
        }

        int AWin, BWin; // number of symbols along the specific row / column

        // Check rows for winner
        for (int i = 0; i < 3; i++){
            AWin = 0, BWin = 0;
            for (int j = 0; j < 3; j++){
                if (ticTacToeBoard[i][j] == 'X'){
                    AWin += 1;
                }
                else if (ticTacToeBoard[i][j] == 'O'){
                    BWin += 1;
                }
            }
            if (AWin == 3){
                return "A";
            }
            else if (BWin == 3){
                return "B";
            }
        }

        // Check columns for winner
        for (int j = 0; j < 3; j++){
            AWin = 0, BWin = 0;
            for (int i = 0; i < 3; i++){
                if (ticTacToeBoard[i][j] == 'X'){
                    AWin += 1;
                }
                else if (ticTacToeBoard[i][j] == 'O'){
                    BWin += 1;
                }
            }
            if (AWin == 3){
                return "A";
            }
            else if (BWin == 3){
                return "B";
            }
        }
        
        // Check main diagonal for winner
        AWin = 0, BWin = 0;
        for (int i = 0; i < 3; i++){
            if (ticTacToeBoard[i][i] == 'X'){
                AWin += 1;
            }
            else if (ticTacToeBoard[i][i] == 'O'){
                BWin += 1;
            }
        }
        if (AWin == 3){
            return "A";
        }
        else if (BWin == 3){
            return "B";
        }

        // Check cross diagonal for winner
        AWin = 0, BWin = 0;
        for (int i = 0; i < 3; i++){
            if (ticTacToeBoard[i][2 - i] == 'X'){
                AWin += 1;
            }
            else if (ticTacToeBoard[i][2 - i] == 'O'){
                BWin += 1;
            }
        }
        if (AWin == 3){
            return "A";
        }
        else if (BWin == 3){
            return "B";
        }

        // No winner was found, either there are moves to play, or it's a draw 
        if (moves.size() == 9) {
            return "Draw";
        }
        return "Pending";
    }    
};