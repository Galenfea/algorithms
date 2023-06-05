# Успешная отправка 4 июл 2022, 00:05:45 id 69290987

def edge_search(nums: list, left: int, right: int) -> int:
    """Найди индекс элемента бывшего нулевым в кольцевом буфере."""
    if nums[left] <= nums[right]:  # массив отсортирован
        return left  # начало массива
    mid = (left + right) // 2
    # массив не отсортирован в левой части от mid
    if nums[left] > nums[mid]:
        return edge_search(nums, left, mid)
    # массив отсортирован по левой, но, возможно,
    # не отсортирован в правой части от mid
    else:
        return edge_search(nums, mid+1, right)


def binarysearch(nums: list, target: int, left: int, right: int) -> int:
    """Проведи стандартный рекурсивный бинарный поиск.

    В случае отсутствия элемента в массиве, верни -1.
    """
    if right <= left:
        return -1
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif target < nums[mid]:
        return binarysearch(nums, target, left, mid)
    else:
        return binarysearch(nums, target, mid + 1, right)


def broken_search(nums, target) -> int:
    """Проведи бинарный поиск в частях массива, разделённых нулевым элементом.

    Функция находит элемент, бывший нулевым в кольцевом буфере, разделяет
    массив на две отсортированные части и проводит бинарный поиск в каждой
    из них.
    """
    nums_length = len(nums)
    initial_element = edge_search(nums, 0, nums_length-1)
    target_index = binarysearch(nums, target, 0, initial_element)
    if target_index > -1:
        return target_index
    return binarysearch(nums, target, initial_element, nums_length)


def main() -> None:
    # Тесты не предполагают передачу размера массива в функцию broken_search()
    input()
    target = int(input())
    nums = list(map(int, input().split()))
    broken_search(nums, target)


if __name__ == '__main__':
    main()
