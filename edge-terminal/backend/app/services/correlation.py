import pandas as pd
from typing import Dict, List


def correlation_matrix(prices: Dict[str, pd.Series], windows: List[int] = [30, 90]):
    mats = {}
    for w in windows:
        df = pd.DataFrame(prices)
        df = df.dropna().pct_change().dropna()
        mats[w] = df.tail(w).corr().to_dict()
    return mats
