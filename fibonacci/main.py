from datetime import datetime


from fibonacci1 import fibonacci as fibonacci_1
from fibonacci2 import fibonacci as fibonacci_2
from fibonacci3 import fibonacci as fibonacci_3



def main(fibonacci):

	lst = []

	start_time = datetime.now()
	for n in range(1, 35):
		lst.append(fibonacci(n))
	end_time = datetime.now()

	diff_time = end_time - start_time
	print(lst)
	print(f'実行時間は{diff_time.total_seconds()}秒です')




if __name__ == '__main__':
	main(fibonacci_1)
	main(fibonacci_2)
	main(fibonacci_3)
