from datetime import datetime

def count_time(func):
	""" 実行時間を計測するデコレータ """
	def wrap_func(*args, **kwargs):
		start_time = datetime.now()
		rtrn = func(*args, **kwargs)
		end_time = datetime.now()
		diff_time = end_time - start_time
		print(f"実行時間は {diff_time.total_seconds()} 秒です")
		return rtrn
	return wrap_func