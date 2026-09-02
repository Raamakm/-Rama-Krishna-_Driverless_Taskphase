def sort_points(points, reference):
    x,y=reference
    points.sort(key=lambda point: (point[0] x) ** 2 + (point[1] y) ** 2)
    return points

points = [(0, 1), (0, 3), (1, 2)]
reference = (0, 0)

print(sort_points(points, reference))
