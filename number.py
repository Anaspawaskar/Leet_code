num1 = (input("number 1:"))
num2 = (input("number 2:"))

def number(num1, num2):
    """_summary_

    Args:
        num1 (int): taking number
        num2 (int): taking number
    """

    l1 = []
    l2 = []

    l1.append(num1[::-1])
    l2.append(num2[::-1])

    print(l1,l2)

    for numbers in l1:
        for numbers1 in l2 :
                list1 = None
                list2 = None

                list1.append(numbers)
                list2.append(numbers1)

                print(list1,list2)

    

    

number(num1,num2)


