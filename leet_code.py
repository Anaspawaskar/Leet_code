def func(num,target):
    for number in range(len(num)):
        for number2 in range(number +1 , len(num)):
            if num[number] + num[number2] == target:
                print(number, number2)
#example 1         
# nums1 = [2, 7, 11, 15]
# target = 9
# print(func(num= nums1 , target= target))

# example2
# nums2 = [8,5,4]
# target2 = 12
# print(func(num= nums2 , target= target2))

# wxample 3
# num3 = [1,2,1,1,1]
# target3 = 3
# print(func(num=num3,target = target3))

