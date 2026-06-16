import random

def get_random_numbers(
        start_range: int,
        end_range: int,
        out_len: int
) -> list[int]:
    if out_len > (end_range - start_range) + 1:
        raise ValueError(f'Out_len={out_len} is out of range')
    numbers_list = []
    while len(numbers_list) < out_len:
        num = random.randint(start_range, end_range)

        if num not in numbers_list:
            numbers_list.append(num)
    return numbers_list
