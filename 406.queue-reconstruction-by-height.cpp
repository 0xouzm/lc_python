/*
 * @lc app=leetcode id=406 lang=cpp
 *
 * [406] Queue Reconstruction by Height
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        
        sort(people.begin(),people.end(),[](vector<int>h, vector<int>k){
            if(h[0] == k[0]) return h[1] < k[1];
            return h[0] > k[0];
        });
        list<vector<int>> que;
        int len = people.size();
        for(int i = 0; i< len; ++i){
            list<vector<int>>::iterator it = que.begin();
            int position = people[i][1];
            while(position--){
                it ++;
            }
            que.insert(it, people[i]);
        }
        return vector<vector<int>>(que.begin(), que.end());

    }
};
// @lc code=end

