def find_smallest_number_with_sum(digit_count: int, target_sum: int) -> str:
    """
    Находит минимальное число с заданным количеством цифр и суммой цифр.
    """
    # Проверка возможности существования такого числа
    if target_sum < 1 or target_sum > 9 * digit_count:
        return "NO"
    
    remaining_sum = target_sum
    number_digits = []
    
    for position in range(digit_count):
        is_first_digit = (position == 0)
        remaining_positions = digit_count - 1 - position
        
        # Определяем минимальную возможную цифру для текущей позиции
        min_digit = 1 if is_first_digit else 0
        
        # Ищем наименьшую цифру, которую можно поставить на эту позицию
        for digit in range(min_digit, 10):
            needed_remaining = remaining_sum - digit
            
            if 0 <= needed_remaining <= 9 * remaining_positions:
                number_digits.append(str(digit))
                remaining_sum -= digit
                break
    
    if len(number_digits) == digit_count:
        return "".join(number_digits)
    else:
        return "NO"


def process_number_search():
    """
    Основная функция: обрабатывает ввод и выводит результат.
    """
    try:
        digits_needed = int(input())
        sum_needed = int(input())
        
        result = find_smallest_number_with_sum(digits_needed, sum_needed)
        print(result)
    except ValueError:
        print("NO")


if __name__ == "__main__":
    process_number_search()