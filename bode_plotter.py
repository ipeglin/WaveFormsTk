import matplotlib.pyplot as plt
from tkinter import filedialog
import tkinter
import csv
import os

root = tkinter.Tk()
root.withdraw()

filename = "" # Path to CSV data file

if not filename:
    filename = filedialog.askopenfilename(initialdir="/", title="Please select a directory", filetypes=(("CSV files", "*.csv*"), ("All files", "*.*")))

include_phase_response = True # Plot phase response in addition to amplitude response
logarithmic_x_axis = False # Logarithmix X axis for plot

position_of_bode_legend = "lower left" # Standard: lower right
position_of_phase_legend = "lower left" # Standerd: lower right


def plot_data(filename, include_phase=False, log_scale=False, bode_label_pos="lower right", phase_label_pos="lower right"):
    header = []
    data = []

    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile)

        header = next(csvreader)

        for datapoint in csvreader:
            values = [float(value) for value in datapoint]
            data.append(values)


    frequency = [p[0] for p in data]
    ref_voltage = [p[1] for p in data]
    amplitude_response = [p[2] for p in data]

    if (include_phase):
        phase_response = [p[3] for p in data]

        fig, axs = plt.subplots(2, sharex=True)

        color = "tab:blue"
        axs[0].set_ylabel("Amplituderespons [dB]", color=color)
        axs[0].plot(frequency, ref_voltage, "-", color="tab:orange", label="Referansesignal")
        axs[0].plot(frequency, amplitude_response, "-", color=color, label="Utgangssignal")
        axs[0].legend(loc=bode_label_pos)
        axs[0].tick_params(axis="y", labelcolor=color)

        color="tab:green"
        axs[1].set_ylabel("Vinkel [deg $^\circ$]", color=color)
        axs[1].plot(frequency, phase_response, "-", color=color, label="Faserespons")
        axs[1].legend(loc=phase_label_pos)
        axs[1].tick_params(axis="y", labelcolor=color)

        fig.tight_layout()

    else:
        plt.plot(frequency, ref_voltage, "-", color="orange")
        plt.plot(frequency, amplitude_response, "-", color="blue")

        plt.ylabel("Amplituderespons [dB]")
        plt.legend(["Referansesignal", "Utgangssignal"], loc=bode_label_pos)
    
    plt.xlabel("Frekvens [Hz]")

    if (log_scale):
        plt.xscale("log")

    plt.show()

plot_data(filename, include_phase=include_phase_response, log_scale=logarithmic_x_axis, bode_label_pos=position_of_bode_legend, phase_label_pos=position_of_phase_legend)