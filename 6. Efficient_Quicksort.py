# Успешная отправка 4 июл 2022, 10:45:21 id 69293840

import random

FIELDS = {'LOGIN': 2, 'SCORE': 0, 'FINE': 1}


def partition_without_memory(array, left, right, pivot):
    """Определи границы разделения массива на отсортированные части.

    Функция принимает опорный элемент, и возвращает границы подмассивов для
    проведения быстрой сортировки.
    """
    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        # Следующие два условия можно объединить в одно,
        # но мне кажется, что при этом пострадает устойчивость сортировки.
        if left < right:
            array[left], array[right] = array[right], array[left]
        if left == right:
            left, right = left + 1, right - 1
    return left, right


def quicksort(array, left, right):
    """Проведи быструю сортировку по подмассивам в полученных границах."""
    if left >= right:
        return
    pivot = array[random.randint(left, right)]
    new_left, new_right = partition_without_memory(array, left, right, pivot)
    quicksort(array, left, new_right)
    quicksort(array, new_left, right)


def input_members(members_number):
    members = []
    for _ in range(members_number):
        login, score, fine = input().split()
        members.append((-int(score), int(fine), login,))
    return members


def print_members(members):
    # Хотел использовать именованные кортежи, но их нельзя сравнить
    # без написания дополнительных функций типа компаратора,
    # что выглядит как излишний код там, где можно обойтись константой
    # для читаемости.
    print(*[member[FIELDS['LOGIN']] for member in members], sep='\n')


def main():
    members_number = int(input())
    members = input_members(members_number)
    quicksort(members, 0, members_number-1)
    print_members(members)


if __name__ == '__main__':
    main()
