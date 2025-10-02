import pandas as pd
from prophet import Prophet
import os

def run_predict(csv_path='data/cpu_timeseries.csv'):
    # Expect csv with columns: ds (RFC3339), y (numeric)
    if not os.path.exists(csv_path):
        # create synthetic series if not present
        import numpy as np
        import pandas as pd
        idx = pd.date_range(end=pd.Timestamp.now(), periods=288, freq='5min')
        y = 20 + 10 * np.sin(2 * 3.1415 * (pd.Series(range(len(idx))) / 288))
        df = pd.DataFrame({'ds': idx, 'y': y})
        os.makedirs(os.path.dirname(csv_path), exist_ok=True)
        df.to_csv(csv_path, index=False)
    df = pd.read_csv(csv_path, parse_dates=['ds'])
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=12, freq='5min')
    forecast = model.predict(future)
    out = forecast[['ds','yhat','yhat_lower','yhat_upper']].tail(12)
    os.makedirs('orchestrator/predictor/out', exist_ok=True)
    out.to_csv('orchestrator/predictor/out/forecast.csv', index=False)
    return out.to_dict(orient='records')

if __name__ == '__main__':
    print(run_predict())
