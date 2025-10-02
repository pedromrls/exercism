def flatten(iterable):
    flatten_list = []
    stack = iterable.copy()

    while stack:
        value = stack.pop(0)
        if isinstance(value, list): stack[0:0] = value
        elif value is None : continue
        else: flatten_list.append(value)
    return flatten_list
        