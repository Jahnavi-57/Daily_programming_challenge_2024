def find_missing_number(arr:int)->int:
    n=len(arr)+1
    sum_of_n_numbers=n*(n+1)//2
    array_sum=sum(arr)
    return sum_of_n_numbers-array_sum


arr=[1]
missing_number=find_missing_number(arr)
print(f"Missing Number : {missing_number}")

arr=list(range(1,10000))
missing_number=find_missing_number(arr)
print(f"Missing Number : {missing_number}")
    