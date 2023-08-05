## LevelRegressor 

import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset
from torch.utils.data import DataLoader

class Dataset(Dataset) :
    def __init__(self, x, y):
        self.x_data = None;

    def __len__(self) :
        return len(self.x_data)
    
    def __getitem__(self, idx) :
        None;

class LevelRegressor :
    def __init__(self) :
        super(LevelRegressor, self).__init__()
        self.layer = nn.Sequential(
            nn.Linear(2,16),
            nn.ReLU(),
            nn.Linear(16,8),
            nn.ReLU(),
            nn.Linear(8,4),
            nn.ReLU(),
            nn.Linear(4,1)
        )


    def forward(self, x) :
        x = self.layer(x)
        return x

model = LevelRegressor()

loss_fn = nn.MSELoss()

optimizer = optim.Adams(lr=1e-4)

def train(dataloader, model, loss_fn, optimizer) :
    size = len(dataloader.dataset)
    for epoch in epochs :
        pred = model.forward(x)
        loss = loss_fn(y,pred)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        print(f"loss {loss}, epoch {epoch}")




