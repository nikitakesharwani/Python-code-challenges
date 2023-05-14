from functools import reduce

numbers= [1,2,3,4,5,6,7,8,9]

sum_of_list = reduce(lambda prevNum , nextNum : prevNum + nextNum, numbers)
print(sum_of_list)


def number_multiplication(number1 , number2):
    return number1 * number2

multiplied = reduce(number_multiplication , numbers)
print(multiplied)

