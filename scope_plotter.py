import matplotlib.pyplot as plt
from tkinter import filedialog
import tkinter
import csv
import os

root = tkinter.Tk()
root.withdraw()

filename = "" # Path to CSV data file

SAVE_FIGURE = True
SAVE_NAME = "scope_realized_circuit"
SAVE_DIRECTORY = ""

logarithmic_x_axis = False # Logarithmix X axis for plot


if not filename:
    filename = filedialog.askopenfilename(initialdir="/", title="Please select a directory", filetypes=(("CSV files", "*.csv*"), ("All files", "*.*")))

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

    plt.ylabel("Spenning [V]")
    plt.xlabel("Tid [s]")

    plt.legend(["$V_1$", "$V_2$"], loc="upper right")

    if (SAVE_FIGURE):
        if (SAVE_DIRECTORY != "" and SAVE_NAME != ""):
            plt.savefig(f"{SAVE_DIRECTORY}/{SAVE_NAME}.png")
        elif (SAVE_DIRECTORY == "" and SAVE_NAME != ""):
            FULL_SAVE_PATH = filedialog.askdirectory(initialdir=".", title="Please select a directory")
            plt.savefig(f"{FULL_SAVE_PATH}/{SAVE_NAME}.png")
        else:
            save_name_input = input("Name of figure: ")
            plt.savefig(f"{save_name_input}.png")

    plt.show()

plot_data(filename, logarithmic_x_axis)