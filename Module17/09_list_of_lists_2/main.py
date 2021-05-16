nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_list = [number for next_list in nice_list for next_list_2 in next_list for number in next_list_2]
print('Ответ: ', new_list)
