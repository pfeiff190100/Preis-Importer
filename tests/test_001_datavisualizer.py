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