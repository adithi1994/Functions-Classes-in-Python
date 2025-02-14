def calculate_powers(*args):
    number_of_args= len(args)

    if number_of_args == 1:
        return args[0]**2
    elif number_of_args == 2:
        return args[0] ** args[1]
    elif number_of_args > 2:
        total_sum = sum(args[:-1])
        return total_sum ** args[-1]
    else:
        return "No arguments provided."


print(calculate_powers(4))
print(calculate_powers(2, 3))
print(calculate_powers(1, 2, 3, 2))
print(calculate_powers())


