class Solution(object):
    def number_is_happy(num):
        while num != 1 and num != 4: #цикл работает до тех пор, пока num не станет 1 или 4
            num = sum(int(digit) ** 2 for digit in str(num)) #происходит преобразование числа в строку, извлечение цифры, их возведение в квадрат и суммирование
        if num == 1: #сравнивается текущее значение num с 1
            return True #если num равно 1, возвращается true, если нет - false
        if num == 4: #цикл прекращает выполнение
            return False #и программа выполняет return n == 1, что возвращает false

    num = int(input('введите число: '))
    print(number_is_happy(num))