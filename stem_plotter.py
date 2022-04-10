from matplotlib import pyplot as plt
import numpy as np

a = 0.5
V_0 = 1

x = np.linspace(0, 10, 41)
y = a * V_0 * np.sinc(a * x)

markerline, stemlines, baseline = plt.stem(x, np.abs(y), linefmt="grey", markerfmt="D")
markerline.set_markerfacecolor("none")
plt.xlabel("Fourierkoeffisient [k]")
plt.ylabel("Amplituderespons")
plt.show()