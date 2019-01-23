import numpy as np
import time
# a = np.array([1,2,3])
# print(a)
#
# b = np.array([[1,2,3],[4,5,6]])
# print(b)
# print(b.shape)
#
# a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(a)
#
# row_r0 = a[0,:]
# print(row_r0)
# row_r1 = a[1,:]
# print(row_r1)
#
# b = np.array([1,2,3,4])
# c = [1,2,3,4]
#
# print(b[0:2])
# print(c[0:2])
#
# print(type(b))
# print(type(c))
# print(type(a))
#
# a = np.array([[1,2],[3,4],[5,6],[7,8]])
#
# bool_idx = (a>2)
# print(bool_idx)
# print(a[bool_idx])
# print(a[a>2])
#
# e = [1,2,3,4,5,6,7,8]
# print(e[e>2])

# start = time.time()
# print(start)
# x = np.array([[1,2],[3,4]],dtype=np.float64)
# print(x)
# y = np.array([[5,6],[7,8]],dtype=np.float64)
# print(y)
# print(x+y)
# end = time.time()
# print(end)
# elapsed = end-start
# print(elapsed)
#
# print()
#
# start = time.time()
# print(start)
# x = [[1,2],[3,4]]
# # print(x)
# y = [[5,6],[7,8]]
# # print(y)
# print([[x[0][0]+y[0][0],x[0][1]+y[0][1]],[x[1][0]+y[1][0],x[1][1]+y[1][1]]])
# end = time.time()
# print(end)
# elapsed = end-start
# print(elapsed)

start = time.time()
x = np.array([[1,2],[3,4]],dtype=np.float64)
y = np.array([[5,6],[7,8]],dtype=np.float64)
print(np.multiply(x,y))
end = time.time()
print(end-start)

print("------------------------------------------------------")

start = time.time()
v = [[1,2],[3,4]]
w = [[5,6],[7,8]]
print([v[0][0]*w[0][0],v[0][1]*w[0][1]],[v[1][0]*w[1][0],v[1][1]*w[1][1]])
end= time.time()
print(end-start)

print("------------------------------------------------------")

a = np.array([9,10])
b = np.array([11,12])

dot_1_result = np.dot(a,b)
print(dot_1_result)

dotresult = np.dot(x,y)
print(dotresult)

print("------------------------------------------------------")

n = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
u = np.array([0,2,0,1])
idx = np.arange(4)
print(idx)
print(n[np.arange(4),u])


print("------------------------------------------------------")

start = time.time()
x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
v = np.array([1,0,1])
empty_start= time.time()
y = np.empty_like(x)
empty_end = time.time()
for i in range(x.shape[0]):
    y[i,:]=x[i,:]+v

print(y)
end = time.time()
print("empty_list: "+str(empty_end-empty_start))
print(end-start)


print()

start = time.time()
x = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
v = [1,0,1]
empty_start= time.time()
y = [[0 for i in range(len(x[0]))] for j in range(len(x))]
empty_end= time.time()
for i in range(len(x)):
    for j in range(len(x[0])):
        y[i][j] = x[i][j]+v[j]

print(y)
end = time.time()
print("empty_list: "+str(empty_end-empty_start))
print(end-start)


print()





start = time.time()
x = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
v = [1,0,1]
# y = [[0 for i in range(len(x[0]))] for j in range(len(x))]
empty_start= time.time()
for i in range(len(x)):
    for j in range(len(x[0])):
        y[i][j] = 0
empty_end= time.time()
for i in range(len(x)):
    for j in range(len(x[0])):
        y[i][j] = x[i][j]+v[j]

print(y)

end = time.time()
print("empty_list: "+str(empty_end-empty_start))
print(end-start)





















