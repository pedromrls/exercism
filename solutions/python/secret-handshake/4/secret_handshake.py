ACTIONS = ('wink', 'double blink', 'close your eyes', 'jump')

def commands(binary_str):
    number = int(binary_str, 2)
    secret_handshake = []
    for index, code in enumerate(ACTIONS):
        if number & 1 << index: secret_handshake.append(code) 
    if number & 1 << 4: secret_handshake.reverse()
    return secret_handshake
