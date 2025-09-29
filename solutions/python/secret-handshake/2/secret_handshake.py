ACTIONS = ("reverse","jump","close your eyes","double blink", "wink")

def commands(binary_str):
    secret_handshake = []
    for num in range(4, 0, -1):
        if binary_str[num] == '1': secret_handshake.append(ACTIONS[num])
    if binary_str[0] == '1': secret_handshake.reverse()
    return secret_handshake
