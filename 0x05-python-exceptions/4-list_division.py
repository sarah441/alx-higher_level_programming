#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    for i in range(list_length):
        try:
            element = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            element = 0
            print("division by 0")
        except IndexError:
            element = 0
            print("out of range")
        except TypeError:
            print("wrong type")
            element = 0
        finally:
            n_list.append(element)
    return n_list
