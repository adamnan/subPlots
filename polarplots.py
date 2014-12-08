#!/usr/bin/env python

import numpy as np
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt

x = np.arange(-np.pi, np.pi, np.pi/100)
y1 = np.sin(x)
y2 = np.sin(x) ** 2
y3 = np.cos(x)

plt.subplot(1, 2, 1)

plt.plot(x, y1, label = "y = sin(x)")
plt.plot(x, y2, 'r', label = "y = sin(x)^2")
plt.plot(x, y3, 'g', label = "y = cos(x)")

plt.legend()

plt.subplot(1, 2, 2, polar = True)

plt.plot(x, y1, label = "y = sin($\Theta$)")
plt.plot(x, y2, 'r', label = "y = sin($\Theta$)^2")
plt.plot(x, y3, 'g', label = "y = cos($\Theta$)")

plt.legend()

plt.suptitle("Trigonometric functions")
plt.savefig("AdamsGraph.pdf")