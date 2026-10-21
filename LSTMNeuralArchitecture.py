import torch
import torch.nn as nn

class JenaLSTMModel(nn.Module):
    def __init__(self, inp_size, lstm_width=64):
        super().__init__()

        self.lstm = nn.LSTM(
            input_size=inp_size,
            hidden_size=lstm_width,
            num_layers=2,
            batch_first=True
        )

        self.linear_out = nn.Linear(lstm_width, 1)

    def forward(self, x):
        lstm_out, _ = self.lstm(x)
        last_step = lstm_out[:, -1, :]

        out = self.linear_out(last_step)

        return out