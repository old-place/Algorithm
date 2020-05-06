import unittest

from is_prime import is_prime


class PrimeNumberTest(unittest.TestCase):

	def test_is_prime_ok(self):
		""" 素数である数のテスト """

		for i in [2, 3, 5, 7, 11, 13, 17, 19]:
			self.assertTrue(is_prime(i))

	def test_is_prime_no(self):
		""" 素数でない数のテスト """
		for i in [1, 4, 6, 8, 9, 10, 12, 14, 15, 18, 20]:
			self.assertFalse(is_prime(i))

	def test_is_prime_negative(self):
		""" 負の数のテスト """
		self.assertFalse(is_prime(-1))
