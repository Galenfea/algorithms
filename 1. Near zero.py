# успешная отправка 19 июн 2022, 13:57:52 id 69040917

def first_zero_pozition(street_length: int, street: list) -> int:
    """Вычисли позицию первого пустого участка на улице."""
    for site in range(street_length):
        if street[site] == '0':
            return site
    raise Exception('На улице нет пустых участков')


def last_zero_pozition(street_length: int, street: list) -> int:
    """Вычисли позицию последнего пустого участка на улице."""
    for site in range(street_length-1, -1, -1):
        if street[site] == '0':
            return site
    raise Exception('На улице нет пустых участков')


def calculate_range_to_near_zero(street_length: int, street: list) -> str:
    """Создай массив с расстояниями до ближайших не застроенных участков."""
    list_of_range_to_zero = []
    # инициализация ближайшего нуля
    near_zero = first_zero_pozition(street_length, street)
    last_zero = last_zero_pozition(street_length, street)
    for cursor in range(street_length):
        if street[cursor] == '0':
            near_zero = cursor
        # кладём в массив разницу между позицией элемента и позицией
        # ближайшего нуля слева -->
        list_of_range_to_zero.append(
            abs(cursor - near_zero)
        )
    for cursor in range(street_length-1, -1, -1):
        if street[cursor] == '0':
            last_zero = cursor
        # кладём в массив разницу между позицией элемента и позицией
        # ближайшего нуля справа <--, если она меньше,
        # чем расстояние до нуля слева
        right_distance_to_zero = abs(cursor - last_zero)
        if right_distance_to_zero < list_of_range_to_zero[cursor]:
            list_of_range_to_zero[cursor] = right_distance_to_zero
    return ' '.join(map(str, list_of_range_to_zero))


def main() -> None:
    street_length = int(input())
    street = input().split()
    print(calculate_range_to_near_zero(street_length, street))


if __name__ == '__main__':
    main()
