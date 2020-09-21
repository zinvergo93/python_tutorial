import math

sale_prices = [
    100,
    83,
    220,
    40,
    100,
    400,
    10,
    1,
    3
]

# sorted_list = sorted(sale_prices)
# print(sorted_list)

# list_length = len(sale_prices)
# print(list_length)

# sliced_list_one = slice(0, 4)
# sliced_list_two = slice(5, 9)
# median_value = slice(4,5)

# print(sorted_list[sliced_list_one])
# print(sorted_list[sliced_list_two])
# print(sorted_list[median_value])

# Jordan's solution

sorted_list = sorted(sale_prices)
num_of_sales = len(sorted_list)
half_slice = math.floor(num_of_sales/2)
first_sale_items = sorted_list[:half_slice]
last_sale_items = sorted_list[-(half_slice):]
median = sorted_list[half_slice:(half_slice + 1)]


print(sorted_list)
print(num_of_sales)
print(first_sale_items)
print(last_sale_items)
print(median)
