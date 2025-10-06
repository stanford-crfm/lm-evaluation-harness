# data = load_dataset('HausaNLP/AfriSenti-Twitter', 'yor', trust_remote_code=True)
# print(data)

try:
    import torch
except ImportError:
    torch = None


print(torch.cuda.is_available())  # Should return True
print(torch.cuda.device_count())
