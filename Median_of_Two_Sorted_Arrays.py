class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        len1=len(nums1)
        len2=len(nums2)
        mid=(len2+len1)/2+1
        flag=(len1+len2+1)%2
        tag=(len1+len2)/2 %2
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
