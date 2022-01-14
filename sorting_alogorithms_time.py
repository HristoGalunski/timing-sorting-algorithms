from random import randint
import numpy as np
import timeit
import time


class Algorithm:
	def __init__(self, name, size):
		self.array = np.random.randint(0, 100, size)
		self.name = name


class BubbleSort(Algorithm):
	def __init__(self):
		super().__init__("BubbleSort", ARRAY_SIZE)

	def run(self):
		for i in range(len(self.array)):
			for j in range(len(self.array) - 1 - i):

				if self.array[j] > self.array[j + 1]:
					self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]


class InsertionSort(Algorithm):
	def __init__(self):
		super().__init__("InsertionSort", ARRAY_SIZE)

	def run(self):
		for i in range(1, len(self.array)):
			to_insert = self.array[i]
			j = i - 1

			while j >= 0 and self.array[j] > to_insert:
				self.array[j + 1] = self.array[j]
				j -= 1

			self.array[j + 1] = to_insert


class MergeSort(Algorithm):
	def __init__(self):
		super().__init__("MergeSort", ARRAY_SIZE)

	def run(self, low=0, high=None):
		if high == None:
			high = len(self.array) - 1

		if low < high:
			middle = low + (high - low) // 2

			self.run(low, middle)
			self.run(middle + 1, high)
			self.merge(low, middle, high)

	def merge(self, low, middle, high):
		helper = self.array.copy()
		i, j, k = low, middle+1, low

		while i <= middle and j <= high:
			if helper[i] < helper[j]:
				self.array[k] = helper[i]
				i += 1
			else:
				self.array[k] = helper[j]
				j += 1
			k += 1

		while i <= middle and k <= high:
			self.array[k] = helper[i]
			i += 1
			k += 1

		while j <= high and k <= high:
			self.array[k] = helper[j]
			i += 1
			k += 1
		return
		
	
class SelectionSort(Algorithm):
	def __init__(self):
		super().__init__("SelectionSort", ARRAY_SIZE)

	def run(self):
		for i in range(len(self.array)):
			index = i
			for j in range(i+1, len(self.array)):
				if self.array[j] < self.array[index]:
					i = j
			self.array[i], self.array[index] = self.array[index], self.array[i]


if __name__ == "__main__":
	ARRAY_SIZE = 20

	algorithms_dict = {
		"BubbleSort" : BubbleSort(),
		"InsertionSort" : InsertionSort(),
		"MergeSort" : MergeSort(),
		"SelectionSort" : SelectionSort()
	}

	for i in algorithms_dict:
		alg = algorithms_dict[i]
		print(f"{i} Algorithm: {timeit.timeit(lambda: alg.run(), number = 1000)}")
