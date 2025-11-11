def append(list1, list2):
    return list1 + list2


def concat(lists):
    concatenated_list = []
    for list in lists:
        concatenated_list.extend(list)
    return concatenated_list


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    return sum(1 for item in list)


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    value = initial
    for el in list:
        value = function(value, el)
    return value

def foldr(function, list, initial):
    value = initial
    for el in reverse(list):
        value = function(value, el)
    return value


def reverse(list):
    return list[::-1]
