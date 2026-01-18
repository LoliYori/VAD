def compute_finish_time(teeth_in_row: int, minutes_per_tooth: int):
    """
    Вычисляет время окончания чистки зубов.
    """
    START_TIME = 8 * 60  # 8:00 в минутах от полуночи
    
    total_teeth = teeth_in_row * 2
    total_duration = total_teeth * minutes_per_tooth
    
    finish_in_minutes = START_TIME + total_duration
    
    hours = finish_in_minutes // 60
    minutes = finish_in_minutes % 60
    
    return hours, minutes


def process_brushing_session():
    """
    Основная функция: читает входные данные и выводит результат.
    """
    try:
        teeth_count = int(input())
        time_per_tooth = int(input())
        
        end_hour, end_minute = compute_finish_time(teeth_count, time_per_tooth)
        
        print(end_hour)
        print(end_minute)
        
    except ValueError:
        pass


if __name__ == "__main__":
    process_brushing_session()