# Успешная отправка 1 июл 2022, 16:04:22 id 69262899

# Имеет ли смысл уточнять что-то в Slack? Как вообще работает обратная связь?
# Я обращался в Slack-е 22-ого июня но не получил обратной связи.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            raise IndexError('Не хватает элементов для совершения операций.')
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            raise IndexError('Нет элементов для вывода.')
        return self.items[-1]


# Константа
OPERATIONS = {'+': lambda a, b: a + b,
              '-': lambda a, b: a - b,
              '*': lambda a, b: a * b,
              '/': lambda a, b: a // b
              }


def int_operand(value):
    """Если значение - не оператор, приведи к целочисленному типу."""
    # нет возможности заменить одним .isdigit() так как .isdigit()
    # не воспринимает '-' перед отрицательным числом как часть числа.
    if ((value == '-') or (value == '+') or (value == '/')
       or (value == '*')):
        return value
    return int(value)


def calculator(data_in):
    stack = Stack()
    for value in data_in:
        if type(value) == int:
            stack.push(value)
        if type(value) == str:
            try:
                operand_2 = stack.pop()
                operand_1 = stack.pop()
            except IndexError as error:
                print(error)
            else:
                value = OPERATIONS[value](operand_1, operand_2)
                stack.push(value)
    print(stack.peek())


def main():
    calculator(map(int_operand, input().split()))


if __name__ == '__main__':
    main()
