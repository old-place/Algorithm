

def fibonacci(n: int) -> int:
	""" フィボナッチ数列(シンプルな再帰) """
	if n in [1, 2]:
		return 1
	return fibonacci(n-1) + fibonacci(n-2)



if __name__ == "__main__":
	print(list(map(lambda n:fibonacci(n), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
