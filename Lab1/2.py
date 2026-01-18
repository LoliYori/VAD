def compute_infection_duration(daily_spawn: int, daily_cleanup: int, target_limit: int) -> int:
    """
    Вычисляет количество дней, за которое количество изображений
    превысит заданный лимит.
    """
    if daily_spawn > target_limit:
        return 1
    
    daily_net_gain = daily_spawn - daily_cleanup
    remaining_to_target = (target_limit - daily_spawn) + 1
    
    extra_days_needed = (remaining_to_target + daily_net_gain - 1) // daily_net_gain
    
    return 1 + extra_days_needed


def run_virus_simulation() -> None:
    """
    Основная функция: считывает параметры и выводит результат.
    """
    try:
        spawn_rate = int(input())
        cleanup_rate = int(input())
        limit = int(input())
        
        days_required = compute_infection_duration(spawn_rate, cleanup_rate, limit)
        print(days_required)
        
    except ValueError:
        pass


if __name__ == "__main__":
    run_virus_simulation()