"""
Author: Rawley Collins
Program: basic_IO.py

"""
FILE_NAME = 'student_info.txt'
MAX = 50
MIN = 1
IOERROR_MES = "cannot open file on file system"


def write_to_file(*args):
	print(args)
	try:
		with open(FILE_NAME, 'a') as f:
			f.write('{} {}:\t'.format(args[1], args[0]))
			for i in args[2]:
				f.write('{}\t'.format(i))
			f.write('\n')
	except IOError:
		print(IOERROR_MES)


def get_student_info(**kwargs):
	print("Welcome {} {}".format(kwargs['firstName'], kwargs['lastName']))
	scores = []
	num = 0
	while num != -1:
		try:
			num = float(input("Enter a score between {} and {}, (-1 to exit)".format(MIN, MAX)))
			if num == -1:
				break
			elif num < MIN or MAX < num:
				raise ValueError("Score must be between {} and {}, (-1 to exit)".format(MIN, MAX))
			else:
				scores.append(num)
		except ValueError as err:
			print(err)
	write_to_file(kwargs['firstName'], kwargs['lastName'], scores)


def read_from_file():
	try:
		with open(FILE_NAME, 'r') as f:
			read_line = f.read()
			print(read_line)
	except IOError:
		print(IOERROR_MES)


if __name__ == '__main__':
	get_student_info(firstName='Rawley', lastName='Collins')
	get_student_info(firstName='Jacob', lastName='Yu')
	get_student_info(firstName='Morgan', lastName='MaCarley')
	get_student_info(firstName='Jack', lastName='Douglas')
	input("hold....")
	read_from_file()
	input("press any key to end")
