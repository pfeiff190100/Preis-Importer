import csv
from datetime import datetime
import matplotlib.pyplot as plt

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

    def visualize_data(self, data, testmode=False):
        dates = [datetime.fromtimestamp(int(row[1])) for row in data]
        prices = [float(row[2]) for row in data]

        if not testmode:
            plt.plot(dates, prices)
            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.show()
        else:
            return dates, prices

if __name__ == "__main__":
    visualizer = DataVisualizer("data/test_data.csv")
    data = visualizer.read_data()
    visualizer.visualize_data(data)