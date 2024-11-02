def merge_two_lists(l1, l2):
    merged = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            merged.append(l1[i])
            i +=1
        else:
            merged.append(l2[j])
            j +=1
    while i < len(l1):
        merged.append(l1[i])
        i +=1
    while j < len(l2):
        merged.append(l2[j])
        j +=1
    return merged

def merge_k_lists(lists):
    if not lists:
        return []
    while len(lists) > 1:
        merged_lists = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            if i + 1 < len(lists):
                l2 = lists[i + 1]
                merged_lists.append(merge_two_lists(l1, l2))
            else:
                merged_lists.append(l1)
        lists = merged_lists
    return lists[0]

def main():
    sorted_lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    print("Sorted lists:", sorted_lists)
    merged_list = merge_k_lists(sorted_lists)
    print("Merged list:", merged_list)

    print()

    sorted_lists = [[], [1], [0, 2, 2], [3, 3, 3]]
    print("Sorted lists:", sorted_lists)
    merged_list = merge_k_lists(sorted_lists)
    print("Merged list:", merged_list)

if __name__ == "__main__":
    main()
