import matplotlib.pyplot as plt
from tkinter import filedialog
import tkinter
import csv
import os

header = []
data = []

root = tkinter.Tk()
root.withdraw()

filename = "" # Path to CSV data file

if not filename:
    filename = filedialog.askopenfilename(initialdir="/", title="Please select a directory", filetypes=(("CSV files", "*.csv*"), ("All files", "*.*")))

with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)

    header = next(csvreader)

    for datapoint in csvreader:
        values = [float(value) for value in datapoint]
        data.append(values)

frequency = [p[0] for p in data]
ref_voltage = [p[1] for p in data]
# voltage_change = [p[3] for p in data]


plt.plot(frequency, ref_voltage, "-", color="orange", alpha=0.85)
# plt.plot(frequency, voltage_change, "-", color="blue")

plt.xlabel("Frekvens [Hz]")
plt.ylabel("Amplituderespons [dB]")

plt.legend(["Inngangsignal", "Utgangssignal"], loc="upper right")

plt.show()