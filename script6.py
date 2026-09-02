import csv
import math

with open("cones.csv","r") as file:
    reader = csv.DictReader(file)
    cones = list(reader)

for cone in cones:
    cone["x"] = float(cone["x"])
    cone["y"] = float(cone["y"])

cones.sort(key=lambda cone: cone["x"] ** 2 + cone["y"] ** 2)

blue=[]
yellow=[]

for cone in cones:
    if cone["colour"] == "blue":
        blue.append(cone)
    else:
        yellow.append(cone)

with open("blue.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "x", "y", "colour"])
    writer.writeheader()
    writer.writerows(blue)

with open("yellow.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "x", "y", "colour"])
    writer.writeheader()
    writer.writerows(yellow)

with open("centreline.csv", "w", newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["x", "y"])

    for b in blue:
        nearest None
        shortest_distance=float("inf")

        for y in yellow:
            distance=(b["x"] - y["x"]) ** 2 + (b["y"] - y["y"]) ** 2

            if distance<shortest_distance:
                shortest_distance=distance
                nearest=y

        mid_x=(b["x"]+nearest["x"])/2
        mid_y=(b["y"]+nearest["y"])/2

        writer.writerow([mid_x, mid_y])
