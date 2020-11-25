/*
 * @lc app=leetcode id=763 lang=cpp
 *
 * [763] Partition Labels
 */

// @lc code=start
class Solution {
public:
    vector<int> partitionLabels(string S) {
        vector<int> res;
        int last[26];

        for (int i = 0; i < S.size(); i++) {
            last[S[i] - 'a'] = i;
        }

        int a = 0, b = 0;
        for (int i = 0; i < S.size(); i++) {
            b = max(b, last[S[i] - 'a']);
            if (b == i) {
                res.push_back(b - a + 1);
                a = i + 1;
            }
        }
        return res;
    }
};
// @lc code=end
