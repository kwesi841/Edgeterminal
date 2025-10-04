import numpy as np
import pandas as pd
from typing import Tuple, List

# RSI (Wilder) with period n

def rsi_wilder(close: pd.Series, n: int = 14) -> pd.Series:
    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1 / n, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / n, adjust=False).mean()
    rs = avg_gain / (avg_loss.replace(0, np.nan))
    rsi = 100 - (100 / (1 + rs))
    return rsi.fillna(50)

# OBV and OBV ROC

def obv(close: pd.Series, volume: pd.Series) -> pd.Series:
    direction = np.sign(close.diff().fillna(0))
    return (direction * volume).cumsum()

# Volume-by-Price approximate VPOC

def vpoc(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series, bins: int = 30
) -> Tuple[float, List[float]]:
    typical_price = (high + low + close) / 3.0
    price_min, price_max = typical_price.min(), typical_price.max()
    bin_edges = np.linspace(price_min, price_max, bins + 1)
    bin_indices = np.digitize(typical_price, bin_edges) - 1
    vol_by_bin = np.zeros(bins)
    for idx, vol in zip(bin_indices, volume):
        if 0 <= idx < bins:
            vol_by_bin[idx] += vol
    max_idx = int(np.argmax(vol_by_bin))
    centers = (bin_edges[:-1] + bin_edges[1:]) / 2.0
    top_nodes_idx = np.argsort(vol_by_bin)[-5:]
    nodes = [float(centers[i]) for i in sorted(top_nodes_idx)]
    return float(centers[max_idx]), nodes

# Helpers

def ema(series: pd.Series, n: int) -> pd.Series:
    return series.ewm(span=n, adjust=False).mean()


def true_range(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    prev_close = close.shift(1)
    tr = pd.concat([
        (high - low),
        (high - prev_close).abs(),
        (low - prev_close).abs(),
    ], axis=1).max(axis=1)
    return tr.fillna(high - low)


def rolling_zscore(series: pd.Series, window: int = 30) -> pd.Series:
    mean = series.rolling(window).mean()
    std = series.rolling(window).std(ddof=0)
    return (series - mean) / (std.replace(0, np.nan))
