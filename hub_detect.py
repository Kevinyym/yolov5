import torch

# Model
model = torch.hub.load("./", "yolov5s", source="local")

# Images
img = "./data/images/zidane.jpg"

# Inference
results = model(img)

# Results
results.show()