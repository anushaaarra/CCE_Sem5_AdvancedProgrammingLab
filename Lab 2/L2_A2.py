def custom_union(list1, list2):
    result = list1[:]
    for item in list2:
        if item not in result:
            result.append(item)
    return result

def custom_intersection(list1, list2):
    result = []
    for item in list1:
        if item in list2:
            result.append(item)
    return result

def custom_difference(list1, list2):
    result = []
    for item in list1:
        if item not in list2:
            result.append(item)
    return result

list1 = [int(x) for x in input("Enter elements of list 1 ").split()]
list2 = [int(x) for x in input("Enter elements of list 2 ").split()]

union_result = custom_union(list1, list2)
intersection_result = custom_intersection(list1, list2)
difference_result = custom_difference(list1, list2)

print("Union:", union_result)
print("Intersection:", intersection_result)
print("Difference:", difference_result)
