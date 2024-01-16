def merge(list1,list2):
    result = []


    if list1 and list2 is None :
        print("[]")
    op = sorted(list1+list2)
    result.append(op)
    return result
     


   
            

list1 = [1,2,3]
list2 = [2,4,5]

print(merge(list1,list2))

