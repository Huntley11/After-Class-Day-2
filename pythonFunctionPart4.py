# Write a Python function called max_num()to find the maximum of three numbers.
def max_value(num1, num2, num3):
    max_value = max(num1, num2, num3)
    return max_value

print(max_value(7, 2, 11))

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(list_num):
    result = 1
    for num in list_num:
        result *= num
    return result

my_list = [2, 3, 7, 2]
result = mult_list(my_list)
print(result)

# Write a Python function called rev_string() to reverse a string.
def rev_string(string):
    return string[::-1]

print(rev_string("Huntley"))

# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(number, start, end):
    return start <= number <= end

result = num_within(9, 5, 16)
print(result)  # Output: True

result = num_within(21, 5, 16)
print(result)  # Output: False

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
# was lost so I used chatgpt still trying to understand this

def pascal(n):
    triangle = []
    for i in range(n):
        row = [1]  # First element of each row is always 1
        if triangle:
            prev_row = triangle[-1]  # Get the previous row
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j+1])  # Compute the next element
            row.append(1)  # Last element of each row is always 1
        triangle.append(row)
        print(' '.join(str(num) for num in row).center(n*4))  # Print the row centered
    
pascal(5)