from noise import pnoise2
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
a = 1000
b = 1000
base = 200
offset = 0.5
A = [[pnoise2(i/a*4, j/b*4, octaves = 4, persistence=0.4, lacunarity=2.0, base = base) + offset for i in range(a)] for j in range(b)]
pi = 3.14
counter = 0

fig = plt.figure(figsize = (10,10))

def updatefig(*args):
    global counter, A
    counter += 1
    #fig = plt.figure(figsize = (10,10))
    ax1 = plt.subplot(2,2,1)
    ax1.plot(A[0], animated = True)
    ax2 = plt.subplot(2,2,2, projection = 'polar')
    ax2.plot([i/a*pi*2 for i in range(a)], A[0])
    return plt.show(),



ani = animation.FuncAnimation(fig, updatefig, interval=10, blit=True)
plt.show()