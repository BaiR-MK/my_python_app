# utils.py
from colorama import Fore, Style  # Добавили импорт

def calculate_sum(a, b):
    return a + b

def calculate_difference(a, b):
    return a - b

def format_message(msg):
    return f"{Fore.GREEN}{msg}{Style.RESET_ALL}"  # Новая функция
