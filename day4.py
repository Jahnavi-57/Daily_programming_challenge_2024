def merge_sorted_arrays(arr1,arr2):
    m=len(arr1)
    n=len(arr2)
    left=m-1
    right=0
    while(left>=0 and right<n):
        if (arr1[left]>arr2[right]):
            temp=arr1[left]
            arr1[left]=arr2[right]
            arr2[right]=temp
            left-=1
            right+=1
        else:
            break
    arr1.sort()
    arr2.sort()
    return arr1,arr2

arr1=[12,3]
arr2=[2,3,4,5,6,7,100,8,9,10]
a,b=merge_sorted_arrays(arr1,arr2)
print(f"Sorted Arrays:\narr1: {a}\narr2: {b}")

#Time Complexity: For swapping elements to correct sides(either to left(arr1) or right(arr2)):O(min(m,n))
#                 sorting arr1:O(mlogm)
#                 sorting arr2:O(nlogn)
#  Total: O(min(m,n))+O(m logm)+O(n logn)
#Space complexity: since no extra space is used,it is constant time complexity.O(1)