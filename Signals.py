import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-5, 20, 0.01)


def step(u=1, t0=0):
    n = len(t)
    arr = np.empty(n)

    for i in range(n):
        if t[i] < t0:
            if u == 1:
                arr[i] = 0
            else:
                arr[i] = 1
        else:
            if u == 1:
                arr[i] = 1
            else:
                arr[i] = 0
    return arr


def impulse(u=1, t0=0):
    n = len(t)
    arr = np.empty(n)

    for i in range(n):
        if t[i] == t0:
            if u == 1:
                arr[i] = 1
            else:
                arr[i] = -1
        else:
            arr[i] = 0
    return arr

v1 = 20 * np.exp(-2 * t) * (step() - step(1, 2))
v2 = (10 * (t - 3)) * (step(1, 2) - step(1, 3))
v3 = (-10 * (t - 5)) * (step(1, 3) - step(1, 5))
v4 = (10 * (t - 7)) * (step(1, 5) - step(1, 7))
plt.plot(t, v1, label='v1(t)')
plt.plot(t, v2, label='v2(t)')
plt.plot(t, v3, label='v3(t)')
plt.plot(t, v4, label='v4(t)')
plt.plot(t, np.zeros(len(t)), color='k')
plt.title('Suma de funciones escalón unitario 0<t<7')
plt.xlim(-2, 8)
plt.ylim(-20, 20)
plt.xlabel('t(s)')
plt.ylabel('v(t)')
plt.grid(True)
plt.legend()
plt.show()

der = 20*np.exp(-2 * t)*step() -40*np.exp(-2 * t)*step() +10*(t-3-2*np.exp(-2 * t))*impulse(1,2) +10*(1+4*np.exp(-2 * t))*step(1,2) -20*(t-4)*impulse(1,3) +20*step(1,3) +20*(t-6)*impulse(1,5) +20*step(1,5) -10*(t-7)*impulse(1,7) -10*step(1,7)
plt.plot(t, der, label='Amplitud')
plt.title('Derivada de la suma de funciones escalón')
plt.xlim(-5, 10)
plt.ylim(-25, 60)
plt.xlabel('t(s)')
plt.ylabel('dv(t)/dt')
plt.grid(True)
plt.legend()
plt.show()
