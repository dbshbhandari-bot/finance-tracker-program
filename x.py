import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def forecast_series(series, days=14):
    series = series.dropna()
    X = np.arange(len(series)).reshape(-1, 1)
    y = series.values

    model = LinearRegression()
    model.fit(X, y)

    future_X = np.arange(len(series), len(series) + days).reshape(-1, 1)
    forecast = model.predict(future_X)

    return forecast
