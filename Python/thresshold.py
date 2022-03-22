import copy

arr = [1, 5, 5, 1]
result = []

def calculateCost(arr, threshold):
    temp = sum(arr[0:threshold])
    left = []
    right = []
    index = 0
    if threshold < len(arr):
        for i in range(1,len(arr)-threshold+1):
            if temp < sum(arr[i:i+threshold]):
                temp = max(arr[i:i+threshold])
                index = i
        left = copy.deepcopy(arr[0:index])
        right = copy.deepcopy(arr[index+threshold:])
        return calculateCost(left,threshold) + calculateCost(right,threshold) + temp
    elif len(arr) == 0:
        return 0
    else:
        return max(arr)

print(calculateCost(arr,2))
