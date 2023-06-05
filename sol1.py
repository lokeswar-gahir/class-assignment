def sol1(arr):
    for _ in range(arr.count(0)):
        arr.remove(0)
        arr.append(0)


nums = [0,1,0,3,12]
sol1(nums)
print("Example 1:",nums)

nums2 = [0,5,7,0,0,4,1]
sol1(nums2)
print("Example 2:",nums2)