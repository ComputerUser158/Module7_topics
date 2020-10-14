"""
Author: Rawley Collins
Program: sort_and_search_list.py

"""


def sort_list(newList):
	pass
	"""newList.sort()
	return newList # I returned a list because I needed to print out the list after it was sorted"""


def search_list(newList):
	userInput = int(input("input what you would like to find in the list: "))
	if userInput in newList:
		return newList.index(userInput)
	else:
		return -1


def make_list():
	u_list = []
	counter = 0
	for i in range(0, 3):
		while counter < 3:
			try:
				u_input = int(input("enter a number between 1 and 50:"))
				if u_input < 1 or u_input > 50:
					raise ValueError
				else:
					u_list.insert(counter, u_input)
					counter = counter + 1
			except ValueError:
				print("That wasn't valid input try again,")
	return u_list


if __name__ == '__main__':
	# test_list = make_list()
	# sort_list()
	newList = make_list()
	print(newList)
	# print(sort_list(newList))
	# userInput = int(input("input what you would like to find in the list: "))
	print(search_list(newList))
