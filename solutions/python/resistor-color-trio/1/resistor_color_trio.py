def label(colors: list) -> str:
    """
    Translates three resistor color bands into a labeled resistance value (in ohms).

    The first two bands form the significant digits, and the third band is the multiplier (power of 10).
    Metric prefixes (kilo, mega, giga) are used for large values.

    :param colors: list - A list of three color strings (e.g., ["orange", "orange", "orange"]).
    :return: str - The resistance label (e.g., "33 kiloohms").
    """
    
    # 1. Словарь для перевода цветов в числовые значения
    COLOR_VALUES = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, 
        "yellow": 4, "green": 5, "blue": 6, "violet": 7, 
        "grey": 8, "white": 9
    }

    # 2. Вычисляем общее сопротивление в Омах
    
    # Первые две полосы - значащие цифры
    digit_1 = COLOR_VALUES[colors[0].lower()]
    digit_2 = COLOR_VALUES[colors[1].lower()]
    
    # Третья полоса - множитель (количество нулей или степень 10)
    multiplier_exponent = COLOR_VALUES[colors[2].lower()]
    
    # Основное значение из первых двух цифр
    main_value = digit_1 * 10 + digit_2
    
    # Общее сопротивление в Омах
    total_ohms = main_value * (10 ** multiplier_exponent)

    # 3. Применение метрического префикса
    
    # Префиксы для 1000 (kilo), 1,000,000 (mega), 1,000,000,000 (giga)
    
    if total_ohms < 1000:
        # Если меньше 1000, используем просто "ohms"
        return f"{total_ohms} ohms"
    
    # Если total_ohms >= 1000, начинаем делить на 1000 и добавлять префикс
    
    # Метрические префиксы: 
    # 0: "" (ohms), 1: "kilo", 2: "mega", 3: "giga"
    units = ["ohms", "kiloohms", "megaohms", "gigaohms"]
    
    # Начинаем с килоом (индекс 1)
    for i in range(1, len(units)):
        divisor = 1000 ** i
        if total_ohms < divisor * 1000:
            # Преобразуем значение в метрическую единицу
            # Например: 33000 / 1000 = 33.0 kiloohms
            # 3300 / 1000 = 3.3 kiloohms
            
            converted_value = total_ohms / divisor
            
            # Форматируем число, убирая ".0" для целых чисел,
            # но сохраняя десятичные для нецелых (например, 3.3)
            if converted_value == int(converted_value):
                # Если 33.0, выводим 33
                formatted_value = int(converted_value)
            else:
                # Если 3.3, выводим 3.3
                formatted_value = converted_value
            
            return f"{formatted_value} {units[i]}"
            
    # Крайний случай (для очень больших чисел, но в рамках задания не требуется)
    return f"{total_ohms} ohms" 

# --- Примеры использования для демонстрации: ---

# orange-orange-black (33 * 10^0 = 33) -> 33 ohms
# print(label(["orange", "orange", "black"]))

# orange-orange-red (33 * 10^2 = 3300) -> 3.3 kiloohms
# print(label(["orange", "orange", "red"]))

# orange-orange-orange (33 * 10^3 = 33000) -> 33 kiloohms
# print(label(["orange", "orange", "orange"]))

# yellow-violet-yellow (47 * 10^4 = 470000) -> 470 kiloohms
# print(label(["yellow", "violet", "yellow"]))

# brown-black-black (10 * 10^0 = 10) -> 10 ohms
# print(label(["brown", "black", "black"]))

# brown-black-orange (10 * 10^3 = 10000) -> 10 kiloohms
# print(label(["brown", "black", "orange"]))

# brown-black-yellow (10 * 10^4 = 100000) -> 100 kiloohms
# print(label(["brown", "black", "yellow"]))

# brown-black-blue (10 * 10^6 = 10000000) -> 10 megaohms
# print(label(["brown", "black", "blue"]))
