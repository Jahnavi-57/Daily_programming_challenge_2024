from collections import Counter
def find_duplicate(array):
    d=Counter(array)
    res=0
    for k in d.keys():
        if d[k]==2:
            res=k
    return res
arr=[3, 1, 3, 4, 2]
result=find_duplicate(arr)
print(f"The duplicate present in the array {arr} is: {result}")