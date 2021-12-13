import numpy as np

#x = np.random.random((100, 100)) + 54
#x = (m := np.random.random((100, 100))) + 54
#print(m)

m = [np.random.random((100, 100)) for _ in range(10)]
d = [det for matrix in m if (det := np.linalg.det(matrix)) > 0]
print(d)
