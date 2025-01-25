# def print_even_numbers(start_num, n):
#     count = 0
#     while count < n:
#         if start_num % 2 == 0:
#             print(start_num)
#             # print(count)
#             count += 1
#         start_num += 1



def print_even_numbers(start, n):
    count = 0
    while count < n:
        if start % 2 == 0:
            print(start)
            count += 1
        start += 1



# Example usage:
start_num = 42  # Starting number
n = 5          # Number of even numbers to print
print_even_numbers(start_num, n)
