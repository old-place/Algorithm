import math
from typing import List
from decorators import count_time


@count_time
def get_prime(num: int) -> List[int]:
	""" エラストテネスの篩 """

	if num <= 1:
		return []

	prime_numbers = [2]

	# 探索する条件を最大数の平方根までとする
	limit = int(math.sqrt(num))
	
	# 奇数だけを探していく
	# 2以上の奇数のリストを作る
	odd_numbers = [i+1 for i in range(2, num, 2)]

	while limit > odd_numbers[0]:
		prime_numbers.append(odd_numbers[0])

		odd_numbers = [j for j in odd_numbers if j % odd_numbers[0] != 0]

	return prime_numbers + odd_numbers

if __name__ == '__main__':
	print(get_prime(100000))
