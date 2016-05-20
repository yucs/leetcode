/*
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
*/


func intersection(nums1 []int, nums2 []int) []int {
    //简单通过map 映射，就好了
    nums1map:=make(map[int]bool)
    result:=[]int{}
    for _,num:=range nums1{
        nums1map[num]=true
    }
    
    for _,num2:=range nums2{
        value,ok:=nums1map[num2]
        if ok&&value{
            result=append(result,num2)
        } 
        //避免重复
        nums1map[num2]=false
        
    }
    
    return result
}