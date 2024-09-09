import torch
print("Welcome to the myTOEIC project.")
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Use device: ", device)
