import pandas as pd
from edge-terminal.backend.app.services.indicators import rsi_wilder, obv, vpoc

def test_rsi_basic():
    s = pd.Series([i for i in range(100)])
    r = rsi_wilder(s, 14)
    assert 0 <= r.iloc[-1] <= 100

def test_obv_monotonic():
    close = pd.Series([1,2,3,4,5])
    volume = pd.Series([10,10,10,10,10])
    o = obv(close, volume)
    assert o.iloc[-1] > o.iloc[0]

def test_vpoc_returns_nodes():
    import numpy as np
    high = pd.Series(np.linspace(10,20,50))
    low = high - 1
    close = (high + low) / 2
    volume = pd.Series(np.random.rand(50) * 100)
    v, nodes = vpoc(high, low, close, volume)
    assert isinstance(v, float)
    assert len(nodes) <= 5
