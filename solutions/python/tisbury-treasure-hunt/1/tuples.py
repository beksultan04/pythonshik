def get_coordinate(record):
    """
    Возвращает значение координаты из кортежа, содержащего название сокровища и координату.
    """
    return record[1]


def convert_coordinate(coordinate):
    """
    Разделяет данную строку с координатами на кортеж из отдельных компонентов.
    """
    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """
    Сравнивает запись Азары с записью Руи, возвращает True, если координаты совпадают.
    """
    azara_coordinate_tuple = convert_coordinate(azara_record[1])
    return azara_coordinate_tuple == rui_record[1]


def create_record(azara_record, rui_record):
    """
    Объединяет две записи в одну, если они совпадают, иначе возвращает 'not a match'.
    """
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return "not a match"


def clean_up(combined_record_group):
    """
    Создает многострочный отчет из объединенных записей в требуемом формате.
    """
    report = ""
    for record in combined_record_group:
        # Для отчета мы создаем НОВЫЙ кортеж из 4-х элементов,
        # исключая record[1] (оригинальные координаты Азары).
        report_record = (record[0], record[2], record[3], record[4])
        report += str(report_record) + "\n"
        
    return report