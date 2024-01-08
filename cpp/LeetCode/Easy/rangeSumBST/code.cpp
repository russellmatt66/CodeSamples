// https://leetcode.com/problems/range-sum-of-bst/submissions/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        sum_ = 0;
        sum_ += addBST(root, low, high);
        return sum_;
    }

    int addBST(TreeNode* currNode, const int low, const int high){
        if (currNode->left != nullptr){
            sum_ += addBST(currNode->left, low, high);
        }
        if (currNode->right != nullptr){
            sum_ += addBST(currNode->right, low, high);
        }
        if (currNode->val >= low && currNode->val <= high){
            return currNode->val;
        }
        return 0;
    }

    private:
        int sum_;
};
