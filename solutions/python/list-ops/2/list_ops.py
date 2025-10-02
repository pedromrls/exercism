def append(list1, list2):
    return [*list1, *list2]


def concat(lists):
    return [el for arr in lists for el in arr]


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    return sum(1 for item in list)


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    while list:
        initial = function(initial, list.pop(0))
    return initial
    
def foldr(function, list, initial):
    while list:
        initial = function(initial, list.pop())
    return initial


def reverse(list):
    return list[::-1]
