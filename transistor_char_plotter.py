import matplotlib.pyplot as plt
from tkinter import filedialog
import numpy as np
import tkinter
import random
import csv
import os

V_t = 2
K = 2
V_dd = 8
R_d = 0.5 * 10 ** 3

V_gs_MIN = 2
V_gs_MAX = 9
V_gs_STEP_DISTANCE = 1

if not V_gs_STEP_DISTANCE == 1:
    V_gs_steps = round((V_gs_MAX - V_gs_MIN) / V_gs_STEP_DISTANCE) + 1
else:
    V_gs_steps = V_gs_MAX - V_gs_MIN + 1


# V_gs = np.linspace(V_gs_MIN, V_gs_MAX, V_gs_steps)
# x = np.linspace(0, 10, 1000)
V_gs = 4


# I_d = K / 2 * (V_gs - V_t) ** 2

def I_d(V_gs):
    return K / 2 * (V_gs - V_t) ** 2

# # V_ds = V_dd - I_d * R_d
def V_ds(x):
    return V_dd - I_d(x) * R_d

# for i in V_gs:

# V_ds = np.linspace(0, 10, 1000)

plt.plot(V_ds(V_gs), I_d(V_gs), "-", alpha=1)
    

plt.show()