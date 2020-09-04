import math 
# Function for calculating standard deviation
def standardDeviation(a, n): 
    # Compute mean (average of the numbers) 
    sum = 0
    for i in range(0 ,n): 
        sum += a[i] 
    mean = sum /n  
    # Finding the differences of the mean and square the sum. 
    squaredDiff = 0
    for i in range(0 ,n): 
        squaredDiff += ((a[i] - mean)  
                * (a[i] - mean)) 
    return math.sqrt(squaredDiff / n) 
  

# Driver Code 
arr = [10, 20, 30, 40, 100] 
n = len(arr) 
print("Standard Deviation: ", int(standardDeviation(arr, n))) 
print("Standard Deviation in 4 decimal places: ", round(standardDeviation(arr, n), 4))
