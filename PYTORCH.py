import torch

print("PyTorch Version:", torch.__version__)
print("CUDA Available:", torch.cuda.is_available()) # 应输出 True
print("CUDA Version:", torch.version.cuda)
print("GPU Count:", torch.cuda.device_count())
if torch.cuda.is_available():
    print("Current GPU:", torch.cuda.get_device_name(0))