import math
def dist(x1, y1, x2, y2):
    d1 = math.pow((x2 - x1), 2)
    d2 = math.pow((y2 - y1), 2)
    return math.sqrt(d1 + d2)

print(dist(5,5,-5,-5))