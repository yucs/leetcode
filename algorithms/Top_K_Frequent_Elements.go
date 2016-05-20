/*
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

*/


func topKFrequent(nums []int, k int) []int {
    //第一反应：通过map统计数据先，再堆排序 排出前k个元素就好了（问题：堆排序复杂..）
    //堆排序改为一个数据，找到最小的并替换

    numsmap:=make(map[int]int)
    //counts 频率...
    counts:=make([]int,k)
    result:=make([]int,k)
    
    for _,num:=range nums{
        value,ok:=numsmap[num]
        if !ok{
            numsmap[num]=1
        }else{
            numsmap[num]=value+1
        }
    }
    
    lowestcount:=counts[0]
    lowestpoint:=0
    
    for key,value:=range numsmap{
        
        if value <= lowestcount{
            continue
        }
        //result用最小值替代掉
        counts[lowestpoint]=value
        result[lowestpoint]=key
        lowestcount = value
        //重新获得最小值指针
        for i:=0;i<k;i++{
            if counts[i]<lowestcount{
                lowestpoint=i
                lowestcount=counts[i]
            }
        }

      }
    
    return result
        
 }