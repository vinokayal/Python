def First_Search(arr,testVariable,CurrentIndex):
    if CurrentIndex==len(arr):
        return CurrentIndex

    if arr[CurrentIndex]==testVariable:
        return CurrentIndex

    return First_Search(arr,testVariable,CurrentIndex+1)


arr=[10,20,12,15,22,44,23]
testVariable=22
CurrentIndex=0

print(First_Search(arr,testVariable,CurrentIndex))