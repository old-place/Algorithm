
memo = {
	1: 1,
	2: 1,
}

def fibonacci(n: int) -> int:
	""" フィボナッチ数列(メモ化よる高速な再帰) """

	if n in memo:
		return memo[n]

	memo[n] = fibonacci(n-1) + fibonacci(n-2)
	return memo[n]


if __name__ == "__main__":
	print(list(map(lambda n:fibonacci(n), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
