# 测试 PyTorch
import torch
print(f"PyTorch version: {torch.__version__}")
print(f"NumPy version for PyTorch: {torch.__config__.show().split()}") # 查看PyTorch使用的numpy版本<websource>source_group_web_1</websource>

# 测试 TensorFlow
import tensorflow as tf
print(f"TensorFlow version: {tf.__version__}")