import csv

# def plot_data(filename, include_phase=False, log_scale=False, bode_label_pos="lower right", phase_label_pos="lower right"):
def get_csv_data(filename='') -> list:
    header = []
    data = []

    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile)

        header = next(csvreader)

        for datapoint in csvreader:
            values = [float(value) for value in datapoint]
            data.append(values)
    
    return data
