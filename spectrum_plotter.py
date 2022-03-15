import matplotlib.pyplot as plt
import csv

header = []
data = []

filename = "" # Path to CSV data file


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