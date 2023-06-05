# успешная отправка 19 июн 2022, 13:30:06 id 69040442

def get_matrix() -> list:
    """Получи данные из input и верни очищенную входную матрицу.

    Возвращает line_matrix матрицу очищенную от всего, кроме цифр и
    преобразовыванную в список.
    """
    line_matrix = []
    for i in range(4):
        line_matrix += (list(map(int, (''.join(filter(str.isdecimal, input()))
                                       ))))
    return line_matrix


def sleight_of_hand(number_of_fingers: int, line_matrix: list) -> int:
    """Определи сколько раз можно нажать все одинаковые цифры в списке.

    Функция принимает number_of_fingers - количество пальцев у одного игрока,
    то есть количество клавиш на которое, он способен нажать за раз,
    и line_matrix - список с цифрами от 0 до 9.
    Функция определяет сколько раз два игрока с одинаковым количеством пальцев
    могут нажать все клавиши с одной цифрой из списка line_matrix.
    """
    return sum([1 for number in range(10) if 0 < line_matrix.count(number)
                <= number_of_fingers*2
                ]
               )


def main() -> None:
    number_of_fingers = int(input())
    print(sleight_of_hand(number_of_fingers, get_matrix()))


if __name__ == '__main__':
    main()
