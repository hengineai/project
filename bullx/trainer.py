import torch
from model import BullXModel

def train_model():
    model = BullXModel()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    loss_fn = torch.nn.CrossEntropyLoss()

    for epoch in range(10):
        inputs = torch.randn(32, 128)
        targets = torch.randint(0, 10, (32,))

        outputs = model(inputs)
        loss = loss_fn(outputs, targets)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")

if __name__ == '__main__':
    train_model()
