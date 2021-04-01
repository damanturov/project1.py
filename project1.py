spisok = [ 5, 3, 8, 13, 5, 6, 8, 15, 13, 5, 5, 8]
spisok_set = set(spisok)
spisok_list = list(spisok_set)
spisok_list.append(spisok_list[0:6])
#print(type(spisok_list))
print(spisok_list)
