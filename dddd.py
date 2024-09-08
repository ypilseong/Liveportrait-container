import torch
print(torch.cuda.is_available())  # True가 출력되어야 함
print(torch.cuda.current_device())  # 현재 사용 중인 GPU의 ID를 출력
print(torch.cuda.get_device_name(0))  # GPU의 이름을 출력
