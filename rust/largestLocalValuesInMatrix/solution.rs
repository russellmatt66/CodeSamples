// https://leetcode.com/problems/largest-local-values-in-a-matrix/submissions/
impl Solution {
    pub fn largest_local(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut maxLocal: Vec<Vec<i32>> = vec![vec![0; grid[0].len()-2]; grid.len()-2];
        for i in 1..=(grid.len()-2){ 
            for j in 1..=(grid[0].len()-2){
                maxLocal[i-1][j-1] = Solution::findMax(&grid,i,j);
            }
        }
        maxLocal
    }
    // 3x3 stencil
    fn findMax(grid: &Vec<Vec<i32>>, i: usize, j: usize) -> i32 {
        // i,j != 0
        // i,j != grid.size()
        let mut max: i32 = 0;
        for k in (i-1)..=(i+1){
            for l in (j-1)..=(j+1){
                if max < grid[k][l] {
                    max = grid[k][l];
                }
            }
        }
        max
    }
}