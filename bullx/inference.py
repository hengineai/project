import torch
from model import BullXModel

def run_inference():
    model = BullXModel()
    model.eval()
    inputs = torch.randn(1, 128)
    with torch.no_grad():
        output = model(inputs)
    print("Predicted logits:", output)

if __name__ == '__main__':
    run_inference()
