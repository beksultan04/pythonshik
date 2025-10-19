def square_of_sum(number):
    # сумма первых number чисел = number*(number+1)//2, затем возвести в квадрат
    s = number * (number + 1) // 2
    return s * s


def sum_of_squares(number):
    # формула суммы квадратов: n(n+1)(2n+1)/6
    return number * (number + 1) * (2 * number + 1) // 6


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
