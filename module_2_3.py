my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_list_new = 0
while my_list_new < len(my_list):
    if my_list[my_list_new] > 0:
        print(my_list[my_list_new])
        my_list_new += 1
        continue
    elif my_list[my_list_new] == 0:
        my_list_new += 1
    else:
        break


