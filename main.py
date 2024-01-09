import csv
from datetime import datetime

class DataVisualizer:
    def __init__(self, file):
        self.file = file
    def read_data(self):
        data = []
        with open(self.file, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                data.append(row)
        return data

if __name__ == "__main__":
    visualizer = DataVisualizer("data/test_data.csv")
    data = visualizer.read_data()