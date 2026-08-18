class Solution {
public:
    void find_combination(int index, vector<int>& candidates, int target, vector<int>& temp, vector<vector<int>>& returnable){
        if (index == candidates.size()) return;
        if (target < 0) return;
        if (target == 0){
            returnable.push_back(temp);
            return;
        }

        temp.push_back(candidates[index]);
        find_combination(index, candidates, target - candidates[index], temp, returnable);

        temp.pop_back();
        find_combination(index + 1, candidates, target, temp, returnable);
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> returnable;
        vector<int> temp;

        find_combination(0, candidates, target, temp, returnable);
        return returnable;
    }
};