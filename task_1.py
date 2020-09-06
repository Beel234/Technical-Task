def sumArray(arr):
    newArray = [0,0]
    for num in arr:
        if num%2 == 0:
            newArray[0] += num
        else:
            newArray[1] +=num
    return newArray

out = sumArray([1,2,3,6,9])
print(out)