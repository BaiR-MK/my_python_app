import config
from utils import calculate_sum
from colorama import init, Fore, Style

init()

print(f"{Fore.GREEN}Запуск {config.APP_NAME}{Style.RESET_ALL}")
result = calculate_sum(10, 5)
print(f"{Fore.CYAN}10 + 5 = {result}{Style.RESET_ALL}")
