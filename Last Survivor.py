def last_survivor(letters, coords):
    result = list(letters)
    for coord in coords:
        result.pop(coord)
    return ''.join(result)