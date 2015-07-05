"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
"""
"""
思路：类似快排一次，想象往迟库加水，加满后 从外到里依次拔掉最低的，再加水
"""
class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        end=len(height)-1
        begin=0
        MAX=0
        cur=0
        while(begin<end):
           cur=min(height[begin],height[end])*(end-begin)
           if (cur>MAX):
               MAX=cur
          
           if (height[begin]>height[end]):
               end-=1
           else:
               begin+=1
        
        return MAX
