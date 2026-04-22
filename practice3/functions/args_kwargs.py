# args_kwargs.py
# Demonstrates *args and **kwargs usage

def sum_all(*numbers):
    """Sums all positional arguments."""
    return sum(numbers)

print(sum_all(1, 2, 3, 4))


def print_user_info(**info):
    """Prints keyword arguments."""
    for key, value in info.items():
        print(f"{key}: {value}")

print_user_info(name="Nurkanat", age=19, city="Almaty")
