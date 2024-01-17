def merge(list1,list2):


    if list1 and list2 is None :
        print("[]")
    result = sorted(list1+list2)
    return result
     


   
            

list1 = [2,3,4]
list2 = [1,1]

print(merge(list1,list2))

