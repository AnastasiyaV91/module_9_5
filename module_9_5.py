class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
        if self.step == 0:                                      # Если шаг (step) равен нулю, то вызываем функцию
            raise StepValueError('шаг не может быть равен 0')   # StepValueError с сообщением

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration      # Прекращение итерации при условии логики
        else:
            a = self.pointer           # Создаем переменную а для возврата self.pointer (не увеличенного на self.step)
            self.pointer += self.step  # Увеличиваем итератор self.pointer на self.step
            return a                   # Если условие логики не выполняемся, то возвращаем self.pointer


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()