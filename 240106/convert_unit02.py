def radians(i):
    import math
    result = i * math.pi / 180
    return result

def degree(i):
    import math
    result = i * 180 / math.pi
    return result

if __name__ == '__main__':
    print(radians(50))