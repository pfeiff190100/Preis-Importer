from main import DataVisualizer
import pytest
from datetime import datetime

def test_readdata():
    visualizer = DataVisualizer("data/test_data.csv")
    data = visualizer.read_data()

    assert len(data) > 0
    for row in data:
        assert len(row) == 5
        datetime.fromtimestamp(int(row[1]))
        float(row[2])
    
    assert data[0][0] == "Lenzing"
    assert data[0][1] == "170447112"
    assert data[0][2] == "34.75"
    assert data[0][3] == "EUR"
    assert data[0][4] == "Vienna"

def test_visualizer():
    visualizer = DataVisualizer("data/test_data.csv")
    data = visualizer.read_data()
    dates, prices = visualizer.visualize_data(data, True)

    assert prices == [34.75, 59.41, 28.55, 31.18]
    assert dates == [datetime(1975, 5, 27, 20, 25, 12), 
                    datetime(1975, 5, 27, 20, 25, 31), 
                    datetime(1975, 5, 27, 20, 25, 32), 
                    datetime(1975, 5, 27, 20, 25, 33)]