

def convert_to_binary(num: int) -> str :
	""" 10進数を2進数に変換する """
	binary = ''

	while num > 0:
		binary += str(num % 2)
		num = num // 2

	return binary[::-1] + '(2)'



def convert_to_decimal(binary: str) -> int:
	""" 2進数を10進数に変換する """
	if binary[-3:] == '(2)':
		binary = binary[:-3]

	decimal_num = 0

	for i, bin in enumerate(binary[::-1]):
		decimal_num += int(bin) * 2 ** i

	return decimal_num



if __name__ == '__main__':
	print(convert_to_binary(5))
	print(convert_to_binary(8))
	print(convert_to_binary(15))

	print(convert_to_decimal('101'))
	print(convert_to_decimal('1000(2)'))
	print(convert_to_decimal('1111(2)'))