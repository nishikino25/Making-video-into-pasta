import torch
DEVICE = torch.device('cuda')
SIZE = 512
EPOCHS = 300
STYLE_PATH = './input/pasta.jpg'
STYLE_WEIGHT = 1000000
CONTENT_PATH = '.\images\image_20.jpg'
CONTENT_WEIGHT = 1
OUTPUT_PATH = './output/output_image_0.jpg'
