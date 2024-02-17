list = []
nums1Sum = 0
nums2Sum = 0

for i in range(-10, 20):
    list.append(i)

for i in list:
    if i <= 1:
        nums1Sum += i
    elif 3 < i < 8:
        nums2Sum += i

print(nums1Sum - nums2Sum)
