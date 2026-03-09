# utils.py
from colorama import Fore, Style

def format_message(message, color=None):
    """Форматирование сообщения с опциональным цветом"""
    if color:
        return f"{color}[INFO] {message}{Style.RESET_ALL}"
    return f"[INFO] {message}"

def calculate_sum(a, b):
    """Сложение двух чисел"""
    return a + b

def calculate_difference(a, b):
    """Вычитание двух чисел"""
    return a - b

def calculate_product(a, b):
    """Умножение двух чисел"""
    return a * b

def calculate_quotient(a, b):
    """Деление двух чисел"""
    if b == 0:
        raise ValueError("Деление на ноль!")
    return a / b
