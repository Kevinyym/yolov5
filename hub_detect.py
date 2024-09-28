# import torch
#
# # Model
# model = torch.hub.load("./", "yolov5s", source="local")
#
# # Images
# img = "./data/images/zidane.jpg"
#
# # Inference
# results = model(img)
#
# # Results
# results.show()

import torch

# Model
model = torch.hub.load("./", "custom", path="runs/train/exp2/weights/best.pt", source="local")

# Images
img = "./datasets/images/train/30.jpg"

# Inference
results = model(img)

# Results
results.show()