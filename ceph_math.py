#However, the problems are arranged a little strangely; they seem to be presented next to each
#  other in a very long horizontal list. For example:

# 123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  
# Each problem's numbers are arranged vertically; at the bottom of the problem is the symbol
#  for the operation that needs to be performed. Problems are separated by a full column of 
# only spaces. The left/right alignment of numbers within each problem can be ignored.

# So, this worksheet contains four problems:

# 123 * 45 * 6 = 33210
# 328 + 64 + 98 = 490
# 51 * 387 * 215 = 4243455
# 64 + 23 + 314 = 401

#Part 2: Cephalopod math is written right-to-left in columns. Each number is given in its own
# column, with the most significant digit at the top and the least significant digit at the 
# bottom. (Problems are still separated with a column consisting only of spaces, and the symbol 
# at the bottom of the problem is still the operator to use.)

# Here's the example worksheet again:

# 123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  
# Reading the problems right-to-left one column at a time, the problems are now quite different:

# The rightmost problem is 4 + 431 + 623 = 1058
# The second problem from the right is 175 * 581 * 32 = 3253600
# The third problem from the right is 8 + 248 + 369 = 625
# Finally, the leftmost problem is 356 * 24 * 1 = 8544
import numpy as np

#get data
with open("ceph_math_data.txt", "r") as file:
    data = file.read().strip().split("\n")
#create 2d array except for the last value
#print(data)
data_array = np.array([line.split() for line in data[:-1]], dtype=int)
data_alignmentarray = data[:-1]
#print("Data array:", data_array)
#get last value for operations
operations = data[-1].split()  # ['+', '*', '+', '*']

# Build masks based on operations
#- Produces a list of booleans: True if the symbol is "*", False otherwise.
multiply_mask = np.array([op == '*' for op in operations])
cumulative_mask = np.array([op == '+' for op in operations])

# Separate arrays by column based on masks
#- Uses the boolean mask to select columns of data_array where the operator was "*"
multiply_array = data_array[:, multiply_mask]
cumulative_array = data_array[:, cumulative_mask]
#print("Multply array:", multiply_array)
#sum all dis bitches vertically numpy is useful
vertical_sums = np.sum(cumulative_array, axis=0)
vertical_products = np.prod(multiply_array, axis=0)

# Calculate totals separately and add these fools together
total_sums = np.sum(vertical_sums)
total_products = np.sum(vertical_products)
cumulative_total = total_sums + total_products

print(f"Total sums: {total_sums}")
print(f"Total products: {total_products}")
print(f"Cumulative total is: {cumulative_total}")

# part 2
#create alginment mask
#print("Data alignment array:", data_alignmentarray)
width_mask = []
column_index = 0
#get the width of each column based on numbers and spaces
for Line_index,line in enumerate(data_alignmentarray): 
  #print("Processing line:", Line_index, line) 
  max_char_width = 0
  has_found_number = False
  column_counter = 0
  for index, j in enumerate(range(len(line))):
    #get the max length of the numbers in each column
    col_chars = line[j] 
    #check if j is numeric
    if col_chars.isnumeric():
      #print("Found number", col_chars, "at column", j)
      has_found_number = True
      max_char_width += 1    
    elif has_found_number:
      #print("Found space after number at column", j)
      #max column width found for this line and this column
      has_found_number = False
      if Line_index == 0:
        width_mask.append(max_char_width)
      else:
        if max_char_width > width_mask[column_counter]:
          width_mask[column_counter] = max_char_width
      max_char_width = 0
      column_counter += 1
    if index == len(line) - 1 and has_found_number:
      if Line_index == 0:
        width_mask.append(max_char_width)
      else:
        if max_char_width > width_mask[column_counter]:
          width_mask[column_counter] = max_char_width
      column_counter = 0
#Data alignment array: ['123 328  51 64 ', ' 45 64  387 23 ', '  6 98  215 314']   
#
chunks = []
#turn the data on it's side rows become columns
for index, line in enumerate(data_alignmentarray):
    column_counter = 0   
    for column in range(len(width_mask)): 
      #get chunks from line
      #print("Getting chunk for column", column_counter, "with width", width_mask[column_counter])
      chunk = line[:width_mask[column_counter]]
      line = line[width_mask[column_counter]+1:]
      if index == 0:
        chunks.append([chunk])
      else:
        chunks[column_counter].append(chunk)
      column_counter += 1
#print("Chunks:", chunks)
#Chunks: [['123', ' 45', '  6'], ['328', '64 ', '98 '], [' 51', '387', '215'], ['64 ', '23 ', '314']]
#conver the columnar data into vertical numbers
numbers = []
for index, chunk in enumerate(chunks):
  vertical_numbers = []
  for number_index, number in enumerate(chunk):
    #print("Building number from chunk:", chunk,"number:", number)
    for column_index,i in enumerate(range(width_mask[index])):
      if number_index == 0:
        # print("width_mask[column_index]:", width_mask[index])
        # print("i:", i)
        # print("column_index:", column_index)
        # print("Adding new vertical number:", number[width_mask[index] - i - 1])
        vertical_numbers.append(number[width_mask[index] - i - 1])
      else:
        #print("Adding to existing vertical number:", vertical_numbers[i], "number_index:", number_index, "i:", i, "width_mask[column_index]:", width_mask[column_index])
        vertical_numbers[i] += number[width_mask[index] - i - 1]
    #print("Vertical numbers:", vertical_numbers)
  numbers.append(vertical_numbers)
  #print("Numbers:", numbers)
#print("Numbers:", numbers)
#Numbers: [['356', '24 ', '1  '], ['8  ', '248', '369'], ['175', '581', ' 32'], ['  4', '431', '623']]
part2_cumulative_total = 0
for number_index,number in enumerate(numbers):
  if operations[number_index] == '*':
    part2_cumulative_total += np.prod([int(n.strip()) for n in number])
  else:
    part2_cumulative_total += np.sum([int(n.strip()) for n in number])
print(f"Part 2 - Cumulative total is: {part2_cumulative_total}")

# The rightmost problem is 4 + 431 + 623 = 1058
# The second problem from the right is 175 * 581 * 32 = 3253600
# The third problem from the right is 8 + 248 + 369 = 625
# Finally, the leftmost problem is 356 * 24 * 1 = 8544
#Now, the grand total is 1058 + 3253600 + 625 + 8544 = 3263827.