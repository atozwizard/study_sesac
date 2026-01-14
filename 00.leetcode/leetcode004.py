"""Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # sum=[]
        # median = []
        # sum = (nums1 + nums2 병합)
        # 각 값의 합 / 인덱스 수 = median
        # print median
        """틀린 접근, 중앙값의 이해가 필요. 위는 median 중앙값이 아닌
average 평균을 구하는 공식임. 
    평균  모든 숫자를 더해 개수로 나눈 값
    중앙값  숫자들을 크기순으로 나열했을 떄 정가운데에 위치한 값.
    예시, [1,2,100]
        평균 (1+2+100)/3=34.33
        중앙값 정가운데 숫자인 2
    따라서 단순히 합치기만 해서는 안되고 반드시 크기순으로
    정렬된 상태에서 가운데를 찾아야 함"""
    #두 배열 병합.정렬
        combined = sorted(nums1 + nums2)
        n= len(combined)
        # 중앙값찾기(개수가 홀짝에 따라 다름)
        if n % 2 == 1: #홀수면 가운데값
            median = combined[n //2]
        else: # 짝수면 가운데 두 값의 평
            median = (combined[n//2 -1] +combined[n//2]) /2

        return float(median)