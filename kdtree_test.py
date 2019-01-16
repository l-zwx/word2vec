import kdtree
emptyTree = kdtree.create(dimensions=3)
point1 = (2, 3, 4)
point2 = [4, 5, 6]
point3 =(5, 3, 2)
tree = kdtree.create([point1, point2, point3])
a = tree.search_knn(point=(1, 2, 3),k= 2)#寻找最近点  返回k个最近的点
print(a)