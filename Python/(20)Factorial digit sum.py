def factorial(number):

    if number == 1 or number == 0:
        return 1

    handle_odd = False
    goal = number

    if number % 2 == 1:
        goal -= 1
        handle_odd = True

    next_sum = goal
    next_multi = goal
    factorial = 1

    while next_sum >= 2:
        factorial *= next_multi
        next_sum -= 2
        next_multi += next_sum

    if handle_odd:
        factorial *= number

    return factorial


print(sum([int(x) for x in str(factorial(100))]))
