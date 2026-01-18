def compute_sequence_sum(term_count: int) -> float:
    """
    Вычисляет сумму первых N членов последовательности.
    Формула члена: (2*i)/(i+2), где i от 1 до N.
    """
    if not 1 <= term_count <= 100:
        raise ValueError("N должно быть в диапазоне от 1 до 100.")
    
    total = sum((2 * i) / (i + 2) for i in range(1, term_count + 1))
    return total


def main() -> None:
    """
    Основная функция: получает N, вычисляет сумму и выводит результат.
    """
    try:
        n_terms = int(input().strip())
        result = compute_sequence_sum(n_terms)
        print(f"{result:.3f}")
        
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception:
        print("Произошла непредвиденная ошибка.")


if __name__ == "__main__":
    main()