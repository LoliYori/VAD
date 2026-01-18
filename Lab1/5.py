def compute_reading_duration(pages_per_hour: int, book_length: int) -> int:
    """
    Вычисляет количество дней для прочтения книги с возрастающей скоростью.
    """
    if book_length <= 0:
        return 0
    
    total_read = 0
    day_count = 0
    
    while total_read < book_length:
        day_count += 1
        
        daily_hours = day_count
        current_speed = pages_per_hour + (day_count - 1) * 2
        daily_pages = current_speed * daily_hours
        
        total_read += daily_pages
    
    return day_count


def simulate_reading_progress():
    """
    Основная функция: обрабатывает ввод и выводит результат.
    """
    try:
        initial_speed = int(input())
        total_pages = int(input())
        
        days_needed = compute_reading_duration(initial_speed, total_pages)
        print(days_needed)
        
    except ValueError:
        pass


if __name__ == "__main__":
    simulate_reading_progress()