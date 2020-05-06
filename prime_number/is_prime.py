import math
from typing import List
from decorators import count_time


def is_prime(num: int) -> bool:
	""" 素数であるかを判定する """

	if num <= 1:
		return False

	if num in [2, 3]:
		return True

	if (num % 2 == 0) or (num % 3 == 0):
		return False

	for i in range(2, int(math.sqrt(num))+1, 2):
		if num % i == 0:
			return False

	return True


@count_time
def get_prime(max_num: int) -> List[int]:
	prime_numbers = []

	for num in range(max_num):
		if is_prime(num):
			prime_numbers.append(num)

	return prime_numbers


if __name__ == '__main__':
	max_num = 100000
	prime_numbers = get_prime(max_num)
	print(f'0から{max_num}の素数は {prime_numbers}')
