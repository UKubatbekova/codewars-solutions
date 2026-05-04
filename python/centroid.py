# https://www.codewars.com/kata/58811e9cfd05cb5aed0000a4/train/python

def centroid(points: list[list[float]]) -> list[float]:
    lst = []
    x = []
    y = []
    z = []
    for i in range(len(points)):
        x.append(points[i][0])
        y.append(points[i][1])
        z.append(points[i][2])
    lst.append(sum(x) / len(x))
    lst.append(sum(y) / len(y))
    lst.append(sum(z) / len(z))
    return lst