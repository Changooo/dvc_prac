import torch

num = 100000
tensors = {}

for i in range(num):
    tensors[f"tensor_{i + 1}"] = torch.rand(3, 3)

# 텐서를 파일로 저장
file_path = "random_tensors.pt"
torch.save(tensors, file_path)
