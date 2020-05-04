import math

def calc_charge(price: int, payed_amount: int):
	"""
	Args:
		price: 金額
		payed_amount: 出したお金
	"""
	if price > payed_amount:
		print('金額が不足しています')
		return

	charge_amount = payed_amount - price

	currency_types = [10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
	charge = dict(zip(currency_types, [0]*len(currency_types)))

	for currency_type in currency_types:
		if charge_amount >= currency_type:
			currency_num = math.floor(charge_amount / currency_type)
			charge[currency_type] = currency_num
			charge_amount -= currency_type * currency_num


	print(payed_amount - price, '円のお釣り')
	for curreny, num in charge.items():
		if num > 0:
			print(f"{curreny}円 {num}枚")

if __name__ == '__main__':
	calc_charge(2356, 3000)
