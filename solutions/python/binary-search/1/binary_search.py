def find(search_list, value):
    high = len(search_list)- 1
    low = 0
    
    while low <= high:
        mid = (high + low)//2
        if search_list[mid] == value: return mid
        elif search_list[mid] < value: low = mid + 1
        else: high = mid - 1
    raise ValueError("value not in array")
    
