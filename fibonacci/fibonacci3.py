

def fibonacci(n: int) -> int:
	""" フィボナッチ数列(シンプルな ループ) """

	fib_lst = [1, 1]

	for i in range(2, n):
		fib_lst.append(fib_lst[i-1] + fib_lst[i-2])

	return fib_lst[n-1]


if __name__ == "__main__":
	print(list(map(lambda n:fibonacci(n), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
