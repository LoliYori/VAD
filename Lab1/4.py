def has_unique_digits(number_value: int) -> bool:
    """
    Проверяет, содержит ли число только уникальные цифры.
    """
    digit_string = str(number_value)
    return len(digit_string) == len(set(digit_string))


def find_max_unique_digits_number(upper_bound: int) -> int:
    """
    Находит наибольшее число с уникальными цифрами, не превышающее лимит.
    """
    for current_number in range(upper_bound, 0, -1):
        if has_unique_digits(current_number):
            return current_number
    return 1  # Минимальное число с уникальными цифрами


def process_beautiful_number_search():
    """
    Основная функция: читает входные данные и выводит результат.
    """
    try:
        limit_value = int(input())
        result_number = find_max_unique_digits_number(limit_value)
        print(result_number)
    except ValueError:
        pass


if __name__ == "__main__":
    process_beautiful_number_search()