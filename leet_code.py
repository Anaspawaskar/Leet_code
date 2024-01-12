def two_sum(num,target):
    """creating a function which fecth numbers from list to reach the target

    Args:
        num (list): numbers present in list 
        target (int): a number 

    Returns:
        _type_: index number of the numbers 
    """
    for index1 in range(len(num)):

        for index2 in range(index1 +1 , len(num)):

            if num[index1] + num[index2] == target:
                return index1, index2
            

# example 1         
nums1 = [2, 7, 11, 15]
target = 9
print(two_sum(num= nums1 , target= target))

# example2
nums2 = [8,5,4]
target2 = 9
print(two_sum(num= nums2 , target= target2))

# example 3
num3 = [1,2,1,1,1]
target3 = 3
print(two_sum(num=num3,target = target3))

