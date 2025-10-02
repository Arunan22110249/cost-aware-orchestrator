import torch
import torch.nn as nn
import pandas as pd
from torch.utils.data import Dataset, DataLoader
import os

class TSData(Dataset):
    def __init__(self, series, seq_len=12):
        self.x, self.y = [], []
        for i in range(len(series)-seq_len):
            self.x.append(series[i:i+seq_len])
            self.y.append(series[i+seq_len])
        self.x = torch.tensor(self.x).float().unsqueeze(-1)
        self.y = torch.tensor(self.y).float().unsqueeze(-1)
    def __len__(self): return len(self.x)
    def __getitem__(self, i): return self.x[i], self.y[i]

class LSTMModel(nn.Module):
    def __init__(self, hidden=32):
        super().__init__()
        self.lstm = nn.LSTM(1, hidden, batch_first=True)
        self.fc = nn.Linear(hidden, 1)
    def forward(self, x):
        _, (h, _) = self.lstm(x)
        return self.fc(h[-1])

if __name__ == '__main__':
    # Create synthetic data if none
    csv_path = 'data/cpu_timeseries.csv'
    if not os.path.exists(csv_path):
        import numpy as np
        import pandas as pd
        idx = pd.date_range(end=pd.Timestamp.now(), periods=1000, freq='5min')
        y = 20 + 10 * np.sin(2 * 3.1415 * (pd.Series(range(len(idx))) / 288))
        df = pd.DataFrame({'ds': idx, 'y': y})
        os.makedirs('data', exist_ok=True)
        df.to_csv(csv_path, index=False)
    series = pd.read_csv(csv_path)['y'].values
    dataset = TSData(series, seq_len=12)
    loader = DataLoader(dataset, batch_size=32, shuffle=True)
    model = LSTMModel()
    opt = torch.optim.Adam(model.parameters(), lr=1e-3)
    loss_fn = nn.MSELoss()
    for epoch in range(5):
        for xb, yb in loader:
            pred = model(xb)
            loss = loss_fn(pred, yb)
            opt.zero_grad(); loss.backward(); opt.step()
        print('epoch', epoch, 'loss', loss.item())
    os.makedirs('models', exist_ok=True)
    torch.save(model.state_dict(), 'models/lstm.pth')
