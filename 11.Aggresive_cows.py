def check(mid,arr,n,c):
    cows=1
    position=arr[0]
    for i in range(1,n):
        if (arr[i]-position)>=mid:
            cows+=1
            position=arr[i]
            if cows==c:
                return True
    return False
def binary_search(arr,n,c):
    l=0
    h=arr[n-1]
    max=-1
    while(l<h):
        mid=int((l+h)/2)
        if check(mid,arr,n,c):
            if mid>max:
                max=mid
            l=mid+1
        else:
            h=mid
    return max
arr=[1,2,4,8,9]
result=binary_search(arr,len(arr),3)
print("cows are placed at a distance of each is:",result)
