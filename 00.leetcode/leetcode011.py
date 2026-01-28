"""You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        #return 인덱스간 거리 * 둘 중 작은 축의 높이
        #i,j 투포인터
        #
        #현재넓이와 최대넓이를 비교해서 최대값을 리턴
        n = len(height)
        i = 0
        j = n-1
        wd = 0
        # if not (n == height.length and 2 <= n <=10**5 and 0<= height[i] <=10**4):
        #     return 0

        # while (i and j) in len(height):
        while i < j:
            # i < j
            curr_wd = (j -i) * min(height[i],height[j])
            wd = max(wd, curr_wd)
            if height[i] < height[j]:
                i += 1
            # elif height[i] > height[j]:
            else:
                j -= 1
            
            
            # return wd
        return wd

