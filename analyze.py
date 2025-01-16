import numpy as np
import matplotlib.pyplot as plt
LlegSV=np.load("data/LlegSV.npy")
simulation_steps=500
LlegSV = LlegSV[:simulation_steps]
plt.plot(LlegSV, 'o', markersize = 1, label = "Left leg")
plt.xlim(0,simulation_steps)
plt.ylim(-1.5,1.5)
plt.xlabel("Simulation Step")
plt.ylabel("Touch Sensor Value")
plt.title("Left Leg Touch Sensor Values Over time")
plt.legend()
plt.show()