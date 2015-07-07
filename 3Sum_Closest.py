"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
    
  """
  #之前没想到快排的夹逼方式，可是性能还是不行~~ 
  #想了半天还是没有动态方式可以高效解决的？
  class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        nums.sort()
        nlen=len(nums)
        result=0
        if(nlen<=3):
            for i in range(nlen):
                result+=nums[i]
            return result
            
        summax=nums[nlen-1]+nums[nlen-2]+nums[nlen-3]
        summin=nums[0]+nums[1]+nums[2]
        if(target>summax):
            return summax
        elif (target<summin):
            return summin
        
        closer=nums[0]+nums[1]+nums[2]-target
        for i in range(nlen-2):
             curcloser=self.twocloser(nums[i+1:nlen],target-nums[i])
             if(abs(curcloser)<abs(closer)):
                 closer=curcloser
                 
        return closer+target
        
    def twocloser(self,nums,target):
          closer=nums[0]+nums[1]-target
          b=1
          e=len(nums)-1
          while(b<e):
              if (closer==0):
                  return 0
              tmp=nums[b]+nums[e]-target
              if(abs(tmp)<abs(closer)):
                   closer=tmp
              if (tmp>0):
                   e-=1
              else:
                  b+=1
          return closer
