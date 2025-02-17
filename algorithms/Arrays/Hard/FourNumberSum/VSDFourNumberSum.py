def VSDuserinput():
    n=int(input("Enter the number of elements (>4):"))
    arr=list(map(int,input("Enter the elements in array:").split()))
    target=int(input("Enter the target:"))
    arr.sort()
    print(ksum(arr,target,4))

def twosum(arr,target):
    res=[]
    low,high=0,len(arr)-1

    while low<high:
        cursum=arr[low]+arr[high]
        if cursum<target or (low>0 and arr[low]==arr[low-1]):
            low+=1
        elif cursum>target or (high<len(arr)-1 and arr[high]==arr[high+1]):
            high-=1
        else:
            res.append([arr[low],arr[high]])
            low+=1
            high-=1
    return res


def ksum(arr,target,k):
    res=[]
    if not arr:
        return res
    
    avg=target//k

    if avg<arr[0] or avg>arr[-1]:
        return res
    
    if k==2:
        return twosum(arr,target)
    for i in range(len(arr)):
        if i==0 or arr[i-1]!=arr[i]:
            for s in ksum(arr[i+1:],target-arr[i],k-1):
                res.append([arr[i]]+s)
    return res

if __name__=="__main__":
    VSDuserinput()