import matplotlib.pyplot as plt
import csv

filename = "" # Path to CSV data file
logarithmic_x_axis = False # Logarithmix X axis for plot


def plot_data(filename, log_scale=False, referance_opacity=1, measurement_opacity=1):
    header = []
    data = []

    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile)

        header = next(csvreader)

        for datapoint in csvreader:
            values = [float(value) for value in datapoint]
            data.append(values)

    time = [p[0] for p in data]
    ch1 = [p[1] for p in data]
    ch2 = [p[2] for p in data]

    plt.plot(time, ch1, "-", color="orange", alpha=referance_opacity)
    plt.plot(time, ch2, "-", color="blue", alpha=measurement_opacity)

    if (log_scale):
        plt.xscale("log")

    plt.xlabel("Endring [dB]")
    plt.ylabel("Frekvens [Hz]")

    plt.legend(["Inngangssignal", "Utgangssignal"], loc="upper right")

    plt.show()

plot_data(filename, logarithmic_x_axis)