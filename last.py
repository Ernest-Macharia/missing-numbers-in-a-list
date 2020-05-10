def find_missing(num_list):
	first_list = [x for x in range(num_list[1], num_list[-1]+1)]
	num_list = set(num_list)

	return  (list(num_list ^ set(first_list)))


print(find_missing([1,2,3,4,6,7,10]))
print(find_missing([10,11,12,14,17]))
