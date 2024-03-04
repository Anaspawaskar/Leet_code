def merge(list1,list2):


    if list1 and list2 is None :
        print("[]")
    result = sorted(list1+list2)
    return result 

list1 = [12,34,23,11]
list2 = [10,9,14]

print(merge(list1,list2))

