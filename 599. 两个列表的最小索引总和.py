def findRestaurant(list1, list2):
    index1 = {list1[i]: i for i in range(len(list1))}
    index2 = {list2[i]: i for i in range(len(list2))}
    agreements = set(list1) & set(list2)
    sum_index = {r: index1[r] + index2[r] for r in agreements}
    return [r for r in agreements if sum_index[r] == min(sum_index.values())]


list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
print(findRestaurant(list1, list2))
