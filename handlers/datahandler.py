import csv
from typing import List

# Get data from CSV file
# NB! Program expects file headers to work properly
def get_csv_data(filename='') -> List[List[float]]:
    header = []
    data = []

    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile)

        header = next(csvreader)

        for datapoint in csvreader:
            values = [float(value) for value in datapoint]
            data.append(values)
    
    return data
