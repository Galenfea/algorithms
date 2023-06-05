# Успешная отправка 1 июл 2022, 16:43:50 id 69263319

class DoubleEndedQueueError(Exception):
    """Исключение возникает при ошибках в работе с классом DoubleEndedQueue."""
    pass


class DoubleEndedQueue:
    def __init__(self, max_size_deque):
        self.deque = [None] * max_size_deque
        self.max_size = max_size_deque
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        """Проверь является дек пустым."""
        return self.size == 0

    def push_front(self, value):
        if self.size == self.max_size:
            raise DoubleEndedQueueError('DEQ переполнена')
        self.deque[self.tail] = value
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def pop_back(self):
        if self.is_empty():
            raise DoubleEndedQueueError('DEQ пуста')
        value = self.deque[self.head]
        self.deque[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return value

    def push_back(self, value):
        if self.size == self.max_size:
            raise DoubleEndedQueueError('DEQ переполнена')
        tail_back = self.head - 1
        if tail_back < 0:
            tail_back = self.max_size - 1
        self.deque[tail_back] = value
        self.head = (tail_back) % self.max_size
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise DoubleEndedQueueError('DEQ пуста')
        value = self.deque[self.tail - 1]
        head_back = self.tail - 1
        if head_back < 0:
            head_back = self.max_size - 1
        self.deque[head_back] = None
        self.tail = (head_back) % self.max_size
        self.size -= 1
        return value


def execute_command(deque, command):
    """Прими список строковых 'команд' и верни исполняемую команду."""
    if command[0] == command[-1]:
        return getattr(deque, command[0])()
    return getattr(deque, command[0])(command[-1])


def deque(number_of_commands, commands, deq_size):
    """Распечатай результат выполнения команд.

    Функция принимает число команд, список команд, экземпляр deq
    и печатает результат их выполнения.
    """
    deque_instance = DoubleEndedQueue(deq_size)
    for number in range(number_of_commands):
        # Из решающей части убрано считывание входных данных
        try:
            result = execute_command(deque_instance, commands[number])
            if result:
                print(result)
        except DoubleEndedQueueError:
            print('error')


def main():
    # Считывание входных данных
    number_of_commands = int(input())
    deq_size = int(input())
    commands = []
    # Чтение инпута отделено от решающей функции, что добавляет лишний цикл.
    # Так и должно быть? Это увеличивает расход памяти (в 6,5 раз) и время.
    for number in range(number_of_commands):
        commands.append(input().split())
    # Решающая часть
    deque(number_of_commands, commands, deq_size)


if __name__ == '__main__':
    main()
