/*
 * @lc app=leetcode id=605 lang=cpp
 *
 * [605] Can Place Flowers
 */

// @lc code=start
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        if(n == 0){
            return true;
        }
        int size = flowerbed.size(); //7
        if(size==1 && flowerbed[0]== 0){
            return true;
        }
        if(flowerbed[0] ==0 && flowerbed[1]==0){
            flowerbed[0] = 1;
            --n;
        }
        for (int i = 1; i < size - 1; ++i)
        {
            if(flowerbed[i - 1] == 0 && flowerbed[i] == 0 && flowerbed[i+1] == 0){
                flowerbed[i]=1;
                --n;
            }
        }
        if (flowerbed[size - 1] == 0 && flowerbed[size - 2] == 0){
            --n;
        }
        return n <= 0;
        

    }
};
// @lc code=end

