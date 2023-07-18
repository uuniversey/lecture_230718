


# type conversion

#  문자열 형변환
my_str = 'Hello SSAFY!'
conv_list = list(my_str)
my_list = [my_str]
conv_set = set(my_str)
# conv_dict =dict(my_str) # 불가능



# print(conv_list)
# print(my_list)
# print(conv_set)


my_list = [10, 20, 30, 20, 10]
conv_str = str(my_list) # '[10, 20, 30, 20, 10]'
conv_tup = tuple(my_list)
conv_set = set(my_list)


print(conv_str[0], type(conv_str))
print(conv_tup)
print(conv_set)
