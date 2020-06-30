import matplotlib.pyplot as plt

#实时画画
ax = []
ay = []
plt.ion()
for i in range(100):
    ax.append(i)
    ay.append(i**2)
    #清除
    plt.clf()
    # plt.plot(ax,ay)#画折线图
    plt.scatter(ax,ay,c ="r",marker="v")
    plt.pause(1)

plt.ioff()
plt.show()