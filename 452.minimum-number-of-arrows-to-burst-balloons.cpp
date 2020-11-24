/*
 * @lc app=leetcode id=452 lang=cpp
 *
 * [452] Minimum Number of Arrows to Burst Balloons
 */

// @lc code=start
class Solution {
public:
    int findMinArrowShots(vector <vector<int>> &points) {
        if (points.empty()) return 0;
        int n = points.size() + 1;
        sort(points.begin(), points.end(), [](vector<int> &o1, vector<int> &o2) {
            return o1[1] < o2[1];
        });
        int prev = points[0][1];
        for (auto p: points) {
            if (p[0] <= prev) {
                n--;
            } else {
                prev = p[1];
            }
        }
        return n;
    }
};
// @lc code=end

