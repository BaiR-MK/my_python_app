# main.py
import config
from utils import calculate_sum

print(f"Запуск {config.APP_NAME}")
result = calculate_sum(10, 5)
print(f"10 + 5 = {result}")
