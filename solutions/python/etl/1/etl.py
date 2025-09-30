def transform(legacy_data):
    clean = {}
    for key, value in legacy_data.items():
        for char in value:
            clean[char.lower()] = key
    return clean