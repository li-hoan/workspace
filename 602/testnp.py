import numpy as np

print("使用列表生成数组")
data = [[1,2,3,4,5],[1,2,3,4,5]]
x = np.array(data)
print(x)
print(type(x))
print(x.dtype)
print(x.shape)
print(x.ndim)
print(x.size)

print("zero/one/empty")
x = np.zeros((2,3),dtype=np.int8)
print(x)
print(x.dtype)
x = np.empty((2,3))
print(x)
x = np.ones((2,3))
print(x)

print('使用arange生成连续元素')
print(np.arange(6))
a = np.arange(20)
print(a)
a = a.reshape(4,5)
print(a)


print('使用astype复制数组，并改变类型')
x = np.array([1,2,3,4,5],dtype=np.float64)
y = x.astype(np.int8)
print(x)
print(y)

print("将字符类型的元素转为数值元素")
x = np.array(['1','2','3','4'])
x = x.astype(np.int8)
print(x)

print('使用其他数组的元素的数据类型作为参数')
x = np.array([1,2,3,4],dtype=np.float64)
y = np.array([1,2,3],dtype=np.int8)
print(y)
print(y.astype(x.dtype))

print('ndarray的运算')
x = np.array([1,2,3])
print(x*2)
print(x>2)

print('ndarray的基本索引')
x = np.array(([[1,2],[3,4],[5,6]]))
print(x[0])
print(x[0][1])
print(x[0,1])

x = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(x.shape)
print(x[0])
print(x[0][1])
print(x[0,1])
print(x[0,1,1])

y = x[0].copy()#生成一个副本
z = x[0]#未生成副本
print(y)
y[0,0]=9
z[0,0]=9
print(x)

print('ndarray的切片')
x = np.array([1,2,3,4])
print(x[1:3])
print(x[:3])
print(x[1:x.size])
print(x[:])
print(x[0:4:2])


x = np.array([[1,2],[3,4],[5,6]])
print(x[:2,:1])
x[:2,:1]=9
print(x)

print('ndarray的布尔索引')
x = np.array([3,2,3,1,3,0])
y = np.array([True,False,True,True,False,False])
print(x[y])
print(x[y==False])
print(x[~(x>2)])

print('ndarray的数组索引')
x  = np.array([1,2,3,4,5,6,7])
print(x[[0,1,2]])
print(x[[-1,-2,-3]])

x = np.array([[1,2],[3,4],[5,6]])
print(x[[0,1]])
print(x[[0,1],[0,1]])
print(x[[0,1]][:,[0,1]])


print('ndarray的轴')
x = np.arange(8).reshape((2,4))
print(x)

#转置
print(x.T)
#矩阵乘法
print(np.dot(x,x.T))

k = np.arange(24).reshape(2,3,4)
print(k)
print(k[0][1][0])

#轴变换
k = k.transpose((1,0,2))
print(k.shape)
# print(k)
#轴交换
k = k.swapaxes(0,2)
print(k.shape)

print("numpy的统计")
x = np.array([[1,2],[3,4],[5,6]])
print(x.shape)
print(x.mean())
print(x.mean(axis=1))
print(x.mean(axis=0))
print(x.sum())
print(x.sum(axis=1))
print(x.max())

print('where函数')
x = np.array([1,2,3,4,5,6])
x = np.where(x>2,4,5)
print(x)


print('ndarray的存取')
x = np.array([[1,2,4],[3,4,5],[6,5,4]])
np.save('file',x)#以二进制形式，npy保存
y = np.load('file.npy')
print(y)

print('矩阵求逆')
x = np.array([[1,1],[1,2]])
y  = np.linalg.inv(x)
print(y)
print(x.dot((y)))

print('numpy中的随机')
x = np.random.randint(0,2,10)
print((x>0).sum())