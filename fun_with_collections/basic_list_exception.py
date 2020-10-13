"""
Author: Rawley Collins
Program: basic_list_exception.py


"""


def make_list():
    u_list = []
    for i in range(0, 3):
        try:
            u_input = int(get_input())
            if u_input < 1 or u_input > 50:
                raise ValueError
        except ValueError:
            raise ValueError
        else:
            u_list.insert(i, u_input)
    return u_list


def get_input():
    u_input = input("enter a number: ")
    return u_input


if __name__ == '__main__':
    test_list = make_list()
    print(test_list)
