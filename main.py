# main.py
import config
from utils import format_message, calculate_sum, calculate_product, calculate_quotient, calculate_difference
from colorama import init, Fore, Style

init()  # Инициализация colorama для Windows

def get_number(prompt):
    """Получение числа от пользователя"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(f"{Fore.RED}Пожалуйста, введите число!{Style.RESET_ALL}")

def main():
    print(f"{Fore.GREEN}Запуск {config.APP_NAME} версии {config.APP_VERSION}{Style.RESET_ALL}")
    print(format_message("Приложение инициализировано", Fore.CYAN))
    
    while True:
        print(f"\n{Fore.CYAN}--- Калькулятор ---{Style.RESET_ALL}")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Выход")
        
        choice = input("Выберите операцию (1-5): ")
        
        if choice == '5':
            print(f"{Fore.GREEN}До свидания!{Style.RESET_ALL}")
            break
            
        if choice in ['1', '2', '3', '4']:
            a = get_number("Введите первое число: ")
            b = get_number("Введите второе число: ")
            
            if choice == '1':
                result = calculate_sum(a, b)
                operation = "+"
            elif choice == '2':
                result = calculate_difference(a, b)
                operation = "-"
            elif choice == '3':
                result = calculate_product(a, b)
                operation = "*"
            elif choice == '4':
                try:
                    result = calculate_quotient(a, b)
                    operation = "/"
                except ValueError as e:
                    print(f"{Fore.RED}Ошибка: {e}{Style.RESET_ALL}")
                    continue
            
            print(f"{Fore.YELLOW}{a} {operation} {b} = {result}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Неверный выбор!{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
