"""
суть задачи мне понятна, 
единственное что доставляет сложности это 
работа с внешними файлами и выборкой из них данных
"""

data = []
with open("task2/circle.txt") as f:
    for line in f:
        data.append([int(x) for x in line.split()])
# print(data)

cx = data[0][0]
cy = data[0][1]
r = data[1][0]

data2 = []
file = open("task2/dot.txt", "r")
lines = file.readlines()
for line in lines:
    data2.append([int(x) for x in line.split()])
# print(data2)


def includes(px, py, cx = cx, cy = cy, r = r):
    return (px - cx) ** 2 + (py - cy) ** 2 < r ** 2

included_points = 0


"""
постараюсь доразобрать с этим моментом, если не смогу то коммент останется :(
весьма печально, сломаться на столь тривиальной задаче
"""
for p, r in data2:
    px = data[0][0]
    py = data[0][1]
    p += 1
    r += 1
included_points += includes(px, py)

print(included_points)