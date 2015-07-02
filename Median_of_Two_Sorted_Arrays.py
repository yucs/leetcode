"""
There are two sorted arrays nums1 and nums2 of size m and n respectively. 
Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
"""
 #思路：就是回归排序，但是就用循环队来保存2位 来计算即可。
 #==_==！最初尝试类似半查找方法，考虑情况太多，后面思路有些乱了，ps: 感觉可行，待思考。。
class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        len1=len(nums1)
        len2=len(nums2)
        mid=(len2+len1)/2+1
        #就是标记是双还是单
        flag=(len1+len2+1)%2
        # 报错后发现的，主要轮询问题：eg: 1,3,5,7,9 如果：只有3位的话，3在que[1]上，而当5位的话，5在que[0]。
        tag=(len1+len2)/2 %2
        #
        que=[0,0]
        cur=cur1=cur2=0
       
        while(cur1<len1 and cur2<len2 and cur < mid):
            if(nums1[cur1]<nums2[cur2]):
                que[cur%2]=nums1[cur1]
                cur1+=1
            else:
                que[cur%2]=nums2[cur2]
                cur2+=1
            cur+=1
        
        if(cur >= mid):
            if flag==1:
                return (que[0]+que[1])/2.0
            else:
                return que[tag]
                    
            
        if(cur1>=len1):
            while(cur < mid):
                que[cur%2]=nums2[cur2]
                cur2+=1
                cur+=1
        else:
            while(cur < mid):
                que[cur%2]=nums1[cur1]
                cur1+=1
                cur+=1
                
        if flag==1:
                return (que[0]+que[1])/2.0
        else:
                return que[tag] 
